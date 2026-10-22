import json
D="/Users/ethill/workspace/scratch/pulse/hyperliquid-refdata/"
DEXS=["core","xyz","flx","vntl","hyna","km","abcd","cash","para","mkts","io"]
ctx={}
for d in DEXS:
    m,c=json.load(open(f"{D}ctx_{d}.json"))
    for u,x in zip(m["universe"],c):
        t=u["name"].split(":",1)[-1].upper()
        ctx[(d,t)]=dict(vlm=float(x["dayNtlVlm"]), oi=float(x["openInterest"])*float(x["markPx"]),
                        mark=float(x["markPx"]))
sm,sc=json.load(open(f"{D}ctx_spot.json"))
toks={t["index"]:t for t in sm["tokens"]}
spot={}
for p,x in zip(sm["universe"],sc):
    b=toks.get(p["tokens"][0])
    if b: spot[b["name"].upper()]=dict(vlm=float(x["dayNtlVlm"]), mark=float(x.get("markPx") or 0))

AMB={"UNITREE":[("xyz",),("para",)],"NBIS":[("xyz",),("io",)],"ORCL":[("xyz",),("spot",)],
     "SNDK":[("xyz",),("io",)],"IREN":[("xyz",),("para",)],
     "HOOD":[("xyz",),("cash",),("spot",)],"CRCL":[("xyz",),("flx",),("spot",)],
     "COPPER":[("xyz",),("flx",)]}
def f(v): return f"${v/1e6:>8.2f}M" if v>=1e6 else f"${v/1e3:>8.1f}K"
for t,vs in AMB.items():
    print(f"\n{t}")
    rows=[]
    for (d,) in vs:
        if d=="spot":
            s=spot.get(t)
            rows.append(("spot", s["vlm"] if s else 0, None, s["mark"] if s else 0))
        else:
            c=ctx.get((d,t))
            rows.append((d, c["vlm"] if c else 0, c["oi"] if c else 0, c["mark"] if c else 0))
    rows.sort(key=lambda r:-r[1])
    for i,(d,v,oi,mk) in enumerate(rows):
        star=" <-- deepest" if i==0 and v>0 else ""
        print(f"   {d:<6s} 24h vlm {f(v)}   OI {f(oi) if oi is not None else '       n/a':>10s}   mark {mk:g}{star}")
print("\n--- unique ones, for reference ---")
UNI={"LYTE":"xyz","NATGAS":"xyz","ZHIPU":"xyz","MINIMAX":"xyz","GPRO":"io","OAI":"io",
     "SOXL":"xyz","SKHX":"xyz","HYUNDAI":"xyz","KORU":"xyz","BB":"xyz","LLY":"xyz","AMAT":"xyz"}
for t,d in UNI.items():
    c=ctx.get((d,t))
    print(f"   {t:<8s} {d:<5s} 24h vlm {f(c['vlm'])}   OI {f(c['oi'])}   mark {c['mark']:g}")
