import json, sys
D = "/Users/ethill/workspace/scratch/pulse/hyperliquid-refdata/"
dexs = json.load(open(D+"perpDexs.json"))
perp = json.load(open(D+"allPerpMetas.json"))
sm   = json.load(open(D+"spotMeta.json"))
toks = {t["index"]: t for t in sm["tokens"]}

WANT = """LYTE NATGAS UNITREE NBIS ZHIPU MINIMAX GPRO OAI SOXL ORCL SKHX
HYUNDAI KORU SNDK BB LLY AMAT IREN HOOD CRCL COPPER""".split()

def ok(n):
    n = n.replace(":", "_")
    return all(c.isascii() and (c.isalnum() or c == "_") for c in n)

# every perp the fetcher would emit, indexed by bare ticker (post dex prefix)
perp_by_ticker = {}
all_perp_names = []
for i, m in enumerate(perp):
    dex = dexs[i]["name"] if i and dexs[i] else ""
    ct = m.get("collateralToken") or 0
    quote = toks.get(ct, {}).get("name")
    off = 0 if i == 0 else 100000 + i*10000
    for j, x in enumerate(m.get("universe", [])):
        raw = x["name"]
        all_perp_names.append(raw)
        if not ok(raw):
            continue
        ticker = raw.split(":", 1)[1] if ":" in raw else raw
        sym = f"HYPL.PERP.{raw.replace(':','_')}-{quote}:{quote}"
        perp_by_ticker.setdefault(ticker.upper(), []).append(
            dict(dex=dex or "(core)", dex_idx=i, sym=sym, venue_symbol=raw,
                 alt=j+off, quote=quote, szdec=x["szDecimals"],
                 lev=x.get("maxLeverage"), iso=x.get("onlyIsolated")))

# spot: base-asset ticker -> emitted symbol
spot_by_ticker = {}
for p in sm["universe"]:
    b = toks.get(p["tokens"][0]); q = toks.get(p["tokens"][1])
    if not b or not q: continue
    spot_by_ticker.setdefault(b["name"].upper(), []).append(
        dict(sym=f"HYPL.SPOT.{b['name']}-{q['name']}", venue_symbol=p["name"],
             alt=p["index"]+10000, szdec=b["szDecimals"]))
tok_names = {t["name"].upper() for t in sm["tokens"]}

print("=" * 100)
for w in WANT:
    ps = perp_by_ticker.get(w, []); ss = spot_by_ticker.get(w, [])
    n = len(ps) + len(ss)
    tag = "MISS" if n == 0 else ("UNIQUE" if n == 1 else f"AMBIGUOUS x{n}")
    print(f"\n{w:10s} {tag}")
    for p in ps:
        print(f"    perp  dex={p['dex']:<6s} {p['sym']:<40s} venue={p['venue_symbol']:<20s} "
              f"alt={p['alt']:<7d} szDec={p['szdec']} lev={p['lev']} iso={p['iso']}")
    for s in ss:
        print(f"    spot  {'':11s} {s['sym']:<40s} venue={s['venue_symbol']:<20s} alt={s['alt']}")
    if n == 0:
        near = sorted({t for t in list(perp_by_ticker)+list(spot_by_ticker)
                       if w in t or t in w or
                       (len(t)>2 and len(w)>2 and (t[:3]==w[:3] or t[-3:]==w[-3:]))})
        if near: print(f"    near-misses: {', '.join(near[:14])}")
        if w in tok_names: print(f"    NOTE: exists as a spot TOKEN but in no listed pair")
print("\n" + "="*100)
print(f"total perps emitted: {sum(len(v) for v in perp_by_ticker.values())} "
      f"(skipped by char filter: {sum(1 for n in all_perp_names if not ok(n))})")
print(f"total spot pairs emitted: {sum(len(v) for v in spot_by_ticker.values())}")
