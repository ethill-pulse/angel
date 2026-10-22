import base64, json, sys
from decimal import Decimal
import cbor2

SETTL = {1: "final", 2: "theoretical"}
ETYPE = {0:"bid",1:"ask",2:"trade",3:"index_price",5:"closing_price",6:"mark_price",
         12:"open_interest",16:"interest_rate",19:"book_reset",22:"funding_rate",
         25:"estimated_settle_price",32:"fixing_price"}

def dec(v):
    if v is None: return None
    mant, scale = v
    b = bytearray(mant)
    b.extend(b"\x00" * (16 - len(b)))
    i = int.from_bytes(bytes(b[:16]), "little", signed=True)
    return str(Decimal(i).scaleb(-scale))

def ts(v):
    if v is None: return None
    import datetime
    return datetime.datetime.fromtimestamp(v/1e9, datetime.timezone.utc).isoformat()

src = sys.argv[1]
want = sys.argv[2] if len(sys.argv) > 2 else None
out = []
counts = {}
for line in open(src):
    r = json.loads(line)
    m = cbor2.loads(base64.b64decode(r["value"]))
    for e in m.get("entries", []):
        sp = SETTL.get(e.get("settl_price_type"))
        et = ETYPE.get(e.get("type"), e.get("type"))
        counts[(et, sp)] = counts.get((et, sp), 0) + 1
        if want and sp != want: continue
        out.append({
            "offset": r["offset"],
            "symbol": m.get("symbol"),
            "ts": ts(m.get("ts")),
            "received": ts(m.get("received")),
            "sent": ts(m.get("sent")),
            "next_funding_time": ts(m.get("next_funding_time")),
            "entry_type": et,
            "settl_price_type": sp,
            "price": dec(e.get("price")),
            "rate": dec(e.get("rate")),
        })
print("# entry census (entry_type, settl_price_type) -> count", file=sys.stderr)
for k, v in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"#   {k[0]:<24} {str(k[1]):<12} {v}", file=sys.stderr)
print(f"# total records={sum(1 for _ in open(src))} matched_entries={len(out)}", file=sys.stderr)
for o in out:
    print(json.dumps(o))
