import asyncio, json, ssl, sys, websockets
URL = "wss://api.hyperliquid-testnet.xyz/ws"
COINS = ["vntls:vANTHRPC", "ETH"]
async def run(out):
    async with websockets.connect(URL, ssl=ssl.create_default_context()) as ws:
        for c in COINS:
            await ws.send(json.dumps({"method":"subscribe",
                "subscription":{"type":"activeAssetCtx","coin":c}}))
        seen=set()
        while True:
            raw = await asyncio.wait_for(ws.recv(), timeout=15)
            m = json.loads(raw); ch = m.get("channel")
            if ch == "subscriptionResponse":
                out.write("SUBRESP: %s\n" % raw); out.flush(); continue
            if ch in ("activeAssetCtx","activeSpotAssetCtx"):
                coin = m.get("data",{}).get("coin")
                if coin not in seen:
                    seen.add(coin)
                    out.write("FRAME[%s][%s]: %s\n" % (ch, coin, raw)); out.flush()
            elif ch != "pong":
                out.write("OTHER: %s\n" % raw[:200]); out.flush()
async def main():
    with open(sys.argv[1],"w") as out:
        try: await run(out)
        except Exception as e: out.write("stopped: %s\n" % type(e).__name__); out.flush()
asyncio.get_event_loop().run_until_complete(main())
