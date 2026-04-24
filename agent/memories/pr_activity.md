# PR Activity

## 2026-03-30 through 2026-04-04

### pulseprime/pulse — 47 PRs merged

**Erick Arce (17 PRs)**: Major coordinated push across pulse + polaris simultaneously. OpenSSL removal across multiple crates; heavy quoting/Talos/gateway rework. Biggest contributor this period.

**Talgat Taskhozhayev (8 PRs)**: Digital venue setup in Trade Engine, FIX server integration, audit trail config wiring. PR #1780 notable: wires `audit-trail` crate into `trade-engine` (3 handlers — `NewOrderSingle`, `ExecutionReport`, `OrderCancelReject`). Soft failure pattern (`log::warn`, no hot-path blocking). Architecture question flagged: latency concern on synchronous audit call in quote manager.

**Emre Ekici (7 PRs)**: Algo deployment infra.

**Estiven Salazar (7 PRs)**: Atlas UI entity management refactor, RFQ widgets, roles.

**Chris Davidson (4 PRs)**: Deadletter handling, settlement.

**Aksel Hakim (2 PRs)**: Talos TLS, managed algo IP config.

**Atakan Kupeli (1 PR)**: TLS disconnect handling.

### pulseprime/polaris — 16 PRs merged

**Erick Arce (12 PRs)**: RFQ/quoting push — coordinated with pulse PRs, concurrent cross-repo work.

**Ömer Yılmaz (2 PRs)**: OTC telemetry, BasisRecorder.

**Anton Ronis (1 PR)**: `VolatilityChange` → internal agg book pricing integration.

**Emre Ekici (1 PR)**: Quote adjustment fix.

---

## 2026-04-07 (Heartbeat — second run)

**pulseprime/pulse**: 0 new merged PRs since 2026-04-07.
**pulseprime/polaris**: 0 new merged PRs since 2026-04-07.

## 2026-04-05 through 2026-04-08

### pulseprime/pulse — 12 PRs merged

**Erick Arce (7 PRs)**: Heavy dependency cleanup and upgrade push across multiple sessions.
- #1769: "Updating hyperliquid for CVEs" (+2615/-2962, 7 files) — **notable**: large CVE fix in Hyperliquid integration
- #1782–1787: Dep cleanup chain — removes unneeded deps, consolidates base64, upgrades jsonwebtoken/jsonschema, deduplicates crates. Coordinated multi-PR sweep.

**Estiven Salazar (2 PRs)**: Atlas/algo-UI work — pre-populate form updates, polling fix.

**Atakan Kupeli (1 PR)**: #1779 "Ak.working dummypolaris" (+271/-4019, 12 files) — **notable**: 4k line deletion. Likely cleanup of dummy/test scaffolding from local Polaris dev environment work.

**Emre Ekici (1 PR)**: #1777 BTKB pagination fix.

**Eric Thill (1 PR)**: #1788 "macos make image fixes" (+25/-7, 6 files) — the macOS Docker build pipeline fixes from the Apr 7 session (Dockerfile layer ordering, pycares pin, polaris file renames).

### pulseprime/polaris — 6 PRs merged

**Erick Arce (5 PRs)**: Major architectural refactoring of the risk/portfolio module:
- #385: "Renaming KnownPositions to CentralRiskBook" (+319/-265, 8 files) — **notable**: core concept rename; `CentralRiskBook` is now the canonical name for the shared delta risk book
- #387: "Move around central risk book functions" (+210/-132, 2 files)
- #389: "Move tracker structs" (+40/-39, 9 files)
- #382–383: OTC chain + PositionSkew module restructuring

**Emre Ekici (1 PR)**: #381 "quote expiry validation" (+154/-27, 2 files) — adds validation logic for quote expiry.

**Theme**: Erick doing coordinated polish across both repos (dep hygiene in pulse, risk module rename/refactor in polaris). `KnownPositions` → `CentralRiskBook` rename is architecturally meaningful — the central risk book concept is now explicit in the codebase.

---

## 2026-04-08

### pulseprime/pulse — 6 PRs merged

**Ömer Yılmaz / litityum (4 PRs)**: Heavy Paribu exchange integration work.
- #1791: "Refactor skew parameters: replace `skew` with `delta_skew_params`" (+23/-21, 1 file) — config cleanup
- #1792: "Refactor Paribu WebSocket integration: switch to new API endpoints" (+277/-287, 6 files) — **notable**: large Paribu WS overhaul; this is a new exchange (Turkish crypto exchange Paribu) being integrated into Pulse
- #1794: "Update Paribu order schema: replace default values with nulls" (+7/-6, 2 files) — schema fix

**Matthew Gow / MatthewGow (1 PR)**: #1793 "use AWS public ECR images for python instead of docker.io who ratelimits" (+2/-2, 2 files) — infra fix, docker.io rate limiting workaround

**Aksel Hakim (1 PR)**: #1790 "try to solve sudden disconnect issue" (+22/-26, 1 file) — TLS/connectivity fix

**Talgat Taskhozhayev (1 PR)**: #1780 "Trade-Engine: Audit Trail" (+174/-131, 7 files) — **notable**: this PR finally merged today. Wires audit-trail into trade-engine with 3 handlers (NewOrderSingle, ExecutionReport, OrderCancelReject). Soft failure pattern (log::warn, no hot-path blocking).

### pulseprime/polaris — 3 PRs merged

**Eric Thill / ethill-pulse (1 PR)**: #388 "claude-ify repo and add local run scripts" (+688/-6, 17 files) — **notable**: the polaris CLAUDE.md documentation work + `polaris/local/` docker-compose stack from Apr 7 session. Large addition.

**Emre Ekici (1 PR)**: #390 "purge expired quotes" (+173/-11, 2 files) — quote lifecycle management improvement.

**Ömer Yılmaz / litityum (1 PR)**: #391 "Litityum/position skew refactor" (+160/-136, 7 files) — refactors position skew logic across 7 files.

**Theme**: Ömer active across both repos today (4 pulse + 1 polaris). Paribu exchange is new and significant — this is a Turkish crypto exchange not previously mentioned. Talgat's audit trail PR merged. Eric's polaris CLAUDE.md work landed.

---

## 2026-04-09

### pulseprime/pulse — 3 PRs merged

**Chris Davidson (1 PR)**: #1789 "Cd.remove talos refdata filters" (+1419/-86, 6 files) — **notable**: large change stripping Talos refdata filters from the integration path. Part of Talos↔Pulse connectivity cleanup.

**Emre Ekici (2 PRs)**:
- #1795 "Venue::Haruko" (+196/-0, 18 files) — **notable**: Haruko venue integration scaffold lands. Implements the dropcopy/mktdata REST poll loop Eric directed on Apr 8.
- #1796 "HRKO refdata fetcher" (+490/-8, 9 files) — **notable**: Haruko refdata fetch integration. Companion to #1795 — pulls instrument/refdata from Haruko REST API into Pulse's refdata system. 9 files, significant addition.

### pulseprime/polaris — 7 PRs merged (all Erick Arce)

**Erick Arce (7 PRs)**: Major coordinated skew system refactor — moves all skew calculations from `Envelope::Context` to a dedicated `skewtable` structure.

- #395: "Clear Ts Support" (+280/-4, 5 files) — previously noted
- #396: "Move liquidity skew" (+505/-896, 4 files) — **largest**: significant net deletion as liquidity skew moves into table
- #397: "Move basis adjustment skew in" (+160/-203, 3 files)
- #398: "Skew excess delta into table" (+147/-11, 1 file)
- #394: "SkewApplier use skewtable instead of Envelope::Context" (+272/-346, 4 files)
- #400: "MatchingEngine use skewtable instead of Envelope::Context" (+206/-176, 4 files)
- #401: "LadderQuotingEngine use skewtable instead of Envelope::Context" (+141/-132, 2 files)

**Theme**: Skew centralization — the `skewtable` is now the canonical place for all skew data across SkewApplier, MatchingEngine, and LadderQuotingEngine. Net change across the 6 skew PRs: ~+1431/-1764. Architecturally meaningful; Anton Ronis (Head of Quant) would care about this.

---

## 2026-04-10

### pulseprime/pulse — 4 PRs merged

**Eric Thill / ethill-pulse (1 PR)**: #1799 "bring flow-venues up to parity" (+345/-8, 5 files) — **notable**: flow-venues quoting implementation: QuotingSubscription handler, QuotingRequest handler, is_subscribed fix for QuotingEvent. Also reviewed MutDynService/RefCellLock migration for standalone single-threaded worker pattern.

**Talgat Taskhozhayev (2 PRs)**:
- #1797: "Trade-Engine: Risk Check messages and Cache initial setup" (+88/-0, 7 files) — **notable**: Phase 1 pre-trade risk check work begins. Adds risk check message types and a cache layer to trade-engine.
- #1800: "Trade-Engine: Talos configs" (+11/-0, 2 files) — small Talos config additions.

**Emre Ekici (1 PR)**: #1798 "HRKO position update" (+737/-7, 9 files) — **notable**: large addition to Haruko integration. Implements position tracking/update flow for HRKO.

### pulseprime/polaris — 2 PRs merged

**Ömer Yılmaz / litityum (2 PRs)**: Telemetry improvements.
- #399: "Litityum/positions telemetry otc" (+249/-229, 2 files) — adds OTC position data to telemetry; net-neutral change count suggests refactor of existing telemetry paths.
- #403: "Litityum/telemetry remove strategy update" (+547/-35, 3 files) — **notable**: removes strategy updates from telemetry; +547/-35 net add suggests new telemetry structure being added while old strategy-update paths are removed.

**Theme**: Pre-hackathon Haruko integration push (Emre) + Eric's flow-venues quoting parity + Talgat starting risk check scaffold. Ömer continuing post-skew-refactor telemetry cleanup in polaris.

---

## 2026-04-11 through 2026-04-13

### pulseprime/pulse — 4 PRs merged

**Emre Ekici (1 PR)**: #1804 "HRKO balance update" (+631/-7, 3 files) — **notable**: Haruko balance tracking. Companion to #1798 — together these two PRs bring position + balance sync into the Haruko integration (each ~600-700 line additions). Hackathon-ready Haruko data pipeline in pulse is largely built.

**Erick Arce (2 PRs)**: Continued dep hygiene.
- #1803: "Update versions and remove unneeded aws deps" (+398/-1392, 5 files) — **notable**: large net deletion; significant AWS dep cleanup.
- #1806: "Unify itertools version" (+21/-48, 8 files) — crate version unification.

**Ömer Yılmaz / litityum (1 PR)**: #1805 "Update min_notional for TRY to align with Paribu limits" (+2/-2, 1 file) — small Paribu config fix.

### pulseprime/polaris — 2 PRs merged

**Ömer Yılmaz / litityum (2 PRs)**:
- #405: "Litityum/liq skew zero bugfix" (+8/-17, 4 files) — liquidity skew zero-case bug fix.
- #406: "Update OTC account identifiers in positions.rs" (+3/-3, 1 file) — config correction.

**Theme**: Emre's Haruko pair (#1798 positions + #1804 balances) are the headline: the HRKO data pipeline is now substantially built in pulse ahead of hackathon. Erick wrapping up dep cleanup sprint. Ömer minor Paribu + polaris fixes.

---

## 2026-04-13

Very light day — hackathon in session, team focus is integration work not PRs.

### pulseprime/pulse — 2 PRs merged

**Matthew Gow (1 PR)**: #1808 "Update image repo" (+1/-1, 1 file) — infra config.

**Ömer Yılmaz / litityum (1 PR)**: #1807 "Remove unused `skew_bps` field from Polaris schema" (+0/-3, 1 file) — minor schema cleanup.

### pulseprime/polaris — 1 new PR merged

**Ömer Yılmaz / litityum (1 PR)**: #408 "Update Dockerfiles to use public ECR Ubuntu image" (+2/-2, 2 files) — mirrors pulse #1793 ECR fix from Apr 8.

*(#406 already captured in Apr 11-13 section above.)*

---

## 2026-04-14

Active day despite hackathon — significant new pulse infrastructure landed.

### pulseprime/pulse — 13 PRs merged

**Chris Davidson (3 PRs)**:
- **#1823 "Cd.trade updates to talos"** (+1037/-0, 17 files) — **SIGNIFICANT NEW APP**: `clearstreet-trade-updater` — Kafka consumer that syncs CS trade state changes back to Talos. Listens on `csc.bk.trades.v2.updated` topic; triggers `DELETE /v1/trades/{id}` (cancel) and `POST /v1/settlement` (settled) to Talos. Closes the CS→Talos feedback loop for P1.1 STP. Key detail: uses `client_trade_id` as Talos TradeID for both operations.
- #1827 "Skipping creates" (+14/-4, 1 file) — companion fix to #1823 (likely skips settlement creation events to avoid double-processing)
- #1820 "fixing case" (+3/-3, 1 file) — tiny case fix

**Eric Thill / ethill-pulse (2 PRs)**:
- **#1828 "make review role=..."** (+151/-0, 6 files) — AI review roles system: adds `repos/pulse/roles/` (rust-critic.md, trader-critic.md, architecture-critic.md) + `make review` target. Enables `make review role=rust-critic` to diff current branch vs main and run Opus review.
- #1822 "audit all data elements for talos topic" (+10/-14, 1 file) — small data audit/cleanup

**Talgat Taskhozhayev (2 PRs)**:
- **#1812 "Trade-Engine: Consumer Credit feed"** (+276/-2, 6 files) — **Phase 2 risk check work**: implements credit feed consumer in trade-engine. This is the "subscribe to credit data" side of the pre-trade risk check architecture.
- #1825 "Trade-Engine: Consumer Credit feed" (+32/-34, 2 files) — follow-up cleanup/fix to #1812

**Estiven Salazar (3 PRs)**: #1818 ag grid + algo UI bugfixes, #1824 quote_request_reject text field, #1826 NewRfqWidget fix

**Erick Arce (2 PRs)**: #1821 consolidate quoters with hedging counterparties (+7/-16), #1829 bad SDK fix for polaris OTC (+2/-2)

**Matthew Gow (1 PR)**:
- **#1831 "Test runners"** (+983/-296, 20 files) — **CI infrastructure upgrade**: migrates all GitHub Actions workflows from self-hosted EC2 builders to new GitHub-hosted runners (16 cores, 64GB). OIDC auth replaces static AWS access keys. Adds Rust toolchain install + sccache removed (was causing issues).

### pulseprime/polaris — 6 PRs merged

**Erick Arce (3 PRs)**: #410 collapse quoter configs (+849/-563, 21 files) — large config consolidation; #412 symbol() refactor (+11/-5, 4 files); **#404 "Client account support"** (+94/-30, 6 files) — adds client account support to polaris.

**Anton Ronis / ant0wn (1 PR)**:
- **#407 "Multi-member gzip support for flight recorder"** (+264/-33, 4 files) — Anton contributing directly to polaris infra; adds multi-member gzip to flight recorder. Improves replay capability for large multi-segment flight files.

**Emre Ekici (1 PR)**: #413 missing NOS reject fields (+7/-2, 1 file)

**Estiven Salazar (1 PR)**: #414 quote_request_reject optional text fields (+7/-7, 2 files)

**Theme**: Despite hackathon, substantial infrastructure landed. Chris's `clearstreet-trade-updater` (#1823) is the biggest new piece — closes the CS→Talos state sync loop. Talgat's credit feed consumer is Phase 2 of pre-trade risk checks. Matt's CI upgrade moves to GitHub-hosted runners. Eric's AI review roles system is live. Anton making direct polaris contributions.

---

## 2026-04-15 (Hackathon day 3)

### pulseprime/pulse — 2 new PRs merged (post Apr 14)

**Emre Ekici (2 PRs)** — **NOTABLE: New prediction market venue integration**:
- **#1833 "PredictionProduct"** (+211/-27, 19 files) — adds `PredictionProduct` type to Pulse. New product class for prediction markets.
- **#1835 "Venue::Kalshi"** (+175/-9, 16 files) — **NEW VENUE**: Kalshi integration scaffold. Kalshi is a US-regulated prediction market exchange (CFTC-regulated). This is not on any known roadmap — first prediction market venue in Pulse.

**Matthew Gow (1 PR)**: #1834 "test ci workflows" (+3/-1, 2 files) — CI test/fix.

### pulseprime/polaris — 0 new PRs since Apr 14

**Theme**: Hackathon day 3 is quiet on polaris. Emre's Kalshi work is the headline — adds `PredictionProduct` + `Venue::Kalshi` to pulse. This is Pulse's execution layer for a firm-wide CS Kalshi integration (requested by RenGen). CS has had Kalshi in flight since Jan 2026 across FACT/BASIS/Studio/CSC. Emre's PRs are the Pulse-side venue integration piece.

**Theme**: Despite hackathon, substantial infrastructure landed. Chris's `clearstreet-trade-updater` (#1823) is the biggest new piece — closes the CS→Talos state sync loop. Talgat's credit feed consumer is Phase 2 of pre-trade risk checks. Matt's CI upgrade moves to GitHub-hosted runners. Eric's AI review roles system is live. Anton making direct polaris contributions.

---

## 2026-04-15 through 2026-04-16

### pulseprime/pulse — 7 new PRs

**Emre Ekici (2 PRs)** — Kalshi integration continuing:
- **#1838 "KLSH refdata fetcher"** (+440/-8, 9 files) — Kalshi refdata fetch (mirrors HRKO refdata pattern). Companion to #1835 (Venue::Kalshi scaffold).
- **#1845 "KLSH websocket auth"** (+486/-10, 15 files, Apr 16) — Kalshi WebSocket authentication layer. Together with #1835/#1838, the full Kalshi venue integration trio lands this week.

**Estiven Salazar (1 PR)**:
- **#1836 "cloud-ui widgets dashboard"** (+690/-9273, 11 files) — **notable**: massive net deletion of 8500+ lines. Large cloud-UI widgets dashboard rewrite/cleanup.

**Erick Arce (2 PRs)**: #1839 TLS flag for tcp server (+36/-14) + #1841 improve TLS flag loading (+6/-4) — TLS hardening across standalone tcp server.

**Eric Thill (1 PR)**: #1837 "image building variable flexibility" (+4/-4, 4 files) — build pipeline config tweak.

**Matthew Gow (1 PR)**: #1842 fix bench dockerfile: install aws cli v2 for ubuntu 24.04 (+5/-1) — CI fix.

### pulseprime/polaris — 2 PRs

**Erick Arce (1 PR)**: #416 "Improve config unification otc+arb" (+188/-139, 6 files) — continues config consolidation work from #410.

**Eric Thill (1 PR)**: #422 "simple test of sequencer channel" (+267/-16, 2 files) — adds test coverage for the local sequenced channel. Likely validates the flow-venues quoting work from Apr 10.

**Theme**: Hackathon wrapping up — light PR week as expected. Emre completing the Kalshi integration trio (scaffold + refdata + auth). Estiven's large cloud-UI deletion suggests a dashboard refactor landing. Erick doing TLS hardening on tcp server across both repos.

---

## 2026-04-16 (end of hackathon — second batch)

### pulseprime/pulse — 7 PRs merged (excluding Kalshi already captured)

**Eric Thill (1 PR)**:
- **#1843 "local sequenced session flow migration"** (+732/-3812, 17 files) — **SIGNIFICANT**: migrates flow-venues to the local sequenced session pattern (FlowSessionManager / FlowSessionDispatcher / RefCellLock). Net -3080 lines — substantial old code deleted. This is the MutDynService migration Eric analyzed on Apr 10 and completes the standalone single-threaded worker refactor for flow-venues.

**Talgat Taskhozhayev (1 PR)**:
- **#1840 "Trade-Engine: Apply risk checks"** (+309/-39, 5 files) — Phase 3 (final) of pre-trade risk checks: actually applies the cached credit checks to incoming orders. Completes the three-PR arc: messages+cache (#1797) → credit feed consumer (#1812) → apply checks (#1840). Pre-trade risk checks are now live in the trade-engine.

**Estiven Salazar (2 PRs)**:
- **#1846 "positions widgets and shared state updates"** (+1549/-109, 33 files) — large positions UI overhaul, new shared state pattern.
- #1849 "positions widgets updates" (+184/-175, 10 files) — companion follow-up.

**Chris Davidson (1 PR)**: #1832 "fixing the wrapper logic" (+61/-28) — fix to `clearstreet-trade-updater` wrapper logic (follow-on to #1823).

**Matthew Gow (1 PR)**: #1848 "mirror sync retry" (+2/-1) — mirror sync transient retry with 3 attempts + 15s delay.

**Erick Arce (1 PR)**: #1847 "Update polaris config" (+7/-1) — minor polaris config update pushed via pulse.

### pulseprime/polaris — 2 PRs

**Erick Arce (2 PRs)**:
- #424 "Support dropcopy and rfq account for quoting side" (+33/-13, 4 files) — adds dropcopy + RFQ account support on the quoting side.
- #425 "Log more info about unsupported" (+3/-4, 1 file) — logging improvement for unsupported message handling.

**Theme**: Hackathon final day. Eric's flow-venues migration (#1843) is the architectural headline — -3080 lines of old session management code replaced with the RefCellLock/standalone pattern. Talgat's #1840 completes the pre-trade risk check trilogy — **risk checks are now live end-to-end**. Estiven shipping major positions UI work. Chris fixing the trade-updater wrapper.

---

## 2026-04-16 (third batch — late-day merges)

### pulseprime/pulse — 6 more PRs

**Aksel Hakim (1 PR)**:
- **#1844 "small batch of changes for replay functionality"** (+509/-0, 5 files) — **notable**: new replay capability additions. Pure addition (no deletions). Likely ties to Aksel's assignment on Deribit options / publisher crate work.

**Chris Davidson (1 PR)**:
- #1850 "switching model for stream recovery" (+24/-2, 3 files) — stream recovery model switch in `clearstreet-trade-updater` or related app. Follow-on to #1823/#1832.

**Talgat Taskhozhayev (1 PR)**:
- #1851 "Trade-Engine: Applying Risk Checks" (+1/-0, 1 file) — trivial follow-up to #1840; single-line fix applying risk checks.

**Estiven Salazar (3 PRs)**:
- **#1852 "open orders widget"** (+1073/-200, 16 files) — large new open orders widget for the UI.
- **#1854 "widget clean up"** (+0/-864, 25 files) — **notable**: net -864 lines across 25 files. Major cleanup/consolidation of widget code post-overhaul.

### pulseprime/polaris — 1 PR

**Erick Arce (1 PR)**:
- #426 "Fix feed deps" (+11/-57, 4 files) — dependency cleanup for feeds; net deletion.

**Theme**: End-of-day hackathon trickle. Aksel's replay work (+509) is the most substantive new addition. Estiven continuing UI consolidation — the open orders widget + cleanup pair rounds out the positions/orders UI overhaul that started mid-week. Chris's stream recovery switch closes out `clearstreet-trade-updater` stabilization.

---

## 2026-04-17 (hackathon last day — post-merge)

### pulseprime/pulse — 2 PRs

**Estiven Salazar (1 PR)**:
- **#1859 "balances widgets"** (+1012/-1, 18 files) — large new balances widget. Completes the trinity of positions (#1846) + open orders (#1852) + balances (#1859) — Atlas UI now has a full account state dashboard.

**Emre Ekici (1 PR)**:
- **#1864 "KLSH mktdata bbo"** (+227/-10, 5 files) — Kalshi BBO (best bid/offer) market data feed. Companion to the KLSH auth (#1845) and refdata (#1838) from yesterday. Kalshi venue integration is now substantially complete: scaffold + refdata + auth + mktdata BBO.

**Also captured from Apr 16 late-day (already in third batch above)**: #1858 NewRfqWidget updates (Estiven, +166/-90), #1853 KLSH mktdata trade (Emre, +983/-42), #1857 Talos optional CumQty (Emre, +1/-2), #1856 positions summary widget (Estiven, +857/-4).

### pulseprime/polaris — 0 new PRs (hackathon ends)

**Theme**: Hackathon closes out with Estiven's balances widget completing the new Atlas UI dashboard trio. Emre's Kalshi BBO mktdata rounds out the full venue integration. The hackathon week (Apr 13-17) was one of the most productive in recent memory: ~50 pulse PRs + ~15 polaris PRs. Major deliverables: pre-trade risk checks E2E (Talgat), Haruko position+balance pipeline (Emre), clearstreet-trade-updater (Chris), flow-venues session migration (Eric -3080 lines), Kalshi venue full stack (Emre), full Atlas UI overhaul (Estiven).

**Notable**: No PRs from Erick Arce today — polaris refactor and config consolidation sprint appears complete for now.

---

## 2026-04-17 (hackathon final day — full tally)

### pulseprime/pulse — 21 PRs merged (all Apr 17)

**Estiven Salazar (6 PRs)** — Atlas UI final push:
- **#1861 "blotter widgets"** (+3568/-1, 54 files) — massive blotter widget addition
- **#1862 "overview widget"** (+771/-1, 12 files)
- **#1870 "orderbook widget"** (+1080/-1, 12 files)
- **#1877 "rfq widgets"** (+1267/-0, 17 files)
- **#1878 "algo management widget"** (+4966/-0, 48 files) — **largest single PR of hackathon week**
- **#1879 "alert manager widget"** (+2815/-0, 31 files)

**Emre Ekici (5 PRs)** — Kalshi integration final + position/balance:
- #1867 KLSH mktdata book (captured previously)
- #1868 remove KLSH prod (captured previously)
- #1869 prediction symbol parsing (captured previously)
- **#1872 "KLSH balance update"** (+654/-26, 10 files) — Kalshi balance tracking
- **#1874 "ExecutionReport::prediction_side"** (+23/-0, 4 files) — adds prediction market side to execution reports
- **#1880 "KLSH trade event"** (+592/-14, 7 files) — Kalshi trade event handling
- **#1881 "KLSH position update"** (+197/-10, 4 files) — Kalshi positions

**Erick Arce (3 PRs)** — Talos fixes:
- #1871 fix talos parsing issues (+120/-15, 3 files)
- #1875 fixing talos venue (+46/-33, 3 files)
- #1876 fixing logs talos (+1/-6, 1 file)

**Chris Davidson (1 PR)**: #1873 fix trade time calc (+149/-15, 1 file)

**Previously captured**: #1855, #1859, #1864, #1866, #1867, #1868, #1869

### pulseprime/polaris — 1 PR
**Erick Arce**: #428 missing state type for orders (+15/-0, 1 file)

**Hackathon week (Apr 13-17) FINAL TALLY**: ~55 pulse PRs, ~15 polaris PRs.
Headline deliverables: pre-trade risk checks E2E live (Talgat), Haruko position+balance+trade pipeline (Emre), clearstreet-trade-updater (Chris), flow-venues -3080 line session migration (Eric), Kalshi full venue stack incl positions/balances/trades (Emre), Atlas UI total overhaul — blotter/overview/orderbook/rfq/algo-mgmt/alert-mgmt/orders/positions/balances (Estiven).

---

## 2026-04-20 through 2026-04-21

Post-hackathon momentum picks up — Kalshi reactivated (briefly), Erick back on polaris reconciliation.

### pulseprime/pulse — 11 PRs merged

**Emre Ekici (4 PRs)** — Kalshi partially restored then re-killed:
- **#1893 "KLSH new order single"** (+930/-5, 10 files, Apr 20) — major addition: Kalshi order entry (NOS). Kalshi fully decommissioned from prod/dev last week but NOS logic being added back — likely preparing for eventual production use.
- #1894 "KLSH trade timestamp fix" (+6/-4, Apr 20) — minor fix
- **#1897 "KLSH mass status"** (+601/-100, 3 files, Apr 21) — Kalshi mass order status handling. Kalshi integration continuing to mature despite env removal.
- #1887 "remove KLSH from dev" (already captured)

**Estiven Salazar (4 PRs)** — Atlas UI final widgets:
- **#1892 "account tier mgmt widget"** (+720/-11, 17 files, Apr 20)
- **#1890 "markup tier management widget"** (+675/-7, 12 files, Apr 20)
- **#1889 "static price overrides widget"** (+1421/-0, 13 files, Apr 20)
- #1886 "manual adjustments widget" (already captured, Apr 20)

**Chris Davidson (1 PR)**:
- **#1888 "Settle balances on Talos"** (+540/-6, 8 files, Apr 20) — adds balance settlement sync back to Talos. Companion to the earlier `clearstreet-trade-updater` (#1823) — closes another loop in the CS→Talos state feedback chain.

**Aksel Hakim (1 PR)**:
- **#1895 "transport/socket changes for fix replay"** (+195/-41, 4 files, Apr 21) — transport/socket changes for FIX replay. Likely related to Aksel's replay functionality work from hackathon (#1844).

**Talgat Taskhozhayev (1 PR)**: #1896 minor logging change (Apr 21).

### pulseprime/polaris — 3 PRs merged

**Erick Arce (3 PRs)**:
- **#402 "Reconciliation Logic first pass"** (+1992/-16, 18 files, Apr 20) — **SIGNIFICANT**: first pass of reconciliation logic in polaris. +1992 lines, 18 files. Polaris getting position reconciliation capability — ties to the broader recon discussion in the Apr 20 DA Status meeting.
- #438 "Fix account subscription" (+56/-22, 4 files, Apr 21)
- #439 "Fix inserts for defaults" (+15/-22, 2 files, Apr 21)

**Theme**: Erick's reconciliation PR (#402) is the architectural headline — aligns directly with the Apr 20 DA Status meeting discussion about Talos↔BK position reconciliation. Emre building out Kalshi NOS + mass status despite env removal (preparing for future prod). Chris closing another Talos feedback loop. Estiven completing the Atlas UI widget set.

---

## 2026-04-18 through 2026-04-20

Very light post-hackathon window — weekend + early week catch-up.

### pulseprime/pulse — 5 PRs merged

**Estiven Salazar (3 PRs)** — Atlas UI completion:
- **#1885 "role management widget"** (+1221/-1, 16 files, Apr 18) — role management UI
- **#1884 "entity management widget"** (+2101/-0, 16 files, Apr 18) — entity management UI
- **#1883 "strategy management widget"** (+490/-0, 11 files, Apr 18) — strategy management UI
- **#1886 "manual adjustments widget"** (+811/-0, 13 files, Apr 20) — manual adjustments UI

Estiven continues Atlas UI overhaul post-hackathon. All additions (no deletions) — new widgets being layered in.

**Emre Ekici (1 PR)**:
- **#1887 "remove KLSH from dev"** (+1/-16, 2 files, Apr 20) — removes Kalshi from dev environment entirely. Kalshi was already removed from prod (#1868). Now fully off in all non-prod environments too.

### pulseprime/polaris — 1 PR merged

**Ömer Yılmaz / litityum (1 PR)**:
- **#434 "Introduce separate trading stats support with registries and routing"** (+235/-58, 4 files, Apr 19) — adds dedicated trading stats registry and routing layer. Ömer continuing polaris observability/telemetry work.

**Theme**: Weekend + early-week cleanup. Estiven rounding out Atlas widget set. Kalshi fully decommissioned from all environments (prod Apr 17, dev Apr 20). No contributions from Talgat, Erick, Chris, or Eric yet this week — all hands-on meetings.

---

## 2026-04-17 (hackathon close-out — late merges)

### pulseprime/pulse — 5 additional PRs

**Emre Ekici (3 PRs)** — Kalshi integration final pieces:
- **#1867 "KLSH mktdata book"** (+564/-12, 4 files) — Kalshi full order book market data. Completes the Kalshi mktdata stack: BBO (#1864) + book (#1867).
- **#1868 "remove KLSH prod"** (+2/-17, 2 files) — removes Kalshi prod config (likely keeping it dev/staging-only for now, not yet live in prod).
- **#1869 "prediction symbol parsing sdk"** (+1/-1, 1 file) — tiny fix to prediction market symbol parsing in SDK.

**Chris Davidson (1 PR)**:
- **#1855 "Add error for modifies"** (+309/-8, 3 files) — adds error handling for trade modify messages in the `clearstreet-trade-updater` or related BK integration.

**Matthew Gow (1 PR)**:
- **#1866 "add apt-get retry logic to all Dockerfiles"** (+10/-5, 5 files) — infra reliability fix across Dockerfiles.

### pulseprime/polaris — 0 new PRs

**Theme**: Hackathon final day closes cleanly. Emre ships Kalshi order book data (#1867) — Kalshi venue integration is now feature-complete (scaffold + refdata + auth + mktdata BBO + full book). `remove KLSH prod` suggests it stays off production for now. Chris adds error handling for modifies in the trade-updater flow. No architectural changes — this is polish and stabilization.

**Hackathon week (Apr 13-17) final tally**: ~55 pulse PRs, ~15 polaris PRs. Headline deliverables: pre-trade risk checks E2E live (Talgat), Haruko position+balance pipeline (Emre), clearstreet-trade-updater (Chris), flow-venues -3080 line session migration (Eric), Kalshi full venue stack (Emre), Atlas UI positions/orders/balances overhaul (Estiven).

---

## 2026-04-21 through 2026-04-22

Post-hackathon momentum continues. Heavy Kalshi build-out, Atlas UI polish, Talos/polaris reconciliation work.

### pulseprime/pulse — 24 PRs merged (Apr 21–22)

**Emre Ekici (6 PRs)** — Kalshi order management completing:
- **#1897 "KLSH mass status"** (+601/-100, 3 files, Apr 21) — Kalshi mass order status
- **#1898 "KLSH order status"** (+228/-3, 1 file, Apr 21) — individual order status
- **#1902 "KLSH cancel order"** (+273/-17, 3 files, Apr 21) — cancel order support
- **#1906 "KLSH cancel replace"** (+461/-12, 4 files, Apr 21) — cancel-replace (modify) support
- **#1922 "KLSH position recovery"** (+641/-29, 3 files, Apr 21) — position recovery on reconnect
- **#1932 "KLSH fees"** (+68/-13, 4 files, Apr 22) — fee handling
- **Theme**: Kalshi order management lifecycle is now complete (mass status + individual status + cancel + cancel-replace + position recovery). Despite being removed from prod/dev envs, the integration is maturing rapidly.

**Estiven Salazar (8 PRs)** — Atlas UI finalization:
- #1899 "pulse-ui api-client" (+1358/-1, 23 files) — new API client layer
- #1900 "wiring atlas and cloud-ui with widget-api client" (+69/-20)
- #1903 "migrating self contained api widgets" (+487/-1016, 40 files) — net deletion, cleanup
- #1905 "NewRfqWidget spread and valid_until timer" (+156/-45)
- #1907 "migration of useWidgetQuery to api-client" (+152/-130, 21 files)
- #1926 "new-rfq-widget updates" (+117/-55)
- #1927 "filtering atlas rfq sessions" (+9/-1)
- #1928 "format markup tiers floats" (+1/-1)
- #1929 "new rfq widget approx notional" (+15/-0, Apr 22)
- #1934 "new rfq widget fetch instruments" (+30/-11, Apr 22)
- **Theme**: API client abstraction layer landing across all widgets; RFQ widget receiving heavy polish.

**Erick Arce (2 PRs)**:
- **#1901 "Stamp secondary ids for Talos"** (+49/-11, 7 files, Apr 21) — **notable**: stamps secondary IDs (trade/order IDs) into Talos messages. Directly enables trade-by-trade P&L correlation (see PnL Dashboard Notion meeting, Apr 21). Links client trades with hedges via shared identifiers.
- **#1930 "Configurable recovery time"** (+413/-76, 46 files, Apr 21) — large refactor making connection recovery time configurable across 46 files.

**Chris Davidson (1 PR)**:
- **#1904 "talos contractual settlement"** (+314/-51, 3 files, Apr 21) — adds contractual settlement handling to Talos integration. Companion to the Apr 13 settlement models decision.

**Talgat Taskhozhayev (2 PRs)**:
- #1896 minor logging (Apr 21)
- **#1931 "Trade-Engine: Persist Markups as basis points"** (+54/-35, 7 files, Apr 22) — persists markup pricing data in basis points in trade-engine.

**Matthew Gow (2 PRs)**: #1891, #1914 — self-hosted EKS runner testing (CI infrastructure).
**Aksel Hakim (1 PR)**: #1895 transport/socket changes for FIX replay (Apr 21).

### pulseprime/polaris — 5 PRs (Apr 21)

**Erick Arce (4 PRs)**:
- #438 "Fix account subscription" (+56/-22) — already captured
- #439 "Fix inserts for defaults" (+15/-22) — already captured
- **#442 "Update fill lookup"** (+46/-6, 4 files) — fill tracking improvement in reconciliation logic
- **#443 "Fix exec id lookup"** (+1/-1) — exec ID lookup fix in recon

**Anton Ronis (1 PR)**:
- **#441 "Initialize client account positions for delta skew"** (+218/-5, 3 files) — **notable**: Anton adding client account positions as inputs to delta skew calculation. Polaris now initializes per-account position state for skew management.

**Theme**: Erick's reconciliation PR (#402) from Apr 20 is being actively followed up — #442/#443 are reconciliation fixes suggesting the recon logic is being actively tested and iterated. Anton's #441 is architecturally significant: client account positions now feed into delta skew in polaris. Emre completing Kalshi full order lifecycle despite env decommission. Erick's secondary ID stamping (#1901) enables P&L trade linkage.

**New notable item**: The Apr 21 PnL Dashboard meeting confirmed **Robert (Bob) is driving implementation of trade-by-trade P&L** — a transactional ID to link client trades with hedges in Pulse, then group downstream in Snowflake. Erick's #1901 (stamp secondary IDs for Talos) is almost certainly the Pulse-side response. Robert's action item: "talk to Pulse team about adding transaction identifiers to link client trades with hedges."

---

## 2026-04-24 Heartbeat (PRs since Apr 23)

### pulseprime/pulse — 8 PRs merged (all Apr 23)

**Chris Davidson (3 PRs)**:
- **#1953 "move over dependencies"** (+1798/-1787, 39 files) — large dependency migration across 39 files; net-neutral = crate consolidation, not new code.
- #1956 "swap cancel endpoint" (+4/-4, 1 file) — small fix to swap cancel endpoint.
- #1951 "cleanup admin vscode warnings" (+18/-2, 2 files) — minor cleanup.

**Talgat Taskhozhayev (1 PR)**:
- **#1955 "ClearStreet Account Manager: initial setup"** (+116/-0, 9 files) — already captured in Apr 23 section; new account management service scaffold.

**Estiven Salazar (4 PRs)**: #1957 sidebar/strat styling (+423/-181), #1952 atlas/cloud-ui base URL updates (+48/-42), #1950 alert manager mantine ref (+398/-849 = net deletion = cleanup), #1949 algo table mantine ref (+326/-521 = net deletion). All Atlas UI mantine migration work; significant line deletions indicate cleanup of old widget patterns.

### pulseprime/polaris — 2 PRs merged (both Apr 23, Matthew Gow)
- #452 "Upgrade base image to Ubuntu 24.04 for glibc 2.38+ compat" (+1/-1) — infra upgrade.
- #450 "Fix runner" (+36/-14) — ARC runner fix completing polaris CI migration.

### Summary
Quiet day. No new architectural work. Chris stabilizing dependency structure. Estiven continuing mantine migration (cleanup = good). Matt closing out polaris CI runner upgrade. `ClearStreet Account Manager` from Apr 23 is the last meaningful new signal from this window.

---

## 2026-04-23

### pulseprime/pulse — 6 PRs merged

**Talgat Taskhozhayev (1 PR)**:
- **#1955 "ClearStreet Account Manager: initial setup"** (+116/-0, 9 files) — **NEW SERVICE**: initial scaffold for a ClearStreet Account Manager service. Pure addition — this is a new service being stood up by Talgat, likely related to account management prereqs for the Talos migration (Eric's step 1 requires account management in our services before Talos write path can flip).

**Chris Davidson (2 PRs)**:
- **#1953 "move over dependencies"** (+1798/-1787, 39 files) — large dependency migration across 39 files; net-neutral size suggests rearranging / consolidating deps across crates.
- **#1956 "swap cancel endpoint"** (+4/-4, 1 file) — small fix to the swap cancel endpoint.

**Estiven Salazar (3 PRs)**: #1950 alert manager mantine ref (+398/-849, 12 files), #1949 algo table mantine ref (+326/-521, 17 files), #1957 sidebar/strat mgmt styling (+423/-181) — Atlas UI continuing mantine component library migration; net deletion across each = cleanup of deprecated widget patterns.

### pulseprime/polaris — 2 PRs merged

**Matthew Gow (2 PRs)**:
- **#452 "Upgrade base image to Ubuntu 24.04 for glibc 2.38+ compat"** (+1/-1, 1 file) — infra upgrade for glibc compatibility.
- **#450 "Fix runner"** (+36/-14, 1 file) — ARC runner fix from yesterday's CI switch.

**Theme**: Talgat's new `ClearStreet Account Manager` service is the headline — a pure-addition new service that's likely the first step toward account management living in CS services rather than Talos. Estiven's mantine migration continues (net deletions across widget refactors). Matt finishing the ARC runner rollout in polaris.

---

## 2026-04-22 (end of day)

Post-heartbeat PRs — same-day merges after the Apr 22 morning heartbeat run.

### pulseprime/pulse — 10 PRs merged

**Erick Arce (2 PRs)**:
- **#1938 "Talos instrument control filter"** (+54/-64, 6 files) — filters/controls which instruments are active in Talos integration. Small net deletion suggesting a simplification.
- **#1941 "Fix polling backoff"** (+2/-0, 1 file) — minor polling backoff fix.

**Chris Davidson (1 PR)**:
- **#1830 "new custom instrument admin tab"** (+1496/-1030, 27 files) — **notable**: large new admin UI tab for custom instrument management. Net +466 across 27 files — substantial new admin capability, likely for options instrument setup. This is the Talos instrument admin UI Eric's team needs for options configuration.

**Estiven Salazar (3 PRs)**:
- #1939 "markup tier widget updates" (+115/-94) — minor polish.
- #1934 "new rfq widget fetch instruments" (+30/-11) — already captured.
- #1929 "new rfq widget approx notional" (+15/-0) — already captured.

**Aksel Hakim (1 PR)**:
- **#1863 "Ah.fix replay request"** (+934/-39, 7 files) — **notable**: large addition to FIX replay request handling. Continuing Aksel's replay infrastructure work from hackathon.

**Emre Ekici (2 PRs)**:
- #1936 "KLSH expired position fix" (+10/-1) — Kalshi expired position handling fix.
- #1932 "KLSH fees" (+68/-13) — already captured.

**Talgat Taskhozhayev (1 PR)**: #1931 "Persist Markups as basis points" — already captured.

### pulseprime/polaris — 6 PRs merged

**Anton Ronis (1 PR)**:
- **#429 "Pre-trade risk gate: inventory limits + available funds checks"** (+2057/-4, 11 files) — **SIGNIFICANT**: massive pre-trade risk gate addition in polaris. Adds inventory limit checks and available funds checks. +2057 lines across 11 files — this is Anton shipping a substantial risk management layer directly into polaris. Directly relevant to the Apr 22 calendar item "DSDigital: Confirm buying power/pre-trade limit architecture" (Mon Apr 27).

**Ömer Yılmaz / litityum (3 PRs)**:
- **#449 "positions strategy metrics"** (+428/-19, 1 file) — large addition of per-strategy position metrics.
- #446 "Refactor VolumeRecorder to include per-strategy volume tracking" (+143/-10) — volume tracking per strategy.
- #444 "Add support for tracking primary hedging counterparty" (+123/-2) — tracks primary hedging counterparty. Connects to P&L trade linkage work.

**Matthew Gow (2 PRs)**:
- #445 "switch CI to ARC self-hosted runners" (+256/-101, 8 files) — **notable**: CI infrastructure switch to ARC (Actions Runner Controller) self-hosted runners. Mirrors the pulse CI upgrades from hackathon.
- #447 "Fix rust cache" (+256/-101, 8 files) — companion fix to #445.

**Theme**: Anton's pre-trade risk gate (#429, +2057 lines) is the architectural headline — polaris now has inventory limits and available funds checks before order routing. Directly tied to the pre-trade buying power architecture discussion on Mon Apr 27. Ömer adding dense telemetry (per-strategy metrics, volume, hedging counterparty tracking). Matt upgrading polaris CI to match pulse. Chris's custom instrument admin tab in pulse is a major ops capability for options setup.
