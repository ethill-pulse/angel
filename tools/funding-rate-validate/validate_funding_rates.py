#!/usr/bin/env python3
"""
Validate that every target CLST symbol has a funding rate settlement for every
slot in the trailing window of mktdata.fundingrate.

Usage:
  python3 validate_funding_rates.py <raw.yml> [--hours N] [--grace-minutes M] [--all] [--now ISO]

Expected slots come from each settlement's funding_interval_ms (the gap since the
previous settlement). Walking back from the newest settlement, each settlement says
where the one before it should be; a slot with no settlement is a gap. After the
newest settlement, slots keep coming at its interval, and any whose time plus the
grace period has passed are also gaps.

Settlements without an interval (data written before the field existed, or a seed
with no predecessor) fall back to the interval inferred from the gaps between
settlements. Intervals must divide 24h (1h, 2h, 3h, 4h, 6h, 8h, 12h, 24h) and slots
must sit on that grid from 00:00 UTC; anything else is reported.

Exits 0 if clean, 1 if any symbol is missing, has gaps, or has an invalid interval.
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone

ALL_TARGET = {
    "CLST.SPOT.ANTHROPIC-USD",
    "CLST.SPOT.OPENAI-USD",
    "CLST.SPOT.NVDA-USD",
    "CLST.SPOT.COIN-USD",
    "CLST.SPOT.BABA-USD",
    "CLST.SPOT.SNDK-USD",
    "CLST.SPOT.LYTE-USD",
    "CLST.SPOT.NATGAS-USD",
    "CLST.SPOT.UNITREE-USD",
    "CLST.SPOT.NBIS-USD",
    "CLST.SPOT.ZHIPU-USD",
    "CLST.SPOT.MINIMAX-USD",
    "CLST.SPOT.GPRO-USD",
    "CLST.SPOT.OAI-USD",
    "CLST.SPOT.SOXL-USD",
    "CLST.SPOT.ORCL-USD",
    "CLST.SPOT.SKHX-USD",
    "CLST.SPOT.HYUNDAI-USD",
    "CLST.SPOT.KORU-USD",
    "CLST.SPOT.BB-USD",
    "CLST.SPOT.LLY-USD",
    "CLST.SPOT.AMAT-USD",
    "CLST.SPOT.IREN-USD",
    "CLST.SPOT.HOOD-USD",
    "CLST.SPOT.CRCL-USD",
    "CLST.SPOT.COPPER-USD",
    "CLST.SPOT.AVGO-USD",
}

HOUR = timedelta(hours=1)
DAY_HOURS = 24
VALID_HOURS = [h for h in range(1, DAY_HOURS + 1) if DAY_HOURS % h == 0]
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("raw", nargs="?", default="fundingrate-cs-dev-raw.yml", help="kafka-capture dump")
    p.add_argument("--hours", type=int, default=24, help="trailing window to validate (default 24)")
    p.add_argument("--grace-minutes", type=int, default=15,
                   help="how long after a slot before its absence counts as a gap (default 15)")
    p.add_argument("--all", action="store_true",
                   help="validate every symbol in the capture, not just the CLST target list")
    p.add_argument("--now", help="evaluate as of this UTC time (ISO 8601) instead of the clock")
    return p.parse_args()


# ── parse capture dump ────────────────────────────────────────────────────────
def read_blocks(path):
    blocks, current = [], []
    with open(path) as f:
        for line in f:
            if line.strip() == "---":
                if current:
                    blocks.append(current)
                current = []
            else:
                current.append(line.rstrip())
    if current:
        blocks.append(current)
    return blocks


def extract_mapped_value(block):
    in_mapped = False
    for line in block:
        if line.strip() == "mapped:":
            in_mapped = True
        if in_mapped and "value:" in line:
            m = re.search(r"value:\s+'(.+)'$", line)
            if m:
                try:
                    return json.loads(m.group(1))
                except ValueError:
                    pass
    return None


def parse_ts(ts_str):
    ts_str_us = re.sub(r"(\.\d{6})\d+", r"\1", ts_str)
    return datetime.fromisoformat(ts_str_us.replace("Z", "+00:00"))


def interval_hours(interval_ms):
    """Round a derived interval (venue timestamps jitter by ms) to whole hours."""
    if interval_ms is None:
        return None
    return max(1, round(int(interval_ms) / 3_600_000))


def to_slot(ts):
    """Settlements land a few ms after the boundary; floor to the minute."""
    return ts.replace(second=0, microsecond=0)


def collect(blocks, targets):
    """symbol -> {slot: interval_hours or None}; duplicates keep any interval seen."""
    by_symbol = defaultdict(dict)
    for block in blocks:
        val = extract_mapped_value(block)
        if not val:
            continue
        symbol = val.get("symbol", "")
        if targets is not None and symbol not in targets:
            continue
        for entry in val.get("entries", []):
            if entry.get("type") != "funding_rate":
                continue
            try:
                slot = to_slot(parse_ts(entry.get("ts", "")))
            except ValueError:
                continue
            hours = interval_hours(entry.get("funding_interval_ms"))
            if by_symbol[symbol].get(slot) is None:
                by_symbol[symbol][slot] = hours
    return by_symbol


# ── cadence ───────────────────────────────────────────────────────────────────
def infer_hours(slots):
    """Most common gap between consecutive settlements, rounded to hours."""
    ordered = sorted(slots)
    gaps = Counter(
        round((b - a) / HOUR) for a, b in zip(ordered, ordered[1:]) if b > a
    )
    gaps.pop(0, None)
    if not gaps:
        return None
    return gaps.most_common(1)[0][0]


def on_grid(slot, hours):
    return ((slot - EPOCH) / HOUR) % hours == 0


def expected_slots(settlements, fallback_hours, start, now, grace):
    """Walk back from the newest settlement using each one's own interval, then
    project forward from it. Returns (expected slots in window, intervals used)."""
    newest = max(settlements)
    newest_hours = settlements[newest] or fallback_hours
    expected, used = set(), []

    nxt = newest + timedelta(hours=newest_hours)
    while nxt + grace <= now:
        if nxt >= start:
            expected.add(nxt)
        nxt += timedelta(hours=newest_hours)

    cur, hours = newest, newest_hours
    while cur >= start:
        if cur < now:
            expected.add(cur)
        own = settlements.get(cur)
        if own is not None:
            hours = own
        if not used or used[-1] != hours:
            used.append(hours)
        cur -= timedelta(hours=hours)
    used.reverse()
    return expected, used


def fmt_hours(hours_list):
    return "→".join(f"{h}h" for h in hours_list)


# ── validate ──────────────────────────────────────────────────────────────────
def main():
    args = parse_args()
    now = parse_ts(args.now) if args.now else datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    start = now - timedelta(hours=args.hours)
    grace = timedelta(minutes=args.grace_minutes)

    targets = None if args.all else ALL_TARGET
    by_symbol = collect(read_blocks(args.raw), targets)
    symbols = sorted(targets if targets is not None else by_symbol)

    print(f"Validation window: [{start.strftime('%Y-%m-%dT%H:%MZ')} — {now.strftime('%Y-%m-%dT%H:%MZ')}), "
          f"grace {args.grace_minutes}m\n")

    ok = True
    for sym in symbols:
        settlements = by_symbol.get(sym, {})
        if not settlements:
            print(f"  MISSING  {sym} — no settlements in topic")
            ok = False
            continue

        inferred = infer_hours(settlements)
        fallback = inferred
        if fallback is None:
            fallback = next((h for h in settlements.values() if h is not None), None)
        if fallback is None:
            print(f"  OK?      {sym} — 1 settlement in topic, no interval to check against")
            continue

        expected, used = expected_slots(settlements, fallback, start, now, grace)
        source = "" if any(settlements[s] is not None for s in settlements if s >= start) else ", inferred"
        label = f"{fmt_hours(used)}{source}"

        problems = []
        bad_hours = sorted({h for h in used if h not in VALID_HOURS})
        if bad_hours:
            problems.append(f"interval not a divisor of 24h: {fmt_hours(bad_hours)}")
        misaligned = sorted(s for s in settlements if start <= s < now and not any(on_grid(s, h) for h in used))
        if misaligned:
            problems.append("off-grid: " + ", ".join(s.strftime("%H:%MZ") for s in misaligned[:6]))

        missing = sorted(s for s in expected if s not in settlements)
        covered = len(expected) - len(missing)
        if missing:
            shown = ", ".join(s.strftime("%m-%d %H:%MZ") for s in missing[:6])
            more = f" (+{len(missing) - 6} more)" if len(missing) > 6 else ""
            problems.insert(0, f"missing: {shown}{more}")

        if problems:
            ok = False
            print(f"  GAPS     {sym} ({label}) — {covered}/{len(expected)} slots covered, " + "; ".join(problems))
        else:
            print(f"  OK       {sym} ({label}) — {covered}/{len(expected)} slots covered")

    print()
    if ok:
        print(f"ALL OK — all {len(symbols)} symbols have complete settlement data for the last {args.hours} hours.")
        sys.exit(0)
    print("ISSUES FOUND — see above.")
    sys.exit(1)


if __name__ == "__main__":
    main()
