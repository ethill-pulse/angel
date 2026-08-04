team priorities

## Performance

- disk-backed queue for back-pressure
    - benchmark framework (eric)
    - possible implementations:
        - in-mem w/ flush on runtime exit (eric)
        - https://github.com/tokahuke/yaque ?
        - fork internally (new and not a lot of downloads) https://github.com/jeffilluminati/khata-rs - chronicle inspired and zero dependency pure rust ?
        - chronicle? (needs paid subscription)
        - aeron archiver?

- async writers that buffer using proposed disk-backed queue
    - benchmark framework (eric)
    - implementations:
        - write to rolling file (for flight recorder) (eric)
        - postgres impl (for fix replay engine)
        - quest impl (for audit trails)

- durable queue + writer API (combine disk-backed queue and writers)

- measuring end to end (erick)

- more robust on flight recorder in polaris
    - needs log rolling
        - 28 days of disk for 2 symbols only
        - 50 symbols will fall apart for disk capture
    - should we pcap as a last resort? (mgow)
    - use proposed disk-backed low-latency reliable queue with rolling file writer
    

- shared memory transports
    - aeron (eric)
    - use between TE and standalone w/ flow (eric)

- quote cache eviction, don't grow forever (talgat)

- check on postgres performance in dev (mgow)

- fewer locks?

## Functional Improvements

- trade-engine need a notional floor so we don't keep re-slicing dust
- passthrough parties testing for active/studio use-case
- orders keyed per session (amit)
- order status lookup (ethill)
- average price on execution report for GTC (amit)
- reverse lookups
- more durable ability to survive crashes between postgres and TE and lookup state
- graceful shutdown and recovery of GTC orders survive crashes between postgres and TE and lookup state (amit)
- security list request in TE (erick)

# Observability Improvements

- profile system and understand hops, need to be able to accurately measure performance improvements
- bi-directional FIX audit trails to questdb (estiven)
- TE main thread audit trail to questdb
- S3 archival of FIX audit trails
- L2 orderbook capture with depth (binance and coinbase)
- Market spreads at depth in charts in Halo


