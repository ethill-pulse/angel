import asyncio, json, ssl, sys, websockets

URL = "wss://api.hyperliquid.xyz/ws"
COINS = ["ETH", "PURR/USDC", "@1"]

async def run(out):
    ctx = ssl.create_default_context()
    seen = {}
    async with websockets.connect(URL, ssl=ctx) as ws:
        for c in COINS:
            await ws.send(json.dumps({"method": "subscribe",
                                      "subscription": {"type": "activeAssetCtx", "coin": c}}))
        while True:
            raw = await asyncio.wait_for(ws.recv(), timeout=20)
            m = json.loads(raw)
            ch = m.get("channel")
            if ch == "subscriptionResponse":
                out.write("SUBRESP: %s\n" % raw); out.flush(); continue
            if ch in ("activeAssetCtx", "activeSpotAssetCtx"):
                coin = m.get("data", {}).get("coin")
                if (ch, coin) not in seen:
                    seen[(ch, coin)] = raw
                    out.write("FRAME[%s][%s]: %s\n" % (ch, coin, raw)); out.flush()
            elif ch != "pong":
                out.write("OTHER: %s\n" % raw[:300]); out.flush()

async def main():
    with open(sys.argv[1], "w") as out:
        try:
            await run(out)
        except Exception as e:
            out.write("stopped: %s\n" % type(e).__name__); out.flush()

asyncio.get_event_loop().run_until_complete(main())
