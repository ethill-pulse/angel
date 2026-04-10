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

### pulseprime/pulse — 0 new PRs merged

### pulseprime/polaris — 2 PRs merged

**Ömer Yılmaz / litityum (2 PRs)**: Telemetry improvements.
- #399: "Litityum/positions telemetry otc" (+249/-229, 2 files) — adds OTC position data to telemetry; net-neutral change count suggests refactor of existing telemetry paths.
- #403: "Litityum/telemetry remove strategy update" (+547/-35, 3 files) — **notable**: removes strategy updates from telemetry; +547/-35 net add suggests new telemetry structure being added while old strategy-update paths are removed.

**Theme**: Ömer continuing post-skew-refactor telemetry cleanup in polaris. After Erick's skewtable refactor, telemetry needs updating to reflect the new architecture.
