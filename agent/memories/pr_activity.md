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
