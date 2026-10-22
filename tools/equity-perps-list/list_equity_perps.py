#!/usr/bin/env python3
"""List Binance UM + Hyperliquid xyz-dex equity perps in pulse admin with market_data_enabled and
historical_candles_enabled set (candles on BINF only; HYPL has no historical candles).

Equity classification comes from the venues' own APIs (pulse refdata doesn't carry
Binance underlyingType or HL asset class). Matching to pulse symbols is by venue_symbol
on the discovered definition, so no symbol-format guessing.

Each instrument goes through POST /refdata/list/instruments, same as the admin UI: it
auto-lists referenced discovered assets, creates the mktdata Kafka topics, and assigns the
symbol to the mktdata scaleset. Already-listed instruments are updated from their listed
definition, so other settings (trading_enabled etc.) are preserved.

Usage:
  1. Log in to the admin UI, then copy sessionStorage 'adminjwt' (devtools > Application).
  2. Dry run (prints the plan, changes nothing):
       ADMIN_JWT=... ./list_equity_perps.py --admin-url https://<cs-dev admin host>
  3. Apply:
       ADMIN_JWT=... ./list_equity_perps.py --admin-url https://<cs-dev admin host> --apply

Caveats:
  - ~300 instruments; that is a lot of new topics + mktdata scaleset assignments at once.
  - HL is xyz dex only; its non-equity names are excluded by the hand-kept HL_EXCLUDE
    list. Review it as xyz adds markets.
"""
import argparse
import concurrent.futures
import json
import os
import sys
import urllib.parse
import urllib.request

BINANCE_EXCHANGE_INFO = "https://www.binance.com/fapi/v1/exchangeInfo"
HL_INFO = "https://api.hyperliquid.xyz/info"

BINANCE_EQUITY_TYPES = {"EQUITY", "HK_EQUITY", "KR_EQUITY", "CN_EQUITY", "PREMARKET"}

DETAIL_WORKERS = 16

CANDLE_VENUES = {"BINF"}

HL_DEX = "xyz"
# non-equity names on xyz: commodities, FX, unknowns
HL_EXCLUDE = {
    "GOLD", "SILVER", "PLATINUM", "PALLADIUM", "COPPER", "CL", "BRENTOIL", "NATGAS",
    "JPY", "EUR", "GBP",
    "PURRDAT",
}


def http(method, url, headers=None, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers or {})
    if data is not None:
        req.add_header("content-type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
        return json.loads(raw) if raw.strip() else None


# Both venue lists are keyed by the base of the pulse product code (BINF "TSLA" from
# baseAsset, HYPL "xyz_TSLA" from the dex-prefixed name) so discovered symbols can be
# matched exactly before any per-symbol fetch.
def binance_equity_symbols():
    info = http("GET", BINANCE_EXCHANGE_INFO)
    return {
        s["baseAsset"]: s["symbol"]
        for s in info["symbols"]
        if s["status"] == "TRADING"
        and s.get("contractType") == "TRADIFI_PERPETUAL"
        and s.get("underlyingType") in BINANCE_EQUITY_TYPES
    }


def hl_equity_symbols():
    meta = http("POST", HL_INFO, body={"type": "meta", "dex": HL_DEX})
    return {
        a["name"].replace(":", "_"): a["name"]  # venue_symbol in pulse is the raw "xyz:TSLA"
        for a in meta["universe"]
        if not a.get("isDelisted") and a["name"].split(":", 1)[-1] not in HL_EXCLUDE
    }


def log(msg):
    print(msg, flush=True)


class Admin:
    def __init__(self, base, jwt):
        self.base = base.rstrip("/")
        self.headers = {"x-pulse-jwt": jwt}

    def get(self, path, **query):
        qs = f"?{urllib.parse.urlencode(query)}" if query else ""
        return http("GET", f"{self.base}/{path}{qs}", self.headers)

    def post(self, path, body):
        return http("POST", f"{self.base}/{path}", self.headers, body)

    def instrument(self, route, symbol):
        return self.get(f"refdata/{route}/instruments/{urllib.parse.quote(symbol, safe='')}")


def main():
    if len(sys.argv) == 1:
        print(__doc__)
        return
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--admin-url", required=True)
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()

    jwt = os.environ.get("ADMIN_JWT")
    if not jwt:
        sys.exit("set ADMIN_JWT (sessionStorage 'adminjwt' from the admin UI)")
    admin = Admin(args.admin_url, jwt)

    log("fetching venue equity lists")
    wanted = {"BINF": binance_equity_symbols(), "HYPL": hl_equity_symbols()}
    for venue, syms in wanted.items():
        log(f"{venue}: {len(syms)} equity perps at venue")

    candidates = []
    for venue, by_base in wanted.items():
        log(f"{venue}: fetching discovered perps from admin")
        page = admin.get("refdata/disc/instruments", venue=venue, q=".PERP.", limit=0)
        matched = [
            (venue, row["id"], row.get("listed", False))
            for row in page["values"]
            if row["id"].split(".PERP.", 1)[1].split("-", 1)[0] in by_base
        ]
        log(f"{venue}: {page['total']} discovered perps, {len(matched)} match")
        candidates.extend(matched)

    def fetch(candidate):
        venue, sym, listed = candidate
        return venue, sym, listed, admin.instrument("list" if listed else "disc", sym)

    log(f"fetching {len(candidates)} definitions")
    plan, missing = [], {v: set(by_base.values()) for v, by_base in wanted.items()}
    with concurrent.futures.ThreadPoolExecutor(DETAIL_WORKERS) as pool:
        for i, (venue, sym, listed, defn) in enumerate(pool.map(fetch, candidates), 1):
            if i % 50 == 0:
                log(f"  {i}/{len(candidates)}")
            if defn.get("venue_symbol") not in missing[venue]:
                continue
            missing[venue].discard(defn["venue_symbol"])
            candles = venue in CANDLE_VENUES
            if (
                listed
                and defn.get("market_data_enabled")
                and (not candles or defn.get("historical_candles_enabled"))
            ):
                continue
            defn["market_data_enabled"] = True
            if candles:
                defn["historical_candles_enabled"] = True
            plan.append((sym, "enable" if listed else "list+enable", defn))

    for sym, action, _ in plan:
        print(f"  {action:12} {sym}")
    print(f"{len(plan)} to apply")
    for venue, syms in missing.items():
        if syms:
            print(f"{venue}: {len(syms)} not in pulse discovered refdata: {' '.join(sorted(syms))}")

    if not args.apply:
        print("dry run; pass --apply to POST")
        return

    failed = 0
    for i, (sym, _, defn) in enumerate(plan, 1):
        log(f"  [{i}/{len(plan)}] {sym}")
        try:
            admin.post("refdata/list/instruments", defn)
        except urllib.error.HTTPError as e:
            failed += 1
            print(f"FAIL {sym}: {e.code} {e.read().decode(errors='replace')[:200]}")
    print(f"done: {len(plan) - failed} ok, {failed} failed")


if __name__ == "__main__":
    main()
