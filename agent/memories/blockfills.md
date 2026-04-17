# Blockfills

## Status
In bankruptcy. CS is evaluating acquisition. First tech diligence meeting: **Apr 20, 11am** — Eric meeting the person who built Phase 3 (vol surface + risk sharing options system) at Blockfills.

Three-part acquisition rationale:
1. **Tech** — potential replacement for Talos (OMS) and/or Haruko (loan/borrow/risk)
2. **People** — small number of experienced staff remaining
3. **Customer book** — Blockfills clients would welcome CS stepping in

PDFs reviewed Apr 17: `notes/blockfills/6.1_Blockfills-Marvel_Architecture_V2.0.pdf` + `notes/blockfills/6.2_Blockfills-Marvel_System_Feature_Overview.pdf`

---

## Marvel System — What It Is

Full-stack crypto/multi-asset trading platform:
- **Critical path**: C++ (MD gateway, order gateway, trading application)
- **Non-critical**: Python/Go/React microservices
- **Storage**: MongoDB, CassandraDB, QuasarDB, proprietary DB
- **Infrastructure**: Equinix NY4 + LD5, AWS US/EU/Asia; hub-and-spoke, privately leased lines
- **Config-driven**: runs as monolith or distributed across DCs — only a config change

Asset coverage: Crypto (spot, futures, swaps, margin), FX, Loans/Swaps, CFDs, Options, Structured Products, Fixed Income, Equities.

---

## vs. Talos (OMS) — Strong Overlap

Marvel is a credible Talos replacement candidate:
- Streaming RFQ/liquidity aggregation to clients with per-client markup, credit, and leverage controls
- LP performance monitoring — underperforming LPs auto-removed from client streams
- FIX 4.4 + WebSocket + REST client APIs
- 50+ MD feeds, 25+ order gateways (UDP multicast → FIX → WS → REST preference order)
- Voice trade / RFQ chat booking — Blockfills' actual production use case
- Smart order routing, pre-trade risk checks, order splitting
- Vision OMS (internal broker UI) + Vision Trader (client portal)
- 400+ spot crypto + thousands of derivatives across 10+ venues in config DB

---

## vs. Haruko (loan/borrow/risk) — Partial Overlap, Key Gaps

Marvel has: loans/swaps as asset class, automated margin calls, client liquidation system, margin position tracking (unrealized PNL, cash vs margin positions).

**What Haruko has that Marvel's docs don't describe:**
1. **Options FV model** — Haruko's built-in fair value model is CS's planned M2M pricing source for OTC options (not raw Deribit prices). Suley testing whether it ingests live vol surface for real-time updates. Marvel: no mention of vol model, greeks, or options pricing anywhere.
2. **Full loan/borrow lifecycle** — amend, recall, margin call with operator-selectable liquidation levels, post-default partial vs full liquidation, notice periods. Marvel lists "Loans/Swaps" with zero lifecycle detail.
3. **Front office risk view** — Bob/Suley live in Haruko to see their book (greeks, exposure, portfolio-level risk across spot + options + swaps). Vision OMS/Trader are trade desk + client portal tools, not risk-focused front office.
4. **CS integrations already built** — Haruko→Olympus→BK (Vortec), Pulse Venue::Haruko, BK→Haruko recon, Voyager→Haruko for swap risk. Replacing Haruko = rebuilding months of work.

---

## Integration Concerns

- **Proprietary message bus** — inter-component communication is custom high-perf bus; Kafka only listed as an *output log option*, not native. Connecting to CS's Kafka-centric stack (BK, Pulse, Snowflake) requires adapter work.
- **Not a ledger** — Marvel tracks positions internally but doesn't replace BK. Does it post to BK, or sit in front as an OMS layer (like Talos today)?
- **Tech stack mismatch** — C++/Python/heterogeneous DBs vs. CS's Rust-first monorepo; two very different engineering cultures to maintain.
- **Bankruptcy/team risk** — people who understand the C++ core may already be gone.

---

## Strengths Worth Noting

- Tick data back to 2017 from 35+ venues — serious research asset
- DAG-based configurable strategy building blocks (no circular deps) — exactly the Phase 3 Polaris vol surface architecture CS needs
- Pre-written strategies: liquidity aggregation, two-sided market making, position accumulation, automated risk factor hedging, basket trading
- Back-testing system in C++/Python/Scala, distributable across cluster
- Research DB with green-field, pre-trade, and post-trade research flows

---

## Questions for Apr 20 Demo

1. Options pricing — is a vol surface / FV model built in? Who built it?
2. Loans — full lifecycle: amend, recall, margin calls, liquidation modes?
3. Front office risk UI — portfolio/greek level or trade/position level?
4. Kafka native? Or does CS need a custom adapter from the output log?
5. BK integration model — does Marvel post to external ledger, or is it OMS-only?
6. Vision OMS/Trader — replacement path vs. Studio EMS and Active Trader?
7. Team — who's still there? Who owns the C++ core?
8. Codebase health — when did active dev slow down?

---

## Front-End Demo — What to Verify Live

Claims in the docs that are easy to overstate; need screen confirmation:

**Liquidity aggregation**
- Show two different client configs side by side — per-client markup, credit, leverage actually distinct
- LP auto-removal for underperformance — is this live behavior or a dormant config flag?

**Instrument breadth**
- Show a live (or recent) options chain on screen — they list options as supported but the architecture doc never mentions greeks, vol, or pricing model
- Show a loan being created, not just a position on a blotter — "Loans/Swaps" is listed with zero lifecycle detail

**Risk management**
- Automated client liquidation — what triggers it, what does the operator see, walk through the workflow
- Margin call creation — show a margin breach and what fires

**Order routing**
- Smart order routing — show a routing decision across multiple LPs, not just a filled trade
- Pre-trade risk check rejection — show a max position or max order size block

**Configuration claims**
- "Assets added in real time, no external definitions" — have them add one live
- "Only a config change" to go monolith → distributed — probe how true this is in practice

**Vision OMS + Vision Trader**
- These have separate docs (not provided) — ask to see both UIs
- Vision Trader is the client-facing portal — this is the Studio EMS replacement question

**The highest-value thing to push on**: options greeks on screen. If they can show a live options position with delta/gamma/vega, that changes the Haruko calculus significantly. If they can't, options is just a booking stub.
