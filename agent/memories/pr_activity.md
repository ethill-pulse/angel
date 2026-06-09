# PR Activity

## 2026-06-05 through 2026-06-09 (updated June 9 heartbeat)

### pulseprime/pulse — ~40 PRs

**Estiven Salazar — UI RBAC / ACL push (dominant theme)**:
- **#2343 [Jun 8] (+557/-63, 30 files) — "UI RBAC library"** — new front-end role-based access control library. Foundation for the ACL series below.
- ACL-check sweep across the API surface (Jun 8–9): trading ops websockets (#2378), rfq/esp websockets (#2376), CLST account + markup tiering endpoints (#2371), CustomerConfiguration (#2367), HarukoLoans/HarukoVenueAccounts (#2364), book-trade (#2363), MarketAccounts (#2361), HouseAccounts (#2360), ClstAccounts (#2359). Coordinated authorization hardening across Halo/api-gateway.
- Halo polish: compress order forms (#2375 +277), connection/quoting routing (#2372), env distinction, party roles, sign-out, widget fixes.

**Erick Arce — Trade-Engine account-model restructure**:
- **#2340 [Jun 6] (+1225/-276, 35 files) — "TE structural changes to support account_id/clst_account rules"** — **SIGNIFICANT**: trade engine reworked to carry account_id / clst_account through rules. Largest pulse PR of the week. Underpins per-account ACL + markup tiering.
- **#2346 [Jun 7] (+504/-220) — "Esp order support in TE"** — Executable Streaming Price order path in trade engine. #2349 markup/raw price bugfix follows.
- #2369 mktdata api support, #2335 standalone perf fix, #2308 acceptor backpressure fix.

**Emre Ekici — Wintermute (WMUT) order-entry stack** (mktdata landed last week; now order entry):
- **#2344 [Jun 8] (+761/-8, 9 files) — "WMUT new order"**, **#2327 [Jun 5] (+796/-6, 14 files) — "WMUT trade & order event"**, #2353 balance update (+391), #2355 order update fix, #2352 MockFixOrderSession. Wintermute now has a full order-entry FIX path, not just market data.

**Aksel Hakim**:
- **#2280 [Jun 5] (+1336/-40, 22 files) — "gap fill kafka"** — **SIGNIFICANT**: gap-fill recovery wired through Kafka. The gap-fill work Atakan+Aksel have been wrapping up before pivoting to Paradigm. Pagination piece (#2266) landed prior week.

**Amit Kirdatt**:
- **#2318 [Jun 5] (+748/-0, 8 files) — "Persist GTC order type"** — GTC order persistence (follows the May 28 GTC/NOS→Polaris decision).
- DIG-92: calculate trigger price + markup bps (#2337 +171), test for missing-markup trigger price (#2358), get orders by status (#2354).

**Eric Thill (ethill) — shipped 5 PRs himself**:
- **#2362 [Jun 8] (+355/-7, 12 files) — "admin stats page: perf tab"** — perf tab on the admin stats page.
- #2365 missing backoff services, #2329 fact tombstone record handling, #2320 bootstrap per-app override, #2338 fix decimal parsing lossy-ness.

**Matt Gow**:
- **#2374 [Jun 9] — "add alfred skills: version-bump, venue-config, service-config-tweak"** — Matt building out "alfred" AI/automation skills for repo operations. Continued internal AI-tooling investment from the team.

**Talgat Nurakhmetov**: #2315 Trade-Engine Resting Order scaffolding, #2289 Decimal version upgrade (8 files).

**Chris Davidson**: #2330 worktree cd.user name swap (+450), #2342 remove checks (−160), plus options timing/sync-trades carryover.

**Ömer Yılmaz (litityum)**: #2310 OKX_TR (OKX Turkey) venue.

### pulseprime/polaris — ~16 PRs

**Anton Ronis (ant0wn) — quant/risk**:
- **#704 [Jun 9] (+959/-36, 19 files) — "feat(risk): add momentum-aware quote skew"** — **SIGNIFICANT**: new risk feature, quote skew responds to momentum. Largest polaris PR of the week.
- **#693 [Jun 4] (+475/-49, 9 files) — "gate OTC client quotes and trades on position readiness"** — don't quote/trade OTC until position state is ready. (Mirrors the June 9 Swap/Deriv "position readiness" gating theme.)
- **#718 [Jun 9] (+498/-102) — basis-estimator out-of-order timestamp fix + feed-health telemetry**.

**Ömer Yılmaz (litityum)**:
- #722 account-aware cancel-replace suppression (BinancePM), #720 derive venue from account (not symbol), #717 order throttle info w/ symbol+account (+310), #712 remove order_map from RateLimiter, #709 codegen QuotingFeedType schema fix.

**Erick Arce**:
- **#708 [Jun 6] (+568/-229, 14 files) — "Fix rfq and esp support for double feeds"** — ESP/RFQ double-feed handling. #710 esp support, #713 move tests for gate integration, #721 stamp build info, #685 rename ladder engine.

**Theme**: Cross-repo RBAC/ACL + account-model push (Estiven UI RBAC + Erick TE account rules + Ömer venue-from-account); Wintermute order entry; Anton momentum skew + OTC position-readiness gating; Aksel gap-fill-via-Kafka.

## 2026-06-03 through 2026-06-04 (updated June 4 heartbeat)

### pulseprime/pulse — 14 new PRs

**Emre Ekici (4 PRs) — Wintermute full mktdata stack**:
- **#2307 [Jun 4] (+1069/-6, 14 files) — "WMUT mktdata book"** — **SIGNIFICANT**: Full WebSocket order book integration for Wintermute LP. 14 files, +1063 net. Wintermute was added as a venue in May; now getting production market data.
- **#2311 [Jun 4] (+138/-31, 3 files) — "WMUT mktdata bbo"** — BBO (best bid/offer) market data for Wintermute.
- **#2312 [Jun 4] (+74/-1, 5 files) — "quote ws endpoint"** — quote WebSocket endpoint for trading ops.
- **#2313 [Jun 4] (+39/-219, 3 files) — "WMUT book → quote fix"** — net deletion fix for book→quote conversion.

**Ömer Yılmaz (litityum) (1 PR)**:
- **#2310 [Jun 4] (+99/-11, 11 files) — "Add OKX_TR venue (OKX Turkey)"** — adds OKX Turkey as a new execution venue in pulse. 11 files.

**Estiven Salazar (4 PRs)**:
- **#2278 [Jun 3] (+1339/-72, 28 files) — "market widget & UI ESP Support"** — **LARGE**: new market data widget with Executable Streaming Price (ESP) support. 28 files, +1267 net. This is the Halo UI layer for the Paradigm streaming RFQ options path — ESP = real-time executable streaming prices from LPs.
- **#2299 [Jun 3] (+40/-5, 3 files) — "trades-widget market accounts update"** — trades widget update.
- **#2298 [Jun 3] (+1/-1) — "algo-management page one second polling"** — minor polling interval fix.
- **#2302 [Jun 4] (+33/-23, 1 file) — "api-gateway close ws proxy bugfix"** — WebSocket proxy close fix.

**Erick Arce (4 PRs)**:
- **#2306 [Jun 4] (+18/-7, 1 file) — "Fix logon timeout"** — FIX session logon timeout fix.
- **#2314 [Jun 4] (+6/-5, 3 files) — "Start acceptor as a worker"** — FIX acceptor refactor.
- **#2309 [Jun 4] (+38/-14, 7 files) — "Improve ability to name consumers"** — consumer naming improvements.
- **#2304 [Jun 3] (+13/-9, 3 files) — "More fix logging"** — logging improvements.

**Chris Davidson (1 PR)**:
- **#2303 [Jun 3] (+27/-26, 1 file) — "reorder only"** — minor reorder.

### pulseprime/polaris — 16 new PRs

**Ömer Yılmaz (litityum) — flight-deck production hardening (12 PRs)**:
- **#699 [Jun 4] (+240/-7, 2 files) — "dispatch RPC schemas by operating mode"** — **SIGNIFICANT**: RPC handler now dispatches different schemas depending on flight-deck operating mode (ARB/OTC/STAGED). Enables mode-aware API.
- **#695 [Jun 4] (+17/-27, 6 files) — "upgrade schemars 0.8 → 1.2.1"** — JSON Schema draft 2020-12 support.
- **#701, #700 [Jun 4]** — Symbol and Decimal JSON schema fixes for Python/Pydantic compatibility.
- **#697, #698 [Jun 4]** — Flight-deck ARB heartbeat fix + strip `$schema` from RPC schemas.
- **#692, #691, #690, #689, #686 [Jun 3]** — gzip+base64 RPC response wrapping, Pulse standalone endpoint path fixes, WebSocket decode fix, auth transform fix for OTC/STAGED, typed exchange IDs for 1Password credential lookup.

**Anton Ronis (2 PRs) — quant risk correctness**:
- **#687 [Jun 3] (+158/-64, 1 file) — "annualize volatility by sampling interval, not EWMA horizon"** — **CORRECTNESS FIX**: Volatility was being annualized using the EWMA horizon rather than the actual sampling interval. Significant quant error fix.
- **#688 [Jun 3] (+147/-5, 1 file) — "preserve basis_adjustment across OTC dual SkewTracker"** — basis adjustment was being lost when an OTC strategy used the dual skew tracker. Prevents stale basis from accumulating.

**Erick Arce (2 PRs)**:
- **#685 [Jun 3] (+30/-28, 6 files) — "Rename ladder engine"** — cleanup rename.
- **#618 [Jun 2] (+941/-19, 9 files) — "ExecutablePriceStreamer"** — **SIGNIFICANT**: polaris-side ExecutablePriceStreamer implementation (+922 net). This is the polaris companion to pulse's Erick #2228 (May 29, +1654). Together they complete the full Paradigm streaming RFQ infrastructure on both sides of the stack.

### Theme (June 3–4)
**Headlines**: (1) **Wintermute full mktdata integration** (Emre, +1069 book + BBO + quote WS) — Wintermute LP is now live as a real-time market data source. (2) **OKX Turkey venue** (Ömer #2310) — new execution venue added. (3) **ESP market widget** (Estiven #2278, +1339, 28 files) — Halo now has a market widget with executable streaming price support; this is the UI for the Paradigm options streaming RFQ path. (4) **ExecutablePriceStreamer merged** (Erick polaris #618, +941) — the streaming price infrastructure is now complete on both pulse and polaris sides. (5) **Anton quant fixes** (#687 volatility annualization + #688 basis preservation) — production-quality corrections to risk calculations. (6) **Ömer flight-deck hardening** (12 PRs) — RPC mode dispatch, schemars upgrade, auth/encoding fixes; flight-deck is becoming production-ready.

---

## 2026-06-01 through 2026-06-02 (updated June 2 heartbeat)

### pulseprime/pulse — 21 new PRs

**Chris Davidson (5 PRs)**:
- **#2274 [Jun 2] (+943/-75, 22 files) — "new risk endpoint"** — **SIGNIFICANT**: new trade-engine risk endpoint (+868 net). Continues the options risk infrastructure build from May 27's massive risk PRs. Active options E2E testing underway.
- **#2285 [Jun 2] (+240/-37, 14 files) — "options timing fixes"** — options timing correctness across 14 files. Likely fixing race conditions found in E2E testing.
- **#2271 [Jun 1] (+513/-129, 14 files) — "update csv upload"** — CSV trade upload updates.
- **#2273 [Jun 1] (+156/-30, 11 files) — "sync trades fixes"** — sync trades correctness.
- **#2284 [Jun 2] (+2/-2) — "options bug fix"** — minor options fix.

**Estiven Salazar (8 PRs) — Halo + credit widget**:
- **#2286 [Jun 2] (+272/-1068, 23 files) — "credit-widget updates"** — **NOTABLE**: large net deletion (−796). Credit widget being significantly rewritten/stripped. Companion to #2276 (disable).
- **#2276 [Jun 1] (+2/-0) — "disabling credit widget"** — credit widget explicitly disabled. Prior Talos credit flow being replaced.
- **#2282 [Jun 2] (+633/-302, 24 files) — "styling updates for halo modals"** — Halo modal styling polish.
- **#2272 [Jun 1] (+584/-52, 29 files) — "talos stream query and timestamp filters"** — large Talos streaming improvements.
- **#2268 [Jun 1] (+456/-358, 20 files) — "halo sync trades updates"** — Halo sync trades refactor.
- **#2279 [Jun 2] (+7/-0) — "api-gateway executable stream endpoint"** — wires executable streaming endpoint into API gateway (companion to Erick #2228's pulse-side work).
- **#2288 [Jun 2] (+13/-3) — "okta vpn ui error messaging"** — VPN auth error message improvement.

**Erick Arce (3 PRs)**:
- **#2275 [Jun 1] (+118/-184, 20 files) — "kill quoting feed type"** — **NOTABLE**: removes the quoting feed type abstraction (net −66). Coordinated simplification with polaris #683.
- **#2269 [Jun 1] (+93/-27, 3 files) — "notify_session_id stamped on quote"** — session ID now propagated on quotes.
- **#2277 [Jun 2] (+5/-3) — "possible fix S3 parser timeout"** — S3 parser timeout fix.

**Talgat Taskhozhayev (2 PRs)**:
- **#2261 [Jun 1] (+172/-4, 11 files) — "DealLetter-Persister: Implementation"** — actual implementation lands (scaffold was #2248 from May 28). Options deal letter persistence service is functional.
- **#2289 [Jun 2] (+11/-10, 8 files) — "Decimal: Version upgrade"** — dependency upgrade.

**Emre Ekici (2 PRs)**:
- **#2283 [Jun 2] (+40/-59, 12 files) — "update outdated regression tests"** — test maintenance.
- **#2281 [Jun 2] (+88/-68, 1 file) — "instantiate inert venue factories"** — venue factory initialization refactor.

**Aksel Hakim (1 PR)**: #2266 [Jun 1] — gap fill pagination (already captured in June 1 batch).

### pulseprime/polaris — 8 new PRs

**Ömer Yılmaz (1 PR)**:
- **#684 [Jun 2] (+671/-18, 3 files) — "fix(risk): preserve account on empty ok-reason restatement"** — **SIGNIFICANT**: risk gate now correctly preserves account state when an order is restated with an empty ok-reason. Prevents stale account state from accumulating. +653 net.

**Erick Arce (2 PRs)**:
- **#683 [Jun 1] (+1/-12, 3 files) — "kill order entry quoting feed type"** — companion to pulse #2275; removes quoting feed type from polaris order entry path too. Coordinated cross-repo cleanup.
- **#682 [Jun 1] (+651/-127, 2 files) — "reject pretradegate for more reasons"** — **SIGNIFICANT**: pre-trade gate now blocks on more conditions (+524 net). Risk gating becoming more comprehensive ahead of options go-live.

All June 1 polaris PRs (#678-#681) already captured in June 1 batch.

### Theme (June 1–2)
**Headlines**: (1) **Chris's risk endpoint series** (#2274 +943, #2285 +240) — new risk endpoint + options timing fixes; options E2E testing actively underway in dev, with bug fixes landing same-day. (2) **Credit widget disabled and stripped** (Estiven #2276 + #2286, −796 net) — the Talos credit widget flow is being replaced; likely transitioning to the new risk endpoint path Chris is building. (3) **Erick kills quoting feed type** (#2275 + #683, cross-repo) — coordinated abstraction removal; simplification is accumulating. (4) **DealLetter-Persister implementation complete** (Talgat #2261) — options deal letters can now be persisted end-to-end. (5) **Erick #682 pre-trade gate hardening** (+651) — more blocking conditions; production risk controls tightening.

---

## 2026-05-26 through 2026-06-01 (updated June 1 heartbeat)

### pulseprime/pulse — 37 new PRs

**Chris Davidson (3 PRs)**:
- **#2224 [May 27] (+3187/-1714, 36 files) — "csv endpoint risk integration"** — **MASSIVE**: 36 files, +1473 net. Large overhaul of risk endpoint layer — CSV format for trade uploads + risk integration. Biggest PR of the week.
- **#2234 [May 27] (+3120/-481, 26 files) — "risk checks gross amount"** — **LARGE**: 26 files, +2639 net. Significant expansion of gross amount risk checking in trade engine. Together with #2224, this is a near-complete rewrite of risk infrastructure.
- **#2259 [May 29] (+840/-105, 30 files) — "user in comments"** — 30-file update, likely comment format or user attribution change.

**Estiven Salazar (13 PRs) — "Halo" launch sprint**:
- **#2233 [May 26] (+658/-450, 68 files) — "Atlas to Halo"** — **NOTABLE**: 68-file rename. The Atlas trading ops frontend is officially rebranded as "Halo."
- **#2235 [May 27] (+991/-142, 16 files) — "halo styling updates"** — Halo UI styling polish following the rename.
- **#2258 [May 29] (+916/-47, 25 files) — "new order widget"** — large new widget for order entry in Halo.
- **#2256, #2255, #2254, #2253, #2252, #2251, #2250, #2249 [May 28]** — widget library and package updates across booking-form, spot/options/RFQ/loans/crud/data-table widgets: +4818/-4263 net. Package modernization sprint.
- **#2237 [May 28] (+330/-72, 13 files) — "talos cancel trade endpoint"** — new cancel trade endpoint via Talos.
- **#2236 [May 27] (+176/-129) — "fixing newrfq exec report statuses"** — RFQ execution report status fixes.
- **#2232, #2231, #2230 [May 26]** — minor Halo fixes (CSV errors, spot booking LP qty, multileg booking).
- **#2246 [May 28] (+0/-6) — "haruko loans widgets api-gateway url updates"** — minor URL fix.

**Talgat Taskhozhayev (5 PRs)**:
- **#2248 [May 28] (+92/-1, 9 files) — "DealLetter-Persister: Setup"** — **NEW SERVICE**: scaffold for a new service to persist deal letters (options deal notifications). 9 files, new crate.
- **#2244 [May 28] (+67/-13) + #2240 [May 27] (+9/-5) + #2247 [May 28] (+1/-1) — "Trade-Engine DLQ kafka"** — Dead Letter Queue infrastructure added to trade engine. Prevents message loss on processing failures.
- **#2257 [May 29] (+1/-27) — "Option-Pricer: Removed Delta due to decimal precision issues"** — removed delta field from options pricer (precision bug).
- **#2245 [May 28] (+5/-2) — "Option-Pricer: handle() err handling"** — error handling fix.
- **#2229 [May 26] (+14/-39) — "Option-Pricer: Handle DST and remove volatility"** — DST handling fix; volatility field removed from pricer.

**Erick Arce (2 PRs)**:
- **#2228 [May 29] (+1654/-94, 9 files) — "ExecutablePriceStreaming support"** — **SIGNIFICANT**: adds executable streaming price support to pulse (+1560 net). The pulse-side companion to polaris's "prep code for executable streaming prices" (#606, May 18). Enables the Paradigm streaming RFQ path for options.
- **#2260 [May 29] (+360/-224, 3 files) — "Improve flow encapsulation"** — flow architecture refactor.

**Ömer Yılmaz (3 PRs) — Binance Portfolio Margin**:
- **#2262 [May 31] (+23/-3, 3 files) — "Add ed25519_key for Binance PM DropCopy"** — signature method for Binance PM auth.
- **#2263 [May 31] (+48/-1) — "Update portfolio_margin_url to use source_code"** — Binance PM URL config fix.
- **#2264 [May 31] (+14/-21) — "Binance PM url venue def fix"** — venue definition fix.
- **#2267 [Jun 1] (+4/-0) — "Add hedge_only_current_delta field to Polaris schema"** — schema addition (companion to polaris #681).

**Aksel Hakim (1 PR)**:
- **#2266 [Jun 1] (+28/-5, 2 files) — "gap fill pagination"** — fixes pagination in gap-fill recovery logic. Part of Atakan+Aksel's trade history gap-fill work.

### pulseprime/polaris — 21 new PRs

**Anton Ronis (6 PRs) — risk gate correctness**:
- **#680 [Jun 1] (+179/-5, 2 files) — "fix(risk): allow directional de-risking in pre-trade inventory checks"** — important correctness fix: de-risking orders were being blocked by pre-trade inventory checks.
- **#678 [Jun 1] (+92/-22, 5 files) — "fix(quoting): invert perp position skew on client-facing books"** — perp position skew was inverted when exposed to client-facing books.
- **#668 [May 28] (+135/-56, 3 files) — "fix(risk): correct RFQ side semantics and resolve NOS strategy via QuoteMap"** — pre-trade risk gate semantic fix for RFQ.
- **#667 [May 28] (+212/-3, 1 file) — "fix(risk): clear quoting-account state on OTC strategy stop"** — prevents stale state when OTC strategy stops.
- **#664 [May 27] (+409/-35, 4 files) — "fix(matching): respect VWAP limit for RFQ flattened fills"** — VWAP limit enforcement on flattened RFQ fills.
- **#648 (May 26)** — shaper unification (already captured in May 26 batch).

**Ömer Yılmaz (12 PRs) — Binance PM + flight-deck hardening**:
- **#679 [Jun 1] (+408/-118, 3 files) — "Add venue field to position_change and venue-aware telemetry"** — position changes now track which venue drove them. Significant for multi-venue book attribution.
- **#676 [Jun 1] (+306/-4, 1 file) — "test(execution): comprehensive tests for OrderGateway account mapping"** — test coverage for a core execution component.
- **#674 [May 31] (+11/-1, 3 files) — "Add Binance Portfolio Margin support across schemas"** — Binance PM in polaris schema.
- **#675 [May 31] (+1/-1) — "Reorder Venue variants for consistency"** — cleanup.
- **#681 [Jun 1] (+124/-2, 2 files) — "Add hedge_only_current_delta flag to HedgeParams"** — new risk control: when enabled, hedge only current delta (don't carry forward delta). Useful for options hedging precision.
- **#652-#659 [May 26]** — flight-deck hardening: MongoDB datetime deserialization, Python migration compat, OnePassword vault UUID fix, URL encoding fix, infinite reconnect loop fix, unused constants removal.

**Erick Arce (3 PRs)**:
- **#666 [May 27] (+19/-26, 3 files) — "Remove book reset from inside book snapshot"** — architectural fix.
- **#671 [May 28] (+23/-13, 2 files) — "Fix several issues"** — misc fixes.
- **#672 [May 28] (+17/-23, 2 files) — "Switch to slice for ladder"** — minor ladder refactor.

### Theme (May 26 – June 1)
**Headlines**: (1) **"Atlas" → "Halo" rename** (#2233, 68 files, Estiven) — major product branding shift. The internal trading ops frontend is now "Halo." (2) **Chris's risk overhaul** (#2224 +3187 + #2234 +3120) — near-complete rewrite of risk checking infrastructure in trade engine; 62 files total, likely the options risk integration reaching completion. (3) **ExecutablePriceStreaming** (Erick #2228, +1654) — pulse-side streaming price infrastructure enabling Paradigm RFQ path. (4) **Binance Portfolio Margin integration** (Ömer, multiple PRs) — new execution venue. (5) **DealLetter-Persister new service** (Talgat #2248) — options deal letter persistence. (6) **Anton's pre-trade risk gate correctness series** — directional de-risk fix (#680), perp skew inversion fix (#678), VWAP limit enforcement (#664): risk gates are being tightened to production quality. (7) **Aksel gap-fill pagination** — trade history recovery work progressing.

---

## 2026-05-22 through 2026-05-26 (updated May 26 heartbeat)

### pulseprime/pulse — 5 new PRs (since May 22)

**Estiven Salazar (2 PRs)**:
- **#2226 [May 26] (+1839/-26, 22 files) — "haruko loans widgets"** — **LARGE**: first Haruko loan management UI widget suite in Atlas. 22 files, +1813 net. Enables ops to view/manage Haruko loans directly in Atlas.
- **#2227 [May 25] (+3/-1) — "fixing new rfq sides"** — minor RFQ UI fix.

**Amit Kirdatt (1 PR)**:
- **#2222 [May 22] (+11/-10, 3 files) — "Improve UI and Docker builds"** — minor infra/UI improvements.

**Emre Ekici (2 PRs)**:
- **#2225 [May 22] (+7/-3, 2 files) — "lower TS_DIFF_THRESHOLD"** — reduce QuestDB timestamp diff threshold.
- **#2218 [May 22] (+171/-67, 23 files) — "book reset ts fix"** — timestamp fix for book reset events across 23 files.

### pulseprime/polaris — 24 new PRs (since May 22)

**Anton Ronis (5 PRs)**:
- **#640 [May 26] (+795/-44, 1 file) — "feat(quoting): cap OTC hedging-counterparty quotes by total_delta"** — **SIGNIFICANT**: adds total-delta-based quote capping for OTC hedge counterparties (+751 net). New risk control: prevents over-quoting to a hedge counterparty beyond the book's total delta exposure. Key for options central risk book management.
- **#631 [May 25] (+61/-28, 3 files) — "fix(risk): negate net_position when reading client_position in pre-trade gate"** — correctness fix; pre-trade gate was using wrong sign for client position.
- **#624 [May 24] (+302/-64, 4 files) — "fix(risk): correct excess_delta formula and emit on overshoot changes"** — excess_delta calculation corrected; now emits on overshoot changes.
- **#625 [May 25] (+62/-118, 10 files) — "refactor(risk): remove unused delta_threshold field"** — cleanup across 10 files.
- **#648 [May 26] (+20/-19, 3 files) — "refactor(shaper): unify randomization gate behind TSP rand_qty flag"** — minor shaper refactor.

**Ömer Yılmaz / litityum (19 PRs)** — **flight-deck production-readiness sprint**:
- **#623 [May 25] (+1050/-246, 6 files) — "Add multi-mode support to flight-deck (ARB, OTC, STAGED)"** — **SIGNIFICANT**: flight-deck now supports ARB, OTC, and STAGED operational modes (+804 net). Major capability: algo control plane can operate in different contexts.
- **#633 [May 25] (+413/-1, 6 files) — "Add secrets manager for 1Password Connect API integration"** — **SIGNIFICANT**: 1Password Connect secrets management for exchange credentials. Production security infrastructure.
- **#634 [May 25] (+360/-27, 4 files) — "Add exchange authentication to flight-deck bot creation"** — exchange auth wired into bot creation flow.
- **#639 [May 25] (+373/-167, 1 file) — "Fix DB persistence and add authentication to resume/update operations"** — DB persistence correctness + auth for bot resume/update.
- **#627 [May 25] (+264/-229, 4 files) — "refactor(telemetry): extract SkewRecorder into independent service"** — telemetry refactor.
- **#628 [May 25] (+71/-8, 1 file) — "feat(telemetry): add metrics for total_delta and position_to_skew"** — new delta/skew telemetry.
- **#626 [May 25] (+33/-5, 4 files) — "feat(risk): add position_to_skew fields to DeltaSkew and PositionSkew"** — schema addition for delta/skew relationship.
- **#629 [May 25] (+31/-20, 1 file) — "fix(telemetry): store additional skew metrics to prevent GC"** — telemetry GC fix.
- **#630 [May 25] (+66/-62, 1 file) — "fix(telemetry): invert client positions to reflect LP perspective"** — telemetry viewpoint correction.
- **#636 [May 25] (+46/-0, 1 file) — "Add example flight_deck_config.yml"** — config example.
- **#635 [May 25] (+56/-53, 4 files) — "Refactor flight-deck imports"** — style refactor.
- **#638 [May 25] (+54/-55, 4 files) — "Remove onepass_token placeholder"** — config cleanup.
- **#641-649 [May 26]** — threadpool/worker config, WebSocket path fix, URL scheme parsing, MongoDB partial filter fix, connection loop logging, registration message fix, gzip compression fix (small ops fixes, total ~120 lines net).

### Theme (May 22–26)
**Headlines**: (1) **Ömer's flight-deck sprint** — ARB/OTC/STAGED multi-mode (#623, +1050) + 1Password secrets manager (#633, +413) + exchange auth (#634) + DB persistence fixes: the polaris algo control plane is becoming production-grade infrastructure over the long weekend. This is likely supporting the imminent live RenGen integration. (2) **Anton's risk management precision** — total-delta quote cap (#640, +795), correct excess_delta formula (#624), fix net_position sign (#631): the pre-trade and risk gate logic is being refined to production correctness. (3) **Estiven's Haruko loans widget** (#2226, +1839/-26, 22 files) — first Haruko loan management UI in Atlas. Ops no longer needs to leave Atlas to view/manage loans.

---

## 2026-05-22 (updated May 22 heartbeat)

### pulseprime/pulse — 15 new PRs (since May 21 heartbeat)

**Chris Davidson (4 PRs)**:
- **#2203 [May 21] (+1655/-543, 32 files) — "update risk model"** — **SIGNIFICANT**: large options risk model update in trade-engine. +1112 net lines across 32 files. Ties to Haruko margin/options risk path that's now critical path for HT Live.
- **#2212 [May 22] (+147/-288, 6 files) — "split options trades topic"** — splits Kafka topic for options trades (net -141). Complements risk model update.
- **#2214 [May 22] (+7/-22, 1 file) — "contra mpid change"** — **small but critical**: fixes Contra MPID config for options booking test (CSC expected Cayman CSDG KY1; wasn't set). Options test can retry once instruments are recreated.
- **#2216 [May 22] (+3/-1) — "secret fix"** — minor config fix.

**Estiven Salazar (5 PRs)**:
- **#2194 [May 21] (+787/-49, 10 files) — "manual booking widget bulk post updates"** — large manual booking widget expansion.
- **#2219 [May 22] (+6850/-1260, 42 files) — "atlas styling updates"** — **LARGE**: Atlas UI styling overhaul across 42 files (+5590 net). Largest frontend PR in weeks.
- **#2220, #2213, #2221 [May 22]** — new-rfq LP/risk-sub-account inputs, RFQ side UI, sync trades response cleanup. Small iterations.

**Talgat Taskhozhayev (1 PR)**:
- **#2193 [May 21] (+243/-79, 12 files) — "Option Pricer: EOD & Expiry recovery pricing"** — recovery path for EOD/expiry pricing on Mark-Pricer restart. Production hardening.

**Emre Ekici (1 PR)**:
- **#2217 [May 22] (+0/-8) — "remove questdb late arrival discard"** — removes QuestDB late-arrival discard logic.

**Eric Thill (1 PR)**:
- **#2211 [May 21] (+1701/-33, 14 files) — "local trade-engine and polaris"** — the `repos/pulse/local/trade-engine/` docker-compose stack for full local FIX integration testing.

### pulseprime/polaris — 2 new PRs (since May 21 heartbeat)

**Ömer Yılmaz (2 PRs)**:
- **#579 [May 22] (+1402/-101, 6 files) — "Flight deck rpc handlers"** — **SIGNIFICANT**: flight-deck now has full RPC handler layer (+1301 net). Algo control plane evolving into a real operational service.
- **#622 [May 22] (+422/-61, 10 files) — "health check and RPC observability to flight-deck"** — companion to #579: health check + Prometheus observability. Combined: +1724 net lines of flight-deck infrastructure.

### Theme (May 22)
**Headlines**: (1) **Contra MPID fix deployed** (Chris #2214) — unblocks the options test trade retry once Nikhil creates new instruments (old ones expired). (2) **Chris's "update risk model" (#2203, +1655, 32 files)** — largest options-related pulse change this week; directly tied to the Haruko margin integration blocking HT Live. (3) **Estiven's Atlas styling overhaul (#2219, +6850, 42 files)** — largest frontend PR in weeks. (4) **Ömer's flight-deck RPC infrastructure (#579+#622, +1724 net)** — polaris algo control plane gaining full RPC + observability. (5) **Eric's local dev stack lands** (#2211).

---

## 2026-05-21

### pulseprime/pulse — 1 PR

**Estiven Salazar (1 PR)**:
- **#2206 [May 21] (+1191/-238, 21 files) — "talos credit widget and ws endpoint"** — **large**: new Talos credit widget + WebSocket endpoint in Atlas. Adds real-time credit/exposure visibility. +953 net lines across 21 files. Likely enables live credit monitoring in the Atlas UI, relevant to options pre-trade risk path.

### pulseprime/polaris — 3 PRs

**Anton Ronis (1 PR)**:
- **#594 [May 21] (+1571/-167, 15 files) — "feat: per-book hedge capacity (1/3)"** — **SIGNIFICANT**: first of a three-PR series adding per-book hedge capacity management to polaris. +1404 net lines across 15 files. Per-book capacity constraints enable more fine-grained control over how much hedging capital is allocated per book — relevant to options central risk book work and multi-strategy hedging.

**Ömer Yılmaz (2 PRs)**:
- **#620 [May 21] (+96/-140, 3 files) — "Remove client account handling from hedging strategies and update cor…"** — removes client account handling from hedging strategy logic (net -44 lines); aligns with per-book capacity separation.
- **#619 [May 21] (+30/-27, 1 file) — "Client telemetry: fix Dropcopy gauges to use set() not add()"** — correctness fix: gauge metrics were accumulating instead of being set.

### Theme (May 21)
**Headline**: Anton's per-book hedge capacity series begins (#594, +1571/-167) — foundational work for options book management and multi-strategy risk control. Estiven ships a large new Talos credit widget (#2206, +1191) — real-time credit/exposure visibility in Atlas. Ömer cleaning up hedging strategy client account handling alongside the new capacity model.

---

## 2026-05-18 through 2026-05-20

### pulseprime/pulse — 27 PRs

**Emre Ekici (8 PRs) — Haruko loan management layer**:
- **#2168 [May 18] (+476/-1, 3 files) — "trading ops - haruko create loan endpoint"** — creates loans in Haruko from trading ops.
- **#2169 [May 18] (+341/-117, 3 files) — "trading ops - haruko loans endpoint"** — CRUD for Haruko loan contracts.
- **#2170 [May 18] (+229/-6, 2 files) — "trading ops - haruko delete loan"** — delete/terminate Haruko loans.
- **#2177 [May 18] (+33/-13, 3 files) — "trading ops haruko loan logs"** — logging for loan ops.
- **#2179 [May 19] (+631/-1, 3 files) — "trading ops - haruko get loan v2"** — **large**: Haruko loan v2 endpoint integration (+631 lines). Full loan lifecycle retrieval.
- **#2180 [May 19] (+289/-421, 5 files) — "trading ops - haruko v2 endpoints"** — refactor to v2 API.
- **#2181 [May 19] (+271/-77, 4 files) — "trading ops - haruko tests update"** — test updates for trading ops.
- **#2191 [May 19] (+5/-4, 1 file) — "trade engine docs update"** — minor docs.

**Erick Arce (5 PRs) — Haruko symbology + tick sizes**:
- **#2182 [May 19] (+36/-28, 5 files) — "Moving symbology of haruko"** — Haruko symbol handling moved/refactored.
- **#2183 [May 19] (+31/-37, 9 files) — "hrko>clst pt2"** — Haruko→CLST flow cleanup.
- **#2184 [May 19] (+5/-20, 6 files) — "Ea.hrko>clst"** — same flow, earlier part.
- **#2190 [May 19] (+251/-9, 1 file) — "Set haroku tick sizes when not set"** — **notable +251**: sets Haruko tick sizes when absent. Important for correct options order routing.

**Estiven Salazar (6 PRs) — Atlas manual booking widget**:
- **#2172 [May 18] (+116/-27, 2 files) — "atlas manual booking widget updates"** — iterating on manual booking UI.
- **#2173 [May 18] (+148/-48, 2 files) — "atlas manual booking widget more updates"** — further iterations.
- **#2174 [May 18] (+11/-7, 1 file) — "options-manual-booking widget expiry date hh::mm updates"** — expiry datetime handling in widget.
- **#2185 [May 19] (+44/-5, 2 files) — "atlas date validations"** — date validation in Atlas.
- **#2187 [May 19] (+8/-8, 2 files) — "atlas manual booking datetime validation bugfix"** — fix.
- **#2192 [May 19] (+88/-21, 4 files) — "admin add instrument reqs updates"** — instrument requirement updates for admin.

**Chris Davidson (3 PRs)**:
- **#2171 [May 18] (+2/-1) — "adjust language"** — minor.
- **#2178 [May 19] (+2/-2) — "lower to debug"** — logging level tweak.
- **#2189 [May 19] (+59/-7, 3 files) — "trade engine try read errors"** — better error handling for read ops in trade engine.

**Talgat Taskhozhayev (2 PRs)**:
- **#2175 [May 18] (+6/-24, 2 files) — "Tt.option pricer switch to utc"** — UTC timestamp fix in option pricer.
- **#2176 [May 18] (+1/-1) — "Option-Pricer: Option type/side fix"** — correctness fix.

### pulseprime/polaris — 12 PRs

**Erick Arce (9 PRs) — OTC reconciliation + streaming prices prep**:
- **#591 [May 18] (+2251/-324, 13 files) — "Complete recon integration with Haruko"** — **MASSIVE (+1927 net)**: full reconciliation integration between polaris and Haruko. Polaris now reconciles OTC positions against Haruko. This is the largest polaris PR since the ParentOrder refactor.
- **#600, #602, #603, #604 [May 18] — "Ea.first class recon otc" series** — iterative fixes building toward #591.
- **#605 [May 19] (+14/-19, 6 files) — "Fixes for OTC + haruko"** — post-#591 fixes.
- **#606 [May 19] (+983/-936, 2 files) — "Prep code for executable streaming prices"** — **large restructure**: lays groundwork for executable streaming price quotes in polaris. Near-zero net change (+47) but massive internal reorganization. Enabling the Paradigm streaming RFQ path.
- **#607 [May 19] (+6/-2, 1 file) — "Hack snapshot fix"** — small snapshot correctness fix.

**Anton Ronis (2 PRs)**:
- **#608 [May 20] (+119/-86, 3 files) — "Reconciler: derive mark price from hedge BookCache, not OTC BBO"** — reconciler now uses hedge book mark price instead of OTC BBO for correctness.
- **#610 [May 20] (+344/-91, 2 files) — "RFQ: flatten multi-level fills into a single ER"** — RFQ fills now flattened to single execution report. Simplifies the fills pipeline for options RFQ workflow.

**Erick Arce (#593 May 18)**: LadderEngine cleanup (already counted in May 14–18 section).

### Theme (May 18–20)
**Headlines**: (1) **Emre's Haruko trading-ops service now covers the full loan lifecycle** (#2168-#2181) — create/get/delete loans in Haruko from the trading ops layer. Combined with the positions and venue accounts work last week, this service is becoming the complete Haruko operational hub. (2) **Erick's #591 polaris recon (+2251/-324, 13 files)** — polaris now has full OTC reconciliation against Haruko. Largest single polaris change in weeks. (3) **Erick's #606 — "prep code for executable streaming prices"** — internal restructure enabling the Paradigm streaming RFQ path for options. (4) **Anton's #610 — RFQ fills flatten** and **#608 — reconciler mark price fix** — maturing the RFQ execution pipeline. (5) Talgat/Estiven continuing to polish options pricer correctness and manual booking UI.

---

## 2026-05-14 through 2026-05-18

### pulseprime/pulse — 29 PRs (heavy week)

**Emre Ekici (9 PRs) — Haruko trading-ops layer**:
- **#2148 [May 14] (+316/-0, 5 files) — "deribit twap price"** — Deribit price integration for TWAP execution. Feeds Deribit spot pricing into TWAP parent orders.
- **#2155 [May 15] (+103/-51, 11 files) — "venues-haruko-ext"** — Haruko venue extension/refactor.
- **#2152 [May 15] (+4/-6) — "twap price loop update"** — minor TWAP loop fix.
- **#2153 [May 15] (+16/-3) — "deribit price collector ttl"** — TTL config for Deribit index price collector.
- **#2156 [May 15] (+350/-1, 8 files) — "trading ops haruko positions"** — new trading ops service pulling Haruko position data. Part of a dedicated Haruko ops integration layer.
- **#2164 [May 18] (+199/-1, 3 files) — "trading ops - haruko venue accounts"** — venue account management in trading ops.
- **#2165 [May 18] (+20/-8, 2 files) — "trading ops error logs"** — error handling for trading ops.
- **#2166 [May 18] (+104/-25, 3 files) — "trading ops - haruko venue accounts fix"** — fix to venue accounts PR.

**Erick Arce (7 PRs) — Haruko fills/trade capture**:
- **#2139 [May 13] (+417/-5, 3 files) — "Trade Support for Haruko"** — hooks up trade execution support to Haruko; likely the fills-to-Haruko leg of the options booking flow.
- **#2136 [May 14] (+813/-297, 10 files) — "Account mapping driven from atlas"** — **large refactor**: account mapping is now driven from Atlas config rather than hardcoded. Net +516 lines. Core infrastructure change for options entity routing.
- **#2147 [May 14] (+263/-28, 4 files) — "Stamping more fill info on clst fills publisher"** — fills publisher now stamps additional fill fields downstream.
- **#2145 [May 14] (+22/-24) — "Fix fills publisher restart loop"** — fills publisher restart loop fix.
- **#2150 [May 14] (+124/-1, 3 files) — "Haruko secondary trade support"** — adds secondary trade handling to Haruko integration (likely for give-up or allocation flows).
- **#2159 [May 15] (+6/-6) — "Flip sides for talos fills publisher"** — minor side-flip fix in fills publisher.

**Talgat Taskhozhayev (3 PRs) — Options pricing maturation**:
- **#2142 [May 14] (+149/-36, 4 files) — "Option-Pricer: Publish standard mark price"** — Mark-Pricer now publishes standard mark prices in addition to M2M prices. Broadens the pricing pipeline output.
- **#2151 [May 15] (+207/-81, 6 files) — "Tt.option pricer m2m pricing eod and msg change"** — EOD pricing logic + message format changes in the options M2M pricer.
- **#2160 [May 18] (+315/-10, 8 files) — "Option-Pricer: Settlement/Expiry pricing"** — adds settlement and expiry pricing to the Mark-Pricer. The options pricing pipeline now covers M2M, EOD marking, and settlement/expiry.

**Estiven Salazar (6 PRs) — Trade engine + Talos UI**:
- **#2093 [May 13] (+1438/-211, 9 files) — "trade-engine strip markups"** — **significant refactor**: trade engine now strips markups from internal pricing. +1227 net lines. Major change to how client-facing markups are separated from internal prices. Worth reviewing.
- **#2140 [May 15] (+568/-18, 17 files) — "talos trades endpoint updates and widget"** — Talos trades endpoint + widget additions (Atlas). Large PR.
- **#2161 [May 16] (+796/-3, 15 files) — "talos balances endpoint and widget"** — Talos account balances endpoint + widget. Large feature addition.
- **#2157 [May 15] (+1/-2) — "TE zero exposure_limit incorrectly treated as unlimited credit"** — bug fix.
- **#2158 [May 15] (+5/-1) — "trade-engine, remove avg_px from exec_rpts"** — minor cleanup.

**Chris Davidson (5 PRs)**:
- **#2137 [May 14] (+162/-7) — "Adding fix acceptor flexibility"** — FIX acceptor configuration flexibility.
- **#2146 [May 14] (+72/-31, 2 files) — "Worktree cd.clean up exposure warning"** — exposure warning cleanup.
- **#2149 [May 15] (+101/-0, 5 files) — "flush producer on shutdown"** — Kafka producer flush on graceful shutdown. Prevents message loss.
- **#2154 [May 15] (+102/-10, 7 files) — "Worktree cd.cleanup auth token issue"** — auth token handling fix.
- **#2144 [May 14] (+0/-30) — "remove_coinbase"** — removes Coinbase venue (added May 12 in #2125, reverted 2 days later — likely premature).

**Matt Gow (1 PR)**:
- #2138 [May 14] (+0/-19) — removes the test-scaffold-app added to exercise the auto-scaffold pipeline.

### pulseprime/polaris — 10 PRs

**Anton Ronis (5 PRs)**:
- **#587 [May 18] (+546/-197, 5 files) — "refactor(engine): extract BookWalker to unify book-walking across engine crates"** — architectural extraction of `BookWalker` type to unify how the engine walks the order book across strategies. Reduces duplication.
- **#588 [May 14] (+393/-173, 5 files) — "Support single-sided RFQ"** — polaris now handles RFQ where only one side is specified. Important for options RFQ workflow (Paradigm integration path).
- **#572 [May 14] (+163/-5, 3 files) — "twap: symmetric-uniform child-order qty jitter (rnd_qty)"** — child order quantity jitter for TWAP.
- **#589 [May 14] (+1668/-244, 15 files) — "main -> twap"** — large main→twap branch sync.
- **#586 [May 14] (+51/-1, 2 files) — "schemas: add rnd_qty field to twap_params"** — schema addition for rnd_qty.

**Ömer Yılmaz (2 PRs)**:
- **#584 [May 14] (+774/-0, 3 files) — "Add OTC client telemetry tracking for positions and volumes"** — **+774 lines**: new comprehensive telemetry for OTC client positions and volumes in polaris flight-deck. Signals that polaris is now tracking OTC book state explicitly.
- **#590 [May 14] (+347/-3) — "Add client_volume_usd tracking to OTC client telemetry"** — USD volume tracking on top of the positions telemetry. Combined with #584: +1121 lines of OTC telemetry.

**Erick Arce (3 PRs)**:
- **#592 [May 15] (+44/-36, 9 files) — "Rename account parameters"** — codebase-wide account parameter rename across polaris.
- **#593 [May 18] (+107/-84, 1 file) — "Cleanup LadderEngine"** — LadderEngine cleanup (net +23 lines).

### Theme (May 14–18)
**Headlines**: (1) **Haruko operations layer emerging** (Emre's trading-ops PRs + Erick's fills/account-mapping work): A dedicated service for Haruko position/venue-account management is taking shape — this is the production ops infrastructure for options settlement and monitoring. (2) **Estiven's trade-engine strip-markups** (#2093, +1438) is the largest single-repo change of the week — fundamental change to markup handling in the trade engine. (3) **Options pricing pipeline complete** across all stages: M2M (#2123), EOD (#2151), settlement/expiry (#2160). (4) **Anton's single-sided RFQ** (#588) enables the Paradigm-routed options RFQ path decided May 13. (5) **Ömer's OTC telemetry** (+1121 lines) means polaris now explicitly tracks OTC book state. (6) **Coinbase removed** 2 days after being added — premature.

---

## 2026-05-13

### pulseprime/pulse — 3 PRs

**Talgat Taskhozhayev (1 PR)**:
- **#2129 [May 13] (+144/-83, 5 files) — "Option-Pricer: Kafka/FACT publishing of M2M priced options"** — **MILESTONE COMPLETE**: The options pricing pipeline is now end-to-end. Mark-Pricer can now publish M2M priced option values to Kafka topics (and onward to FACT). Combined with #2123 (Haruko BS76 integration, May 12), the full stack is: Haruko `price_positions/v2` → Mark-Pricer → Kafka → FACT. Options M2M pricing is eng-side complete, pending only Haruko risk model sign-off from the business side.

**Chris Davidson (1 PR)**:
- **#2126 [May 13] (+1124/-65, 22 files) — "usd price conversion"** — **TODO CLOSED**: Implements the mktdata publishers → FACT update for stablecoin→USD pricing conversion. Large PR; integrates USDC/stablecoin pricing into the FACT market data pipeline using Binance stables as source. Unblocks stablecoin mktdata flow and supports the Stablecoin→USD semi-automated milestone.

**Erick Arce (1 PR)**:
- **#2120 [May 13] (+135/-225, 11 files) — "Standalone StartTwap -> StageOrder"** — pulse-side rename/refactor to align with polaris's ParentOrder rename. Net -90 lines. Completes the StageOrder/StartTwap alignment between repos.

### pulseprime/polaris — 3 PRs

**Ömer Yılmaz (1 PR)**:
- **#582 [May 13] (+450/-70, 6 files) — "Replace `IndexSet` with new `AccountSymbols` type for handling account symbols"** — new type for account-level symbol management in polaris. Meaningful abstraction (+380 net); likely related to multi-strategy account routing work.

**Anton Ronis (2 PRs)**:
- **#581 [May 12] (+445/-56, 11 files) — "main -> twap"** — large sync of main into the twap branch (+445 lines, 11 files). Brings twap branch up to date with recent main changes including ParentOrder and execution_strategy work.
- **#577 [May 12] (+185/-27, 6 files) — "feat: generic rand_qty opt-in flag + generalized OrderShaper randomization"** — opt-in randomized quantity shaping for order execution. Generalizes the randomization logic beyond TWAP.

### Also from May 12 (missed in prior run)

**Emre Ekici (1 PR)**:
- **#2131 [May 12] (+139/-1, 16 files) — "Venue::Wintermute"** — adds Wintermute as a trading venue in pulse. New LP/market maker integration.

**Erick Arce (1 PR)**:
- **#2135 [May 12] (+107/-21, 7 files) — "Update trade-engine to forward account info downstream"** — trade-engine now propagates account context downstream. Likely needed for options booking flow (entity/account routing).

### Theme (May 12–13)
**Headlines**: (1) **Options pricing pipeline is E2E complete** (Talgat #2123 + #2129 together = Haruko→MarkPricer→Kafka→FACT). (2) **Stablecoin mktdata FACT integration done** (Chris #2126 = stablecoin→USD conversion in FACT pipeline). (3) **Wintermute added as venue** (Emre #2131). (4) Polaris order management layer continues to mature: Ömer's AccountSymbols type, Anton's OrderShaper randomization, twap branch sync.

---

## 2026-05-12

### pulseprime/pulse — 9 PRs

**Talgat Taskhozhayev (1 PR)**:
- **#2123 [May 12] (+894/-13, 11 files) — "Option-Pricer: Haruko implementation"** — **SIGNIFICANT**: Haruko M2M pricing is now integrated into the Mark-Pricer service. Adds the Haruko BS76 `price_positions/v2` call as the live pricing backend. This is the major milestone for OTC options M2M — the service can now price options positions in real-time via Haruko. Combined with the custom pricing/expiry work, the options pricing stack is substantially de-risked.

**Matt Gow (2 PRs)**:
- **#2121 [May 12] (+420/-0, 4 files) — "auto-scaffold infra for new crates landing on main"** — new CI automation that auto-scaffolds boilerplate for new Rust crates landing on main. Reduces friction for new service creation.
- #2127 [May 12] (+19/-0, 4 files) — **"[Test] add test-scaffold-app to exercise auto-scaffold pipeline"** — test for the above.

**Emre Ekici (1 PR)**:
- #2116 [May 12] (+39/-15, 4 files) — **"deribit price index multiple storages"** — enhances the Deribit index price collector to support multiple storage backends. Builds on #2105 (collector MVP, May 8).

**Chris Davidson (1 PR)**:
- #2125 [May 12] (+30/-0, 2 files) — **"Add coinbase venue"** — adds Coinbase as a venue in pulse refdata.

**Estiven Salazar (4 PRs)**:
- #2124 [May 12] (+262/-76, 7 files) — **atlas ui widgets updates** — Atlas UI widget polish sprint
- #2128 [May 12] (+47/-7, 2 files) — **new-rfq-widget symbol and styling updates** — RFQ widget polish
- #2118 [May 11] (+281/-52, 5 files) — **trade-engine: handling error and malformed messages and default values** — robustness improvement for trade-engine message handling
- #2122 [May 11] (+7/-1, 1 file) — **fixing new rfq widget nos side** — minor RFQ NOS side fix

**Chris Davidson (additional)**:
- #2115 [May 11] (+9/-0, 3 files) — **check json** — minor JSON validation addition

### pulseprime/polaris — 2 PRs

**Erick Arce (1 PR)**:
- #575 [May 12] (+1124/-1666, 28 files) — **TwapParent to ParentOrder** — codebase-wide rename completing the ParentOrder abstraction. Net -542 lines across 28 files. Combined with Anton's `execution_strategy` schema (#567), the new order management layer in polaris is fully settled (~3000+ lines touched over 2 weeks).

**Ömer Yılmaz (1 PR)**:
- #574 [May 12] (+260/-29, 5 files) — **Add Prometheus metrics tracking to flight-deck for bot status monitoring** — adds observability for bot status across strategies in the polaris flight-deck layer.

### Theme (May 12)
**Headline: Talgat's Haruko implementation (#2123, +894 lines)** — the Mark-Pricer now calls Haruko's BS76 pricing API live. This is the primary unblocked milestone for options M2M pricing. Erick's #575 completes the ParentOrder refactor; polaris order management is now structurally settled. Matt Gow ships auto-scaffolding infrastructure for new crates — operational quality improvement. Emre extends the Deribit index collector with multiple storage backends.

---

## 2026-05-09 through 2026-05-11

### pulseprime/pulse — 5 PRs

**Emre Ekici (4 PRs)**:
- #2105 [May 8] (+699/-1, 15 files) — **deribit index price collector** — full MVP implementation merged: WebSocket subscriber to all Deribit index feeds, QuestDB WAL+DEDUP write, 2-instance HA, config-driven index list. Major milestone for OTC options settlement path.
- #2110 [May 8] (+5/-0, 1 file) — **deribit price collector dockerfile** — container wiring for the new collector service
- #2112 [May 11] (+28/-0, 2 files) — **Coinone refdata skip maintenance** — skip instruments in maintenance mode for Coinone refdata fetch
- #2114 [May 11] (+26/-1, 2 files) — **CLAUDE rules for adding new schemas** — Emre added CLAUDE.md rules to pulse repo covering schema addition patterns; first explicit AI-tooling housekeeping contribution

**Talgat Taskhozhayev (1 PR)**:
- #2111 [May 9] (+3/-3, 1 file) — **Talos-Fills-Publisher: Better logging** — minor observability improvement

### pulseprime/polaris — 3 PRs

**Anton Ronis (2 PRs)**:
- #567 [May 10] (+408/-269, 7 files) — **schemas: reshape parent_order_params/parent_order/parent_order_status around an execution_strategy variant** — significant architectural refactor in polaris; introduces `execution_strategy` as a first-class variant, likely enabling clean routing to TWAP vs future strategies. Combines with Erick's ParentOrder work (#562/#563) to form a new order management layer.
- #566 [May 11] (+450/-17, 8 files) — **twap: symmetric-uniform lot-time jitter (rnd_dt)** — TWAP scheduling improvement; randomized lot-time to reduce clustering/predictability of child order submissions

**Erick Arce (1 PR)**:
- #565 [May 8] (+92/-76, 8 files) — **Remove defaults from TWAP** — TWAP cleanup, removes implicit defaults requiring explicit config

### Theme (May 9–11)
Emre's Deribit index price collector (#2105) is the headline — the complete MVP is merged, unblocking OTC options settlement pricing. Anton + Erick are converging on a major polaris refactor: `execution_strategy` as a variant (#567) + `ParentOrder` abstraction (#562/#563/#565/#566) = new order management layer in polaris. This is likely foundational for multi-strategy support beyond TWAP.

---

## 2026-05-08 (EOD)

### pulseprime/pulse — 2 PRs

**Chris Davidson (1 PR)**:
- #2099 [May 8] (+914/-35, 5 files) — **add deal ws** — large options WebSocket for deal entry; likely the WebSocket API surface for the options booking flow. Largest PR of the week — worth review.

**Estiven Salazar (1 PR)**:
- #2106 [May 8] (+204/-173, 7 files) — **atlas updates** — Atlas UI changes (net-neutral churn)

### pulseprime/polaris — 1 PR

**Erick Arce (1 PR)**:
- #564 [May 8] (+73/-3, 3 files) — **Missed fields for parent** — follow-up to ParentOrder PRs; fills in missing fields

### Theme (May 8 EOD)
Chris's deal WS PR (#2099, +914 lines) is the most significant — this is probably the WebSocket API surface for options deal entry, directly supporting the options booking workflow. Combined with Talgat's CustomerCredit optional (#2103) and Chris's instrument puller (#2102), options infrastructure is advancing fast. Erick's ParentOrder trilogy (#562, #563, #564) in polaris is now complete at +1253 lines — new order management abstraction worth understanding.

---

## 2026-05-07 through 2026-05-08

### pulseprime/pulse — 8 PRs

**Estiven Salazar (2 PRs)**:
- #2104 [May 8] (+1/-0, 1 file) — **fix atlas build themes** — minor theme fix
- #2100 [May 7] (+210/-152, 15 files) — **alert-manager-widget styling updates** — UI polish on Atlas alert manager widget

**Chris Davidson (1 PR)**:
- #2102 [May 7] (+124/-3, 1 file) — **Adding options to inst puller** — instrument puller now includes options instruments; part of options instrument setup pipeline

**Talgat Taskhozhayev (2 PRs)**:
- #2103 [May 7] (+23/-5, 3 files) — **Trade-Engine: Make CustomerCredit/exposures optional** — key architectural move for options pre-trade path; Talos credit check is now bypassable so Haruko can be the risk source for options
- #2095 [May 7] (+48/-40, 7 files) — **Talos-Fills-Publisher: booking fix** — fill publication correctness fix

**Atakan Kupeli (1 PR)**:
- #2012 [May 7] (+704/-4, 17 files) — **Admin tab options chain** — options chain admin tab merged after 1-2 week review lag

**Erick Arce (1 PR)**:
- #2097 [May 7] (+69/-70, 15 files) — Remove unneeded configs (net-neutral)

**Emre Ekici (1 PR)**:
- #2094 [May 7] (+17/-4, 1 file) — pem parsing error sanitize

### pulseprime/polaris — 5 PRs

**Erick Arce (2 PRs)**:
- #563 [May 8] (+868/-8, 4 files) — **ParentOrder part 2** — continued ParentOrder support work; large addition
- #562 [May 8] (+312/-24, 4 files) — **ParentOrder support** — new ParentOrder abstraction in polaris; likely foundational for new order management patterns

**Anton Ronis (2 PRs)**:
- #561 [May 7] (+51/-2, 2 files) — **twap: set prediction_side on OCR for Kalshi repeg** — Kalshi-specific TWAP correctness
- #559 [May 7] (+107/-4, 1 file) — **twap: fix BBO wait timeout to emit Canceled instead of Rejected** — BBO state correctness fix

**Ömer Yılmaz (1 PR)**:
- #560 [May 7] (+157/-42, 1 file) — **dual gauge support for TWAP telemetry** — exposes global + per-strategy metrics

### Theme (May 7–8)
Options infrastructure advancing on multiple fronts: Talgat making CustomerCredit optional (#2103), Chris adding options to instrument puller (#2102), Atakan's options chain admin tab merged. Erick's ParentOrder work in polaris (#562, #563) is notable — +1180 lines of new order management abstraction. Anton still shipping Kalshi TWAP correctness and BBO fixes.

---

## 2026-05-07 (EOD batch)

### pulseprime/pulse — 5 PRs

**Talgat Taskhozhayev (2 PRs)**:
- #2103 [May 7] (+23/-5, 3 files) — **Trade-Engine: Make CustomerCredit/exposures optional** — makes Talos credit checks optional; needed for options pre-trade path where Haruko (not Talos) is the risk source
- #2095 [May 7] (+48/-40, 7 files) — **Talos-Fills-Publisher: booking fix** — fill publication correctness fix

**Atakan Kupeli (1 PR)**:
- #2012 [May 7] (+704/-4, 17 files) — **Admin tab options chain** — options chain admin tab merged; three options chain PRs (#2012, #2007, #1933) merged after 1-2 week wait for Eric review

**Erick Arce (1 PR)**:
- #2097 [May 7] (+69/-70, 15 files) — Remove unneeded configs (net-neutral cleanup)

**Emre Ekici (1 PR)**:
- #2094 [May 7] (+17/-4, 1 file) — pem parsing error sanitize

### pulseprime/polaris — 3 PRs

**Anton Ronis (2 PRs)**:
- #561 [May 7] (+51/-2, 2 files) — **twap: set prediction_side on OCR venue_fields for Kalshi repeg** — Kalshi-specific TWAP correctness; OCR (OrderCancelReplace) now stamps prediction_side correctly on repeg
- #559 [May 7] (+107/-4, 1 file) — **twap: fix BBO wait timeout to emit Canceled instead of Rejected** — BBO wait state correctness fix; wrong cancel/reject code was being emitted

**Ömer Yılmaz (1 PR)**:
- #560 [May 7] (+157/-42, 1 file) — **Add dual gauge support for global and trading stats in TWAP telemetry** — telemetry improvement; TWAP now exposes both global and per-trading-strategy metrics

### Theme (May 7 EOD)
Talgat's `Make CustomerCredit optional` (#2103) is the most significant — directly enables the options pre-trade risk architecture (Haruko replaces Talos for options; Talos CustomerCredit must become optional so options orders can bypass the spot credit check). Anton still shipping Kalshi TWAP correctness fixes (#561) and BBO state fixes (#559). Atakan's options chain admin tab (#2012) finally merged after review lag. Erick continues net-neutral config cleanup.

---

## 2026-05-06 through 2026-05-07

### pulseprime/pulse — 8 PRs (May 6–7)

**Emre Ekici (3 PRs)** — PEM utils cleanup:
- #2094 [May 7] (+17/-4, 1 file) — pem parsing error sanitize
- #2085 [May 6] (+19/-191, 2 files) — pem load cleanup (net deletion)
- #2084 [May 6] (+199/-197, 3 files) — already in prior batch (pem load refactor)

**Estiven Salazar (1 PR)**:
- #2087 [May 6] (+143/-16, 2 files) — **trade-engine last look rejection** — adds last-look rejection handling in trade engine; relevant for options pre-trade workflow

**Chris Davidson (1 PR)**:
- #2079 [May 6] (+249/-29, 1 file) — **enhance refdata venue map** — venue map enrichment; likely related to options instrument setup

**Erick Arce (1 PR)**:
- #2086 [May 6] (+101/-36, 3 files) — TWAP schema update

**Aksel Hakim (1 PR)**:
- #2082 [May 6] (+32/-5, 3 files) — spot booking symbol conversion

**Matthew Gow (1 PR)**:
- #2088 [May 6] (+1/-1, 1 file) — lock version to prevent upgrade (infra)

### pulseprime/polaris — 5 PRs (May 6)

**Erick Arce (4 PRs)** — TWAP execution module reorganization:
- #557 [May 6] (+46/-57, 11 files) — Move TWAP into execution module
- #556 [May 6] (+2/-2, 1 file) — sccache update to 0.15.0
- #555 [May 6] (+15/-12, 10 files) — Shift TWAP exec module
- #549 [May 6] (+326/-25, 7 files) — **TWAP limits** — adds limit enforcement to TWAP execution; 7 files, significant new constraint handling

**Anton Ronis (1 PR)**:
- #550 [May 6] (+304/-1, 2 files) — **twap: suppress lot-timeout cancel when aggressive price = resting price** — correctness fix; prevents spurious cancels on IOC cross; production safety

### Theme (May 6–7)
TWAP hardening continues in polaris — Erick reorganizing TWAP into its own execution module (4 PRs, structural) and Anton shipping another correctness fix (#550). Estiven's last-look rejection (#2087) in trade-engine is notable for options pre-trade. Chris's refdata venue map enhancement may support options instrument routing. Emre doing PEM utils cleanup (net-neutral refactor).

---

## 2026-05-05 through 2026-05-06

### pulseprime/pulse — 16 PRs (May 5)

**Eric Thill (1 PR)**:
- #2078 [May 5] (+103/-42, 1 file) — kalshi-dropcopy-puller retry changes — hardens dropcopy recovery

**Emre Ekici (3 PRs)**:
- #2075 [May 5] (+179/-178) — KLSH cancel replace v2
- #2074 [May 5] (+93/-94) — KLSH cancel order v2
- #2067 [May 5] (+9/-3) — PredictionProduct portfolio candle fix
- #2084 [May 6] (+199/-197, 3 files) — move pem load utils (refactor, net neutral)

**Estiven Salazar (8 PRs)** — Options booking + Atlas polish sprint:
- #2068 [May 5] (+215/-97, 7 files) — options manual booking endpoint updates
- #2065 [May 5] (+88/-24, 7 files) — manual-booking-widget endpoint updates
- #2073 [May 5] (+30/-13) — fix MarketAccount struct
- #2071 [May 5] (+59/-26, 7 files) — get talos market accounts endpoint
- #2076 [May 5] (+0/-2) — enable manual booking widgets
- #2077 [May 5] (+14/-11) — cloud-ui api key UI bugfixes
- #2080 [May 5] (+136/-72, 9 files) — atlas role management widget registry

**Talgat Taskhozhayev (1 PR)**:
- #2070 [May 5] (+103/-58, 14 files) — **Option-Pricer: Setup continued** — Mark-Pricer service active development

**Chris Davidson (1 PR)**:
- #2072 [May 5] (+60/-21, 34 files) — split clearstreet out — refactor

**Erick Arce (1 PR)**:
- #2081 [May 5] (+124/-11, 2 files) — fix kalshi refdata

**Ömer Yılmaz (1 PR)**:
- #2069 [May 5] (+85/-8, 9 files) — add DerivedBookDefinition to DerivedBook trait and sequenced events

### pulseprime/polaris — 4 PRs (May 5)

**Anton Ronis (1 PR)**:
- #532 [May 5] (+1116/-198, 5 files) — **twap: fix Partial timeout management in bookkeeper** — significant: partial timeout handling in TWAP bookkeeper. ~1.3k line churn across 5 files.

**Erick Arce (1 PR)**:
- #548 [May 5] (+553/-106, 8 files) — **TWAP price fixes** — 8-file TWAP correctness fixes, likely tied to live trading issues

**Ömer Yılmaz (2 PRs)**:
- #547 [May 5] (+66/-4) — track BboByNotional in BasisRecorder
- #546 [May 5] (+48/-1, 2 files) — add derived_book_definition schema and sequenced event field

### Theme (May 5–6)
TWAP stabilization continues at pace (Anton's #532 +1116, Erick's #548 +553). Estiven in a heavy options booking/Atlas widget sprint — manual booking endpoints, market account endpoints, widget enablement all landing together. Talgat's Mark-Pricer active dev is on track for May 8 Talos integration target. Kalshi cancel-replace v2 PRs (Emre) suggest order management refinement post-go-live.

---

## 2026-05-01 through 2026-05-05

### pulseprime/pulse — 34 PRs

**Eric Thill (3 PRs)**:
- #2043 [May 1] (+542/-100, 8 files) — kalshi dropcopy recovery — reconnect/recovery handling for dropcopy puller
- #2039 [May 1] (+44/-3, 6 files) — kalshi dropcopy default party ID
- #2046 [May 2] (+302/-205, 3 files) — fix claude's std::thread usage

**Emre Ekici (5 PRs)**:
- #2035 [May 1] (already captured)
- #2042 [May 3] (+247/-202, 3 files) — **KLSH NOS V2** — revised Kalshi new order single
- #2056 [May 4] (+8/-1, 2 files) — kalshi dropcopy puller debug logs
- #2062 [May 4] (+17/-0, 1 file) — **enable KLSH on rengen prod** — Kalshi live on RenGen production ← milestone
- #2067 [May 5] (+9/-3, 1 file) — PredictionProduct portfolio candle fix

**Estiven Salazar (10 PRs)** — API/widget buildout sprint:
- #2037 [May 1] (+154/-27) — talos post customers endpoint
- #2041 [May 1] (+94/-3) — talos update customer endpoint
- #2047 [May 1] (+33/-13) — add AccountManager role
- #2048 [May 3] (+82/-3) — talos get customer configurations endpoint
- #2052 [May 3] (+113/-4) — talos update customer configurations endpoint
- #2053 [May 3] (+14/-1) — api-gateway talos customer endpoints updates
- #2054 [May 3] (+847/-10, 20 files) — **clearstreet account manager widget** — large new Atlas UI widget for CS Account Manager
- #2058 [May 4] (+17/-1) — api gateway deal entry endpoint updates
- #2059 [May 4] (+19/-12) — manual booking widget updates
- #2060 [May 4] (+50/-19) — clst-account-manager filtering non-numeric talos names
- #2064 [May 4] (+102/-7) — get market-account details endpoint

**Talgat Taskhozhayev (3 PRs)**:
- #2044 [May 4] (+67/-55) — Trade-Engine exposure currency based risk check refactoring
- #2061 [May 4] (+118/-0, 9 files) — **Mark-Pricer: Initial setup** — NEW SERVICE: options M2M pricing service scaffold
- (plus prior HouseAccount PRs captured in last batch)

**Chris Davidson (5 PRs)**:
- #2034 [May 1] (+674/-7, 11 files) — **Adding deal entry endpoint** — significant new endpoint for options deal entry
- #2038 [May 1] (+253/-29) — options deal entry updates
- #2040 [May 1] (+49/-4) — integer validation
- #2045 [May 4] (+622/-262, 10 files) — moving custom instruments to lib
- #2063 [May 4] (+269/-49) — wire in instrument creation
- #2066 [May 4] (+227/-104) — swapping out symbol on entry

**Aksel Hakim (1 PR)**:
- #2057 [May 4] (+679/-287, 10 files) — trading server spot endpoint — significant trading server update

**Erick Arce (2 PRs)**:
- #2049 [May 2] (+130/-41) — update system for Kalshi
- #2050 [May 2] (+7/-5) — prime Kalshi config

**Matthew Gow (1 PR)**:
- #2051 [May 4] (+19/-0) — publish cloud-ui build to S3 and invalidate CloudFront — CI/CD pipeline addition

### pulseprime/polaris — 27 PRs

**Anton Ronis (10 PRs)** — TWAP hardening continues intensively post-Kalshi-launch:
- #505 [May 1] (already captured)
- #513 [May 1] (+358/-171) — twap: register in OrderCache; fills flow via ContextMessage::OrderFill
- #514 [May 1] (+196/-9) — twap: one-shot takeout IOC via new TimedOut state
- #518 [May 1] (+2/-3) — twap: fix build after #513/#514
- #520 [May 1] (+5/-5) — twap: bypass skew/rate-limit stages, fix delta_bps denominator
- #499 [May 2] (+339/-102) — TWAP: extend _bps fields to support notional values
- #530 [May 2] (+380/-46) — **Add TwapState::Completed** for fully-filled parent orders
- #531 [May 3] (+282/-150) — twap: replace on_timeout enum with TwapTimeoutConfig variant; add Takeout max_lots cap
- #533 [May 4] (+270/-81) — TWAP: fix fill-rate EMA cold-start causing spurious aggressive cross at warmup
- #540 [May 4] (+95/-22) — test(twap): failing test — takeout IOC partial fill zombie parent
- #541 [May 4] (+526/-0) — **Add FIX protocol skill and code style rules** — Claude.md/AGENTS.md style addition to polaris

**Erick Arce (11 PRs)** — TWAP cleanup + polaris infra:
- #504 [May 1] (already captured)
- #509 [May 1] (+13/-21) — improve logging
- #512 [May 1] (+50/-26) — fix new issues
- #522 [May 1] (+169/-111) — latest round of TWAP fixes
- #526 [May 2] (+97/-49) — improve orderlookup
- #534 [May 3] (+97/-125) — refine code + remove unwraps
- #535 [May 3] (+174/-247) — more TWAP cleanup
- #537 [May 3] (+36/-67) — compact slicer
- #538 [May 3] (+127/-0) — adding math lib to polaris
- #539 [May 4] (+526/-0) — Add FIX protocol skill and code style rules (same as #541 — merged twice?)
- #542 [May 4] (+80/-109) — remove unnecessary error propagation for enabled_markets

**Ömer Yılmaz (2 PRs)**:
- #465 [May 4] (+340/-35, 21 files) — **Integrate schemars for JSON schema generation** — large: adds JSON schema auto-generation across polaris codebase
- #524 [May 4] (+378/-78) — **Support notional value calculations in FillTracker**
- #536 [May 3] (+9/-2) — use timestamp() in favor of transact_time

**Anton Ronis (additional)**:
- #543 [May 4] (+68/-0) — test(twap): failing test — partial timeout zombie (no inflight child)

**Erick Arce (authenticated mktdata)**:
- #527 [May 4] (+455/-246, 11 files) — **Authenticated mktdata** — significant: adds authenticated market data paths in polaris (11 files)

### Theme (May 1–5)
Three storylines:
1. **Kalshi crosses the finish line**: Emre's #2062 enables KLSH on RenGen prod (May 4). Eric's dropcopy recovery PRs (#2043) harden the infrastructure. Anton/Erick continuing TWAP hardening in polaris — 15+ polaris PRs in 4 days. Kalshi is now live.
2. **Options infrastructure buildout**: Talgat's Mark-Pricer scaffold (#2061) is the first options pricing service. Chris's deal entry endpoint (#2034, +674) is significant new API surface. Estiven building out Talos customer configuration API layer. All pointing toward the options test-trade architecture taking shape. The May 4 entity/lifecycle blocker is the current obstacle, not eng capacity.
3. **TWAP stabilization never stops**: Anton + Erick shipped ~25 polaris PRs in 4 days. Every TWAP edge case being exercised and fixed. TwapState::Completed (#530) and fill-rate EMA cold-start fix (#533) are correctness-critical for live trading.

---

## 2026-04-30 through 2026-05-01

### pulseprime/pulse — 6 PRs (new since last heartbeat)

**Eric Thill (4 PRs)**: Kalshi FIX infrastructure continues.
- #2036 [May 1] (+1/-0) — kalshi dropcopy log info (minor: log level cleanup)
- #2029 [Apr 30] (+47/-17, 5 files) — kalshi key config (wiring API key config)
- #2030 [Apr 30] (+5/-0) — missed dockerfile (dropcopy container)
- #2027 [Apr 30] (+2/-2) — quiet haruko unsupported symbol warning

**Emre Ekici (2 PRs)**: Kalshi order-flow fixes.
- #2035 [May 1] (+8/-1, 2 files) — **KLSH NOS exec type fix** — important correctness fix for Kalshi order execution type handling
- #2032 [Apr 30] (+12/-5, 1 file) — create all topics on post api key (topic creation on venue registration)

**Estiven Salazar (1 PR)**:
- #2033 [Apr 30] (+670/-8, 10 files) — **options manual booking widget** — large new Atlas UI widget for manually booking options trades. Relevant both for options day-1 and potentially Kalshi manual fallback.

### pulseprime/polaris — 2 PRs (new since last heartbeat)

**Anton Ronis (1 PR)**:
- #505 [May 1] (+195/-15, 2 files) — **twap: schedule-based upper-limit gate in compute_desired** — adds schedule-awareness to TWAP desired quantity computation. Robustness improvement for time-sliced execution.

**Erick Arce (1 PR)**:
- #504 [May 1] (+291/-244, 3 files) — Simplified supervisor state — refactor of TWAP supervisor state machine. Net +47, 3 files.

**Theme (Apr 30 – May 1)**: Final push before Kalshi May 4 deadline. Eric, Emre, and Estiven all shipping Kalshi-related pieces in parallel. Anton + Erick continuing polaris TWAP hardening right up to the wire. The Emre KLSH exec type fix (#2035) on May 1 suggests live testing is happening. Estiven's options manual booking widget (#2033) is the largest PR in this batch — significant new UI capability.

---

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

## Apr 30 — late afternoon batch (third run)

### pulseprime/pulse — 5 PRs

**Eric Thill (3 PRs)**: Post-PR cleanup on Kalshi FIX work.
- #2027 (+2/-2) — quiet haruko unsupported symbol warning (log level reduction)
- #2029 (+47/-17, 5 files) — kalshi key config (wiring Kalshi API key config)
- #2030 (+5/-0) — missed dockerfile (Kalshi dropcopy puller container)

**Talgat Taskhozhayev (2 PRs)**: CS Account Manager continuing.
- #2028 (+240/-87, 10 files) — Clearstreet-Account-Manager: Adding HouseAccount (substantial: adds HouseAccount type to account manager)
- #2031 (+3/-2, 1 file) — Clearstreet-Account-Manager: Adding HouseAccount (follow-up fix)

### pulseprime/polaris — 5 PRs — **TWAP hardening sprint**

**Anton Ronis (3 PRs)**: Heavy TWAP edge-case fixes, still pushing hard before May 4.
- #469 (+141/-17, 3 files) — TWAP: add `slippage_tolerance_bps` + aggressive IOC cross (issue #464) — new risk parameter + handling for IOC order crosses
- #498 (+1415/-74, 9 files) — **notable**: twap: admit into WaitingForBbo when BBO unavailable + slicer BBO ingestion fix. Large: fixes TWAP from blocking when BBO not present at startup. Critical for live trading robustness.
- #494 (+153/-134, 8 files) — already captured (math: jitter + Desired ADT split)

**Erick Arce (1 PR)**:
- #495 (+2075/-1179, 61 files) — **LARGE**: Update TWAP with main — 61-file merge bringing TWAP branch up to date with main. +896 net. Resolving post-Phase-3 merge debt.
- #496 (+124/-23, 11 files) — Copy some things down to main — landing other branch changes into main

**Ömer Yılmaz (1 PR)**:
- #493 (+656/-21, 5 files) — Flight Deck: DB connection — adds persistent database connection to Flight Deck service. FlightDeck is gaining state persistence.

**Theme**: TWAP is being hardened against production edge cases (BBO-unavailable admission, slippage tolerance, IOC cross). Anton's #498 (+1415) is the most significant: startup robustness when no BBO present is a real-world concern for a live trading system. Erick's 61-file merge (#495) closes the TWAP integration debt. Ömer adding DB persistence to Flight Deck — the algo control plane is gaining durability. Talgat's HouseAccount PRs in pulse continue Account Manager buildout.

---

## 2026-04-29 through 2026-04-30

### pulseprime/pulse — 12 PRs merged

**Emre Ekici (3 PRs)**: Kalshi integration push.
- #2009 (+1066/-10, 4 files) — KLSH order event handling complete (large, foundational)
- #2014 (+62/-5) — KLSH order side fix
- #2021 (+20/-27) — Prediction quote_asset in ProductTokens

**Estiven Salazar (3 PRs)**: UI and API work.
- #2020 (+552/-150, 12 files) — **notable**: manual booking widget added to Atlas
- #2013 (+29/-10) — api-gateway latency fix, WS stream flushing immediately
- #2010 (+120/-23) — entity management widget styling

**Anton Ronis (polaris, 8 PRs)**: Heavy TWAP stabilization + new work.
- #474 (+1210/-780, 11 files) — size emit_cross_cxr against child leaves (correctness fix, large churn)
- #476 (+1125/-879, 10 files) — derive live child from OrderMap, remove current_child_cloid (second major correctness fix)
- #472 (+604/-70) — fix CxR/NOS emission, required fields
- #479 (+55/-22) — reconcile on live_child to harden blocked-order gate
- #482 (+333/-1) — stamp style/target_strategy on OrderState at inflight time
- #483 (+16/-3) — strip wall-clock transact_time in fixture
- #486 (+797/-43, 14 files) — TWAP merge
- #492 (+9/-4) — telemetry flake fix in basis::handle_bbo_updates

**Erick Arce (3 polaris PRs)**:
- #484 (+192/-17) — Request Stamping
- #486 — part of TWAP merge
- #488 (+11/-4) — startup issues fix

**Ömer Yılmaz (1 polaris PR)**:
- #466 (+312/-1) — standalone mode for Flight Deck (HTTP client + bindings)

**Aksel Hakim (1 pulse PR)**:
- #1975 (+346/-244) — quoting timing improvements

**Matt Gow (1 pulse PR)**:
- #2016 (+1/-1) — increase actix keep_alive from 10s to 75s

**Chris Davidson (1 pulse PR)**:
- #2000 (+289/-16) — new OTC create topic (Kafka surface for OTC trade creation, likely options booking plumbing)

**Notable**: Anton shipped ~5k lines of TWAP correctness fixes across two days (Apr 29-30). The TWAP is now substantially stabilized. Emre's KLSH order event PR (#2009, +1066) makes Kalshi E2E plausible in pulse. Chris's OTC topic (#2000) is new infrastructure for options booking. Omer's Flight Deck standalone mode is new — polaris algo management control plane.

### Apr 30 additional (afternoon batch)

**Eric Thill (2 pulse PRs)**: Kalshi FIX client engineering, branch `et.kalshi_fix`.
- #2023 (+1451/-10, 15 files) — **kalshi fix client boilerplate**: FIX session client scaffolding for Kalshi connectivity
- #2025 (+316/-0, 9 files) — **kalshi-dropcopy-puller part 1**: new app crate; connects to Kalshi FIX gateway (KalshiRT), re-encodes app-level FIX messages to wire bytes, publishes to `digital.kalshi.fix-drop-copy` Kafka topic. Schema ID 50039. This is the first pulse-side Kalshi FIX work.

**Estiven Salazar (2 pulse PRs)**:
- #2026 (+106/-1, 9 files) — initialize trading-ops server (new service skeleton)
- #2022 (+32/-15) — account-tier-mgmt widget: accounts autocomplete input

**Erick Arce (1 polaris PR)**:
- #480 (+1684/-1061, 45 files) — **"Inline and throw when math is wrong"**: large-scale refactor across 45 files. Likely hardening of numerical/math paths — inline assertions + panics where previous code tolerated silent errors.

**Anton Ronis (2 polaris PRs)**:
- #490 (+206/-60, 10 files) — TWAP: split client-facing and venue-facing counterparties (architectural clarity)
- #494 (+153/-134, 8 files) — math: extract symmetric-uniform jitter + split Desired ADT

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

---

## 2026-04-27 through 2026-04-28

### pulseprime/pulse — 21 PRs

**Emre Ekici (5 PRs)** — Kalshi operationalized:
- **#1988 "KLSH refdata categories"** (+340/-49, 3 files, Apr 27) — adds refdata category support for Kalshi instruments; part of making Kalshi production-ready
- **#1989 "enable KLSH on dev"** (+17/-0, 1 file, Apr 27) — Kalshi reactivated on dev environment. Reversed the Apr 20 decommission (#1887). Kalshi is now back on dev as prod ramp-up begins (May 4 deadline)
- **#1978 "standalone refdata diff mode"** (+221/-6, 5 files, Apr 27) — adds diff mode for standalone refdata; aids deployment workflow for instrument changes
- **#1990 "overview debug logs"** (+35/-3, 2 files, Apr 28) — debug logging in overview
- **#1993 "add missing cfg"** (+4/-0, 1 file, Apr 28) — minor config fix

**Estiven Salazar (6 PRs)** — Atlas UI continuing:
- **#1985 "balances widgets styling"** (+88/-28, 4 files, Apr 27), **#1986 "position summary widget"** (+44/-17), **#1981 "overview widget"** (+45/-17), **#1983 "atlas not found page"** (+101/-3), **#1984 "atlas unauthorized/forbidden flows"** (+129/-4), **#1982 "atlas landing page"** (+105/-80), **#1992 "open orders widget styling"** (+44/-14, Apr 28) — steady Atlas UI polish sprint continuing post-hackathon
- **#1980 "api-gateway with_path_overrides enhancement"** (+47/-16, Apr 27) — API gateway enhancement

**Talgat Taskhozhayev (3 PRs)**:
- **#1974 "ClearStreet Account Manager: Implementation"** (+346/-1, 10 files, Apr 27) — **SIGNIFICANT**: implementation PR for CS Account Manager service (follows #1955 initial setup). 10 files, pure addition. This is the account management layer being built natively in CS services.
- **#1987 "Api-Gateway: Adding Clst-Account-Manager"** (+11/-2, 1 file, Apr 27) — wires the new account manager service into the API gateway routing
- **#1976 "findatadb migrations sync"** (+1/-2, Apr 27) — minor DB migrations

**Chris Davidson (3 PRs)**:
- **#1977 "haruko refdata swap"** (+179/-67, 13 files, Apr 27) — refactors Haruko refdata handling for swaps; affects 13 files
- **#1994 "cnr refdata fix"** (+32/-0, 1 file, Apr 28) — CNR refdata fix
- **#1991 "NewRfqWidget accounts endpoint"** (+73/-13, 4 files, Apr 28) — new accounts endpoint for RFQ widget
- **#1979 "fixing atlas cs-dev okta"** (+22/-18, Apr 27) — Okta fix for Atlas cs-dev env

### pulseprime/polaris — 5 PRs — **HEADLINE WEEK**

**Anton Ronis (1 PR)**:
- **#457 "TWAP Phase 2: supervisor, slicer, pegger enhancements (MVP)"** (+4637/-219, 36 files, Apr 28) — **LARGEST PR IN RECENT HISTORY**. Phase 2 of the TWAP smart-execution feature — the functional MVP. Adds: `LimitTracker::would_breach` (risk projection for TWAP admission screening), `TwapParent`/`TwapParentRegistry` state types, Slicer (time-based order slicing), Supervisor (lifecycle management), Pegger (price tracking). This is the complete TWAP execution engine. Built on Phase 1 schema (#456). Critical for Kalshi EDC swap hedging (30-min TWAP at market close).

**Ömer Yılmaz / litityum (2 PRs)**:
- **#461 "Initialize Flight Deck"** (+601/-22, 6 files, Apr 28) — **NEW SERVICE**: `FlightDeckService` for managing algorithm status via WebSocket. New `managed_algo.yml` schema for strategy statuses + RPC handling. Flight Deck = new algo management control plane in polaris.
- **#459 "Add support for Prediction product type and new venues"** (+245/-11, 1 file, Apr 27) — prediction market venue expansion in polaris, companion to Kalshi push

**Erick Arce (1 PR)**:
- **#460 "Twap target"** (+49/-18, 4 files, Apr 27) — TWAP target price handling; companion to Anton's Phase 1 (#456), lands before Phase 2

**Anton Ronis (additional)**:
- **#456 "TWAP Phase 1: schema and mode skeleton"** (+1110/-38, 19 files, Apr 27) — already captured; Phase 1 merged same day as Phase 2 follow-up

### Summary (Apr 27-28)
Two architectural headlines: (1) **Anton's TWAP Phase 2 (#457, +4637 lines)** — the full TWAP execution engine is now in polaris, directly enabling the Kalshi EDC swap hedging strategy by May 4; (2) **Ömer's Flight Deck (#461)** — new algo control plane service in polaris. Talgat's CS Account Manager implementation (#1974) is the other significant piece — native account management is being built out. Emre re-enabled Kalshi on dev (#1989) signaling the May 4 deadline is being treated as real.

---

## 2026-04-28 through 2026-04-29

### pulseprime/pulse — 20 PRs (most Apr 28, a few Apr 29)

**Estiven Salazar (7 PRs)** — Atlas UI polish and decomms:
- **#1999 "decommissioning rfq ui"** (+0/-3814, 36 files, Apr 28) — **SIGNIFICANT**: removes 3814 lines of old RFQ UI code. The legacy rfq-server client is being retired.
- **#2003 "decommissioning rfq-server"** (+1/-1231, 18 files, Apr 28) — companion: rfq-server itself decommissioned (-1231 lines). Old RFQ stack is gone; Atlas new RFQ widgets are the canonical path now.
- #1992 open orders widget styling, #1995 markup tiers endpoints, #1997 NewRfqWidget accounts, #2005 manual adjustments styling, #2010 entity management widget styling (Apr 29)

**Emre Ekici (3 PRs)**:
- **#1998 "KLSH account update"** (+80/-3, 2 files, Apr 28) — Kalshi account wiring; likely the account ID fix referenced in Apr 28 Jon Daplyn meeting (TWAP order needs proper account ID)
- #2006 "prediction symbol pricing" (+49/-9, 2 files, Apr 28) — prediction market symbol pricing fix
- **#2008 "Add TWAP support across schemas, endpoints, and APIs"** (+364/-26, 11 files, Apr 29) — Pulse-side TWAP API surface wired through to schemas and endpoints. Connects pulse TWAP capability to the polaris TWAP engine.

**Talgat Taskhozhayev (2 PRs)**:
- #2002 "Trade-Engine: Risk-checks message" (+2/-2, 1 file, Apr 28) — minor risk check message fix
- #2001 "Busy-spin back-off" (+6/-2, 2 files, Apr 28) — busy-spin optimization in trade engine

**Chris Davidson (4 PRs)**:
- **#2000 "new otc create topic"** (+289/-16, 9 files, Apr 29) — new OTC trade creation Kafka topic. A new event surface for OTC trade creation — likely plumbing for the options booking flow (transfer trade + allocation trade pattern needs its own topic).
- #1994 cnr refdata fix, #1993 add missing cfg, #1996 downgrade to warning (Apr 28)

**Aksel Hakim (1 PR)**:
- **#1975 "Ah.quoting timing"** (+346/-244, 6 files, Apr 29) — quoting timing changes across 6 files. Net -0 net size suggests a timing/scheduling refactor.

### pulseprime/polaris — 7 PRs (Apr 28-29)

**Anton Ronis (2 PRs)**:
- **#458 "TWAP Phase 3: telemetry and flight-replay regression"** (+1390/-245, 22 files, Apr 28) — Phase 3 of TWAP: telemetry instrumentation + flight recorder regression tests. The TWAP trilogy (Phase 1 schema → Phase 2 execution engine → Phase 3 telemetry) is now complete.
- **#472 "twap: fix CxR/NOS emission — populate required fields, remove dead wiring"** (+604/-70, 3 files, Apr 29) — TWAP CancelReplace and NOS field fixes. Active bug-fixing in TWAP post-merge, indicates system is being exercised.

**Erick Arce (4 PRs)**:
- **#468 "Repeg counter impl"** (+540/-346, 7 files, Apr 28) — repeg counter implementation; companion to Anton's TWAP. Tracks how many times the TWAP pegger reprices.
- **#467 "Revert sid from parent order id"** (+166/-259, 7 files, Apr 28) — reverts a previous sid assignment approach; likely a fix from Phase 2 integration testing
- **#471 "Child reject counter"** (+132/-0, 1 file, Apr 28) — tracks how many child orders are rejected in a TWAP execution
- **#473 "TwapParentTelemetry"** (+52/-35, 4 files, Apr 28) — telemetry for TWAP parent order state. All 4 Erick PRs are TWAP stabilization work.

**Ömer Yılmaz (1 PR)**:
- **#461 "Initialize Flight Deck"** — already captured from Apr 28 batch (landed same day)

## 2026-04-29 (additional — same-day merges)

### pulseprime/pulse — 7 PRs (all Apr 29)

**Emre Ekici (2 PRs)** — Kalshi order event completion:
- **#2009 "KLSH order event"** (+1066/-10, 4 files) — large: Kalshi order event handling
- **#2014 "KLSH order side"** (+62/-5, 2 files) — Kalshi order side field fix

**Estiven Salazar (2 PRs)**:
- **#2010 "entity management widget styling"** (+120/-23) — Atlas polish
- **#2013 "api-gateway latency fix: flush ws stream immediately"** (+29/-10, 5 files) — **notable**: WebSocket buffering latency fix; production quality signal

**Aksel Hakim (1 PR)**: #1975 "quoting timing" (+346/-244, 6 files) — timing/scheduling refactor for quoting engine.

**Chris Davidson (1 PR)**: #2000 "new otc create topic" — already captured.

**Ömer Yılmaz (1 PR)**: #2008 TWAP schemas — already captured.

### pulseprime/polaris — 3 PRs (all Apr 29, Anton Ronis)

All TWAP correctness fixes — Anton pushing hard before May 4:
- **#472** — CxR/NOS field fixes (already captured)
- **#474 "twap: size emit_cross_cxr against child leaves, not parent remaining"** (+1210/-780, 11 files) — **significant**: incorrect child order sizing fix; would have caused wrong hedge sizes in live TWAP
- **#476 "twap: derive live child from OrderMap, remove current_child_cloid"** (+1125/-879, 10 files) — **significant**: removes current_child_cloid tracking; derives live child from OrderMap; correctness + simplification

**Theme**: Anton pushing 3 TWAP correctness PRs in one day. The engine is being exercised against real Kalshi-like scenarios. May 4 deadline is the driver.

---

### Summary (Apr 28-29)
**TWAP is the headline story**: The full 3-phase TWAP build in polaris is complete (Phase 1 schema Apr 27 → Phase 2 execution engine Apr 28 → Phase 3 telemetry Apr 28). Erick + Anton are in active stabilization mode (4 polaris fixup PRs in one day, Anton already pushing CxR/NOS field fixes Apr 29). On the pulse side: **Emre wired TWAP through pulse schemas/endpoints** (#2008), making the Kalshi hedging E2E capability plausible by May 4. **RFQ UI decommission** is significant (Estiven, -5k lines across 2 PRs) — old rfq-server and client are gone; Atlas is canonical. Chris's new OTC create topic (#2000) is new infrastructure for the options booking flow.

**New from Studio/CS side (not pulse/polaris)**: Studio EMS Kalshi release scheduled **Apr 30** (confirmed via Notion Release Schedule). Adds L2 market depth, FACT instrument data, symbol picker, fractional trades, Kalshi workspace. This is Kevin's team (Odyssey squad) shipping the Studio-side Kalshi trading UI to match the Pulse-side integration.

---

## 2026-04-25 through 2026-04-27

### pulseprime/pulse — 16 PRs (Apr 24-27)

**Estiven Salazar (8 PRs, Apr 24)** — Atlas UI blotter + widget styling blitz:
- **#1965 "blotter widgets styling updates"** (+2450/-86, 15 files) — largest PR of the batch; Atlas blotter gets major styling treatment
- #1962 positions, #1961 RFQ orders, #1960 RFQ quotes, #1959 role management, #1958 static price overrides widget styling (all Apr 24)
- #1966 "atlas auth options timeout and retry handling" (+47/-9) — auth resilience improvements
- #1972 "alter markup_tier table migration" (+6/-0, Apr 25) — small DB migration for markup tiers
- **Theme**: Atlas UI is approaching visual completeness. Massive styling push (net +3k lines across blotter, positions, quotes, orders, widgets). Also fixing Atlas auth timeout/retry — production readiness signal.

**Erick Arce (2 PRs, Apr 24)**:
- **#1963 "Stamp venue on restatements"** (+570/-128, 69 files) — **notable, large**: stamps venue info on trade restatements across 69 files. Broad consistency fix; likely required for Talos post-trade data quality.
- #1968 "update feed state variable" (+140/-43, 9 files) — feed state management cleanup.

**Chris Davidson (3 PRs)**:
- **#1969 "updating exchange facts"** (+421/-45, 1 file, Apr 24) — large update to exchange facts configuration; affects venue behavior.
- #1964 "swap withdraw endpoint" (+56/-2, Apr 24) — small endpoint fix.
- **#1971 "user override fields"** (+479/-12, 2 files, Apr 27) — substantial addition of user override fields to exchange facts; likely expands per-user or per-account instrument/venue configurability.

**Talgat Taskhozhayev (1 PR, Apr 27)**:
- #1976 "findatadb migrations sync" (+1/-2) — minor DB migration sync.

**Eric Thill (1 PR, Apr 24)**:
- #1967 "scaleset processed revocation error to debug" (+4/-4) — log level change; noise reduction in prod.

### pulseprime/polaris — 2 PRs (Apr 27)

**Anton Ronis (1 PR)**:
- **#456 "TWAP Phase 1: schema and mode skeleton"** (+1110/-38, 19 files, Apr 27) — **SIGNIFICANT**: Anton shipping TWAP execution support in polaris. Phase 1 = schema + mode skeleton. Directly supports the 30-min TWAP mechanism needed for OTC options expiry settlement (Deribit index − strike over 30-min window). This is the polaris-side foundation for options expiry.

**Ömer Yılmaz (1 PR)**:
- **#459 "Add support for Prediction product type and new venues"** (+245/-11, 1 file, Apr 27) — adds Prediction product type and new venues to polaris. Kalshi prediction markets venue expansion.

### Summary (Apr 24-27)
Quiet on new services — consolidation and polish. Three standouts: (1) Anton's TWAP Phase 1 in polaris is the architectural event — directly enables OTC options expiry settlement; (2) Estiven's Atlas blotter styling blitz signals Atlas approaching production-readiness for P1.3 LT RFQ go-live; (3) Chris's exchange facts user override fields (+479) expands per-counterparty instrument configurability. Erick's venue stamping on restatements (69 files) is a broad correctness fix that pays off downstream in reconciliation. Eric himself merged a minor debug log change (#1967).
