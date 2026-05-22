2026/05/01 - EOW for Brian & Lily (Week of Apr 28–May 1)

=======================================================
Product delivery snapshot (by initiative)
=======================================================

Spot - HT Automation (P1.1)

- P0 items confirmed on track for Apr 30.
- End-to-end flow: execution, cancel, settlement, and Haruko integration all complete.
- Manual booking widget shipped (Atlas).

Spot - LT / RFQ (P1.3)

- DA-039 (Digital Trade Engine RFQ/RFS routing) and DA-040 (Polaris Algorithmic Pricing via RFS) both targeted May 15 completion — status to confirm post-weekend.
- BK netting: May 15. Polaris reconciliation logic first pass is in and being iterated.

OTC Options (P2.5)

- Design doc published (Talgat + Anton): Haruko BS76 via `price_positions/v2` endpoint (stateless, unlimited calls), 30-min TWAP expiry using Deribit index prices, Kafka delivery to FACT with CS instrument ID.
- Dev started Apr 29. Test trade in dev targeting May 1. Live target May 30.
- Open Q: CS rollover alignment (minor).
- Risk sign-off on pricing methodology: last formal gate; not blocking dev start.
- Tracker: "initial target" May 15 (milestone summary) vs. live target May 30 — worth aligning on messaging.

Stablecoin→USD (P5b)

- Booking model finalized Apr 29: 3-trade + 1 journal entry structure confirmed.
- Phase 1 = semi-automated (manual initiation of settlements/movements).
- Rama/Rasmus to provide Phase 1 delivery date by May 4.
- Blocker: LLC BitGo wallet not yet configured.

CAST / Client Custody (P3)

- COPS/IRMA/CAST kickoff Apr 29: two flows (institutional/Studio, Active/retail). CaaS product name is now CAST.
- Irma multi-account-subtype question (open for spot + credit different subtypes) deferred to Mally — flagged as critical for multi-product onboarding.
- June 30 at risk: COPS team also owns spot + credit counterparty flow; bandwidth concern.
- Kevin + Amit to provide API contract to COPS.

Recon

- Four-layer recon requirements formally published (Notion Apr 29).
- Chris Davidson: assigned to flatten Talos→Snowflake JSON (currently opaque blob) and consult me.
- Amit Kirdatt: building BitGo→Snowflake daily API job.
- Rita currently doing this manually — both jobs automate her process.

=======================================================
IC work this week (my team)
=======================================================

Anton Ronis (peer, Head of Quant — not direct report)
- TWAP Phase 1-2-3 trilogy: schema (#456), execution engine (#457, +4637 lines), telemetry + regression (#458). Full smart execution engine now in Polaris.
- 8 additional stabilization PRs: CxR emission, child sizing, blocked-order gate, counterparty split, style/strategy stamping, BBO admission fix (#498, +1415 lines), slippage tolerance (#469), jitter refactor.

Erick Arce
- TWAP integration: update TWAP with main (#495, +2075/-1179, 61 files) — closes all merge debt from Phase 2-3.
- Math correctness refactor (#480, +1684/-1061, 45 files) — inline assertions/panics where code previously tolerated silent math errors.
- Request stamping + startup fixes in Polaris.

Emre Ekici
- Prediction product type support (quote_asset in ProductTokens, order side fix).

Estiven Salazar
- Manual booking widget (#2020, +552 lines) — now live in Atlas.
- API gateway latency fix (#2013): flush WS stream immediately (production quality signal).
- `trading-ops-server` initialized (#2026) — new service skeleton.
- Entity management + accounts autocomplete polish.

Chris Davidson
- New OTC create topic (#2000, +289 lines) — new Kafka surface for OTC trade creation, plumbing for options booking flow.
- Haruko refdata swap refactor (#1977, 13 files).
- Minor CNR refdata fix, config additions.

Talgat Taskhozhayev
- CS Account Manager implementation (#1974, +346 lines) + API gateway wiring (#1987) — native account management service progressing (prerequisite for Talos migration step 1).
- HouseAccount type added this week (#2028, +240 lines).
- Options Pricing Engine design doc co-authored; dev started Apr 29.

Aksel Hakim
- Quoting timing improvements (#1975, +346/-244, 6 files) — quoting engine scheduling refactor.

Ömer Yılmaz
- Flight Deck standalone mode (#466, +312 lines) — HTTP client + bindings for algo management control plane.
- Flight Deck DB connection (#493, +656 lines) — persistent state for Flight Deck service.

Matt Gow
- actix keep_alive bump (#2016): 10s → 75s (production fix for connection lifecycle).

Me (Eric Thill)
- Haruko log noise reduction (quiet unsupported symbol warning).

=======================================================
Ongoing conversations
=======================================================

Options (P2.5)
- Tracker shows May 15 as "initial target" — live target is May 30. Worth aligning messaging before the May 4 Options Catch Up.
- Pre-trade risk (CSD cash balances → Talos): offline design between me + Chris Davidson + Rasmus; Lily scheduling call with Ani/Rama/Amit.
- Risk team buying power methodology (credit limit − PFE): timeline from Jason's team due this week.
- Client trading restrictions on margin/premium non-delivery: short-term feasibility still open (my action item).

Perpetuals (P2.4)
- May 15 confirmed "not realistic" in current tracker. Requirements clarification with FACT still needed (Monday meeting).
- Cayman 1 booking: Voyager vs Haruko — Suley's decision, impacts risk pipe for CSDerivatives→Cayman I hedge leg.

CAST / Custody (P3)
- BitGo org structure (one org + tagging vs. two orgs) — decision before infrastructure provisioning.
- Pre-trade velocity limit: BitGo can't expose proximity to daily limits; we must track separately.

Talos migration
- "Getting off Talos" estimate: still owed (P1 on my roadmap). Three-step plan defined; CS Account Manager is step 1 in motion.

=======================================================
Key dates next week
=======================================================

- Mon May 4: Options Catch Up 10:30am. FACT/Perp 10:30am. DA Status 1pm. Stablecoin date due.
- Tue May 5: Dev Sync. CS Digital weekly.
- Thu May 7: Dev Sync
