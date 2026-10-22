# HYPL mark price — live smoke tests & capture scripts

Scratch artifacts from building `MarketDataFeedType::MarkPrice` for Hyperliquid
(branch `et.hypl_markprice`, Sept 2026). **Private — never reference this path from
`repos/pulse`.** These hit the live venue, so they must never land in the public repo:
CI has no network and they would flake.

## What's here

| File | What it does |
|---|---|
| `live_smoke.rs` | Rust tests driving `HyperliquidFundingRatePoller` against **mainnet** |
| `capture_active_asset_ctx_mainnet.py` | Subscribes `activeAssetCtx` for a perp + spot coin, dumps raw frames |
| `capture_active_asset_ctx_testnet.py` | Same against testnet (used for the `vntls:vANTHRPC` builder-dex frame) |
| `verify_encoder_wire_format.py` | Sends the subscription encoder's byte-for-byte output, checks acks + unsubscribe teardown |
| `captured_frames_*.txt` | The raw frames these produced; source of the repo's test fixtures |

No API keys needed for any of it — HYPL market data is fully public.

## Restoring live_smoke.rs

1. Copy to `libs/venues/crates/venues-hyperliquid/src/integration/mktdata/rest/live_smoke.rs`
2. Add to `.../rest/mod.rs`:
   ```rust
   #[cfg(test)]
   mod live_smoke;
   ```
3. Add to `venues-hyperliquid/Cargo.toml` under `[dev-dependencies]`:
   ```toml
   rustls = { workspace = true }
   ```
4. Run:
   ```
   cd libs/venues && cargo test -p venues-hyperliquid live_smoke -- --nocapture --test-threads=1
   ```

Remove all three before committing.

## Two gotchas that cost real time

Both are artifacts of running venue code *outside* the app — neither affects production.

- **rustls panics** with "Could not automatically determine the process-level CryptoProvider".
  Production installs it in bootstrap. Tests need, once per process:
  `let _ = rustls::crypto::ring::default_provider().install_default();`
- **`NbioHttpClient` DNS fails** with `NonBlockingNameResolver requires Runtime`. The resolver
  needs `RUNTIME_CONTEXT`, so the test must be `#[runtime::test]` (not `#[test]`), which wraps
  the body in `runtime::Runtime::new(2)`.

Also: `funding_rate_instrument_filter` requires `market_data_enabled`, so any instrument the
test seeds into `RefDataCache` must set `.market_data_enabled(true)` or the poller selects
nothing and looks broken.

## What these proved against mainnet

- The new `NonBlockingHttpThrottler::send_post_requests` path works against a real server
- Real `fundingHistory` bodies decode (records ascending, `fundingRate` is a JSON string,
  unmapped `premium` ignored)
- Watermark seeds exactly one settlement per symbol, then suppresses — 0 dupes over 40 re-polls
- Encoder wire bytes accepted for perp *and* spot; unsubscribe produces a clean teardown
- Builder-dex (HIP-3) ctx frames null out `premium`/`midPx`/`impactPxs` when illiquid
