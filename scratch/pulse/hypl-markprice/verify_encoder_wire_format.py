import asyncio, json, ssl, sys, websockets

URL = "wss://api.hyperliquid.xyz/ws"
# byte-for-byte what HyperliquidSubscriptionEncoder emits
SUBS = [
  '{"method":"subscribe","subscription":{"type":"activeAssetCtx","coin":"BTC"}}',
  '{"method":"subscribe","subscription":{"type":"activeAssetCtx","coin":"PURR/USDC"}}',
]
UNSUBS = [
  '{"method":"unsubscribe","subscription":{"type":"activeAssetCtx","coin":"BTC"}}',
  '{"method":"unsubscribe","subscription":{"type":"activeAssetCtx","coin":"PURR/USDC"}}',
]

async def run(out):
    async with websockets.connect(URL, ssl=ssl.create_default_context()) as ws:
        for s in SUBS:
            await ws.send(s)
        acks, frames = 0, 0
        try:
            while True:
                m = json.loads(await asyncio.wait_for(ws.recv(), timeout=12))
                ch = m.get("channel")
                if ch == "subscriptionResponse":
                    acks += 1; out.write("ACK %d: %s\n" % (acks, json.dumps(m["data"]))); out.flush()
                elif ch in ("activeAssetCtx","activeSpotAssetCtx"):
                    frames += 1
                    if frames <= 2:
                        out.write("FRAME %s %s\n" % (ch, m["data"]["coin"])); out.flush()
                elif ch == "error":
                    out.write("ERROR: %s\n" % json.dumps(m)); out.flush()
                if acks == 2 and frames >= 2:
                    break
        except Exception as e:
            out.write("phase1 stopped: %s\n" % type(e).__name__)
        out.write("subscribed: acks=%d frames=%d\n" % (acks, frames)); out.flush()

        for u in UNSUBS:
            await ws.send(u)
        out.write("-- sent unsubscribes, watching 12s --\n"); out.flush()
        after = 0
        try:
            while True:
                m = json.loads(await asyncio.wait_for(ws.recv(), timeout=12))
                ch = m.get("channel")
                if ch in ("activeAssetCtx","activeSpotAssetCtx"):
                    after += 1
                elif ch == "subscriptionResponse":
                    out.write("UNSUB ACK: %s\n" % json.dumps(m["data"])); out.flush()
                elif ch == "error":
                    out.write("ERROR: %s\n" % json.dumps(m)); out.flush()
        except Exception:
            pass
        out.write("ctx frames AFTER unsubscribe: %d\n" % after); out.flush()

async def main():
    with open(sys.argv[1],"w") as out:
        try: await run(out)
        except Exception as e: out.write("fatal: %r\n" % e)
asyncio.get_event_loop().run_until_complete(main())
