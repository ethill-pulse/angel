// TEMPORARY live smoke tests against Hyperliquid mainnet. Delete before merge.
// Run with: cargo test -p venues-hyperliquid live_smoke -- --nocapture --test-threads=1
use crate::integration::mktdata::rest::funding_rate::HyperliquidFundingRatePoller;
use httpclient::NbioHttpClient;
use messages_public::schemas::enums::{MdEntryType, SettlPriceType};
use messages_public::schemas::market_data::MarketDataEvent;
use messages_public::schemas::refdata::InstrumentDefinition;
use messages_public::types::symbology::{Symbol, Venue};
use refdata::RefDataCache;
use service::MutService;
use std::sync::Arc;
use std::time::Duration;
use test_utils::ConsoleLogger;
use venues_internal::mktdata::funding_rate_instrument_filter;

const MAINNET: &str = "https://api.hyperliquid.xyz";

// rustls needs a process-level CryptoProvider before the first handshake; bootstrap does this
// in production, so the smoke tests do it once here.
fn install_crypto_provider() {
    static ONCE: std::sync::Once = std::sync::Once::new();
    ONCE.call_once(|| {
        let _ = rustls::crypto::ring::default_provider().install_default();
        ConsoleLogger::init();
    });
}

fn cache_with(symbols: &[(&str, &str)]) -> Arc<RefDataCache> {
    let cache = Arc::new(RefDataCache::new());
    for (symbol, venue_symbol) in symbols {
        cache.set_instrument(
            InstrumentDefinition::new()
                .symbol(Symbol::try_from(*symbol).unwrap())
                .venue_symbol(venue_symbol.to_string())
                .market_data_enabled(true),
        );
    }
    cache
}

#[runtime::test]
fn live_smoke_final_funding_rates_from_mainnet() {
    install_crypto_provider();
    let cache = cache_with(&[
        ("HYPL.PERP.ETH-USDC:USDC", "ETH"),
        ("HYPL.PERP.BTC-USDC:USDC", "BTC"),
    ]);
    let selected = funding_rate_instrument_filter(&cache, &Venue::Hyperliquid);
    println!(
        "live_smoke: filter selected {} instruments: {:?}",
        selected.len(),
        selected
            .iter()
            .map(|i| i.symbol.to_string())
            .collect::<Vec<_>>()
    );

    let mut poller = HyperliquidFundingRatePoller::new(
        NbioHttpClient::default(),
        Venue::Hyperliquid,
        MAINNET.to_string(),
        cache,
        Duration::ZERO,
    );

    let mut events = Vec::new();
    for _ in 0..600 {
        events.extend(poller.handle(()).expect("poller handle failed"));
        if events.len() >= 2 {
            break;
        }
        std::thread::sleep(Duration::from_millis(50));
    }

    println!("live_smoke: received {} MarkPrice events", events.len());
    assert!(!events.is_empty(), "no Final funding rates came back");

    for event in &events {
        let MarketDataEvent::MarkPrice(mp) = event else {
            panic!("expected MarkPrice, got {event:?}");
        };
        let entry = &mp.entries[0];
        println!(
            "  {} rate={:?} settled_at={:?} flag={:?}",
            mp.symbol, entry.rate, mp.ts, entry.settl_price_type
        );
        assert_eq!(entry.r#type, MdEntryType::FundingRate);
        assert_eq!(entry.settl_price_type, Some(SettlPriceType::Final));
        assert!(mp.ts.is_some(), "Final entry must carry a settlement ts");
        assert!(entry.rate.is_some());
    }
}

#[runtime::test]
fn live_smoke_watermark_suppresses_repeats_from_mainnet() {
    install_crypto_provider();
    let cache = cache_with(&[("HYPL.PERP.ETH-USDC:USDC", "ETH")]);
    let mut poller = HyperliquidFundingRatePoller::new(
        NbioHttpClient::default(),
        Venue::Hyperliquid,
        MAINNET.to_string(),
        cache,
        Duration::ZERO,
    );

    let mut seeded = Vec::new();
    for _ in 0..600 {
        seeded.extend(poller.handle(()).unwrap());
        if !seeded.is_empty() {
            break;
        }
        std::thread::sleep(Duration::from_millis(50));
    }
    assert_eq!(seeded.len(), 1, "seed must publish exactly one settlement");

    let mut repeats = Vec::new();
    for _ in 0..40 {
        repeats.extend(poller.handle(()).unwrap());
        std::thread::sleep(Duration::from_millis(50));
    }
    println!("live_smoke: {} events across 40 re-polls", repeats.len());
    assert!(
        repeats.is_empty(),
        "watermark must suppress already-published settlements, got {repeats:?}"
    );
}
