# Projects / Initiatives

Current delivery roadmap for Digital Assets at Clear Street (as of 2026-04-06).
Sources: "Digital Assets Build" Google Sheet (~/Downloads CSVs) + Notion meeting notes + Notion project docs.

---

## Phase Summary

| Phase | Name | Status | Target |
|-------|------|--------|--------|
| P0 | POC Single Firm Trades | **Complete** | Oct 2025 |
| P1.1 | HT Spot - Principal Execution (manual) | **Complete** | Dec 2025 |
| P1.1 scale | HT Spot - Principal Execution (automated, STP) | **RED / In Progress** | Apr 3, 2026 |
| P1.2 (1.3) | LT - RFQ to LP (Polaris + Talos RFQ to RenGen) | **GREEN / In Progress** | Apr 15, 2026 |
| P1.4 | LT - Front-to-Back Integration (Studio EMS + Active Trader) | **GREEN / In Progress** | Apr 30, 2026 |
| P2.1 | Crypto Swap (Voyager + Athena + BK) | **Complete** | Mar 31, 2026 |
| P2.2 | Crypto Portfolio Swap | In Discovery | TBD |
| P2.3 | CFTC Swap Dealer Application | **AMBER / In Progress** | Jun 30, 2026 |
| P2.4 | Perpetual Futures (CME, via FCM) | In Discovery | TBD (FCM ready Jun) |
| P2.5 | OTC Options | **AMBER** — limited eng capacity | TBD |
| P3 | Client Trading & Exchange Connectivity (agent + MTL) | Not Started | TBD |
| P4 (Loan) | Loan & Borrow via Haruko | **GREEN / In Progress** | May 15, 2026 |
| P5a | Payments - Cubix Inbound (Customers Bank → BK) | GREEN | Apr 10, 2026 |
| P5b | Payments - Cubix Outbound + Kyriba | **AMBER** | TBD |

---

## Phase Details

### P1.1 Scale — HT Spot Automation (RED)
Full STP: Talos → Pulse → BK → BitGo + Customers Bank recon.
- **Two BTC/USD trades flowed in production March 27 — fully automated, no human intervention** (confirmed in F2B demo 3/30)
- Company-wide demo targeting **April 18** for BitGo settlement instruction capability
- SSI wallet storage in prod (code merged), needs prod sign-off — ETA 4/17 for full SSI build
- Bank recon (Cubix) nearly done — ops validating as of Apr 6; Customers Bank API balance pull in progress
- BitGo security VM solution agreed (Shlomi Avivi); establishing VM access process, not day-1 blocker
- Trade confirmation: Brian shared PDF template (Apr 6), automatable — work not yet queued, design phase
- **Recon (EOD) — HIGH PRIORITY, NOT STARTED**: Real-time Customers Bank→BK and BitGo→BK sync are both operational (as of Apr 6). But EOD reconciliation statements not yet built. Must be completed before SSI work resumes.
- **Qubics integration** (Cubix/Customers Bank): Ankur (BK eng) working on it. Call Apr 7, target delivery ~2 weeks.
- Stablecoin collateral support: Apr 11 target; USDC→USD conversion tested via BitGo (3/30)
- **Known bug**: BK Pset resolving to DTC instead of crypto — hardcode workaround deployed; proper fix is a Pset rule in BK Gate
- **Known issue**: CSDGCT company code (Clear Street Digital CT) not recognized in BK — fell back to CSLLC for testing
- **Known risk**: CS Digital LLC is a **Reg T account** — 50% initial margin on traded positions (not expected 35%); journaled positions only require 35%. First trade triggered immediate margin call; Joe Pergola borrowed from CS Holdings to cover. Fix: correct maintenance margin override.
- **Concern**: BK leadership spreading thin; BitGo batch settlement only twice/day (not real-time)
- **SSI gap (critical)**: Current SSI model only supports 1 wallet per counterparty. Must support multiple wallets per coin per network. Short-term: embed network in counterparty name (e.g., "RenGen-Ethereum", "RenGen-Polygon"). Long-term: dedicated crypto SSI model with network field, Chainalysis scan, "good to trade" status flag. **Design spec now published**: Annika Wei (CSC team) posted "Crypto SSI enhancement" to Notion (Apr 7) — full proto design for inbound/outbound wallet types, approval workflow, audit log. Status: Not Started.
- **Completed**: BK-to-street event build — DONE (3/30). Trade object build — DONE.
- **Cayman entities**: Cayman 1 & 2 received US tax IDs; Matt Lusignan securing Irma company codes this week. Fall under North America category.
- **CLS→BitGo integration (P1.1 settlement)**: First successful E2E workflow completed Apr 4 — can create commitment and instruct BitGo. But current flow is too STP: needs a manual approval checkpoint between obligation creation and commitment creation (to prevent accidental instruction when coin not available). Target redesign complete: **end of April** (moved up from original June estimate).
- **BitGo exchange flow (new gap)**: Need to handle BitGo-as-exchange (e.g., USDC→USD conversions) differently from BitGo-as-custodian. Exchange trades should use contractual settlement, not physical instruction, to prevent double-instructing. Target: ~2 weeks. High priority alongside EOD recon.
- **Studio counterparty access**: Counterparty login to view trade activity timeline in Studio. Dev complete target: ~Apr 17.

**4 reconciliation layers (defined, not yet built):**
1. Talos ↔ BK (front/back office)
2. BK ↔ BitGo (real-time + EOD snapshot)
3. Pulse ↔ Exchanges (independent execution verification)
4. BK ↔ Haruko (EOD; BK is source of truth)

**Trade reconciliation architecture (Apr 6, high priority, not started)**: Two Snowflake-based services — (1) EOD snapshot upload, (2) independent polling for updates. Customers Bank transactions/balances already pulling every 5 min into nostro recon (Ankit confirmed).

### P1.3 — LT RFQ to LP (GREEN)
Polaris doing RFQ/RFS to RenGen as LP. Talos for post-trade.
- **E2E testing completed** while Eric was out (week of Mar 30). Team reports "looking pretty good" but Eric hasn't reviewed yet (as of Apr 6). Starting to test native in-house piping.
- **Prod rollout target**: Shortly after Apr 17 (not by end of next week, but soon after).
- **Digital Dev Sync Apr 9**: "Production readiness for Polaris to Talos RFQ" confirmed as a topic — review in progress. Chris Davidson's PR #1789 (remove Talos refdata filters, +1419/-86) merged same day, likely related cleanup.

### P1.4 — LT Front-to-Back (GREEN)
Digital Trade Engine routing RFQ to RenGen → Studio EMS + Active Trader. Apr 30.

### P2.1 — Crypto Swap (Complete)
Voyager + Athena upgraded for digital assets. BK→Athena integration complete. CFTC de minimis threshold tracking built.

### P2.3 — CFTC Swap Dealer Application (AMBER)
Working with Potomac + PWC. ~40% of control gaps in progress, 60% not started. Application target Jun 30 (6-9 month approval timeline). Risk hiring just started.

### P2.5 — OTC Options (AMBER) — CSC project formally created Apr 10
CSC (Clearing, Settlement, Custody) team created a formal project entry today: "Digital Asset Options" (Status: Not Started; Goal: Support OTC cash-settled crypto options). This is the CSC-side counterpart to Eric's Deribit integration work. Indicates CSC is now formally planning their side of the options build.

### P2.5 — OTC Options (AMBER)
Manual flow and requirements captured. Deribit for pricing data (Eric owns eng). Haruko for risk. Limited eng capacity until P1.1 scale and basics close out.

**Apr 7 — Two design meetings; major structural clarity now in memory:**

**OTC options (CS-written, Paradigm as LP for RFQ):**
- Cash settled in **USD** (default); future stablecoin settlement (USDC/USDT) possible by defining as currencies
- European exercise only; no early exercise
- Symbology: `CLSD.option.[underlier].[call/put].[strike].[currency].[expiry]`; exchange code `XXXX` (Deribit has no MIC yet)
- Settlement: moneyness at FACT price 4pm Eastern on expiry date
- OTC options expected to be hedged with listed Deribit options, or alternatively delta-neutral with underlying spot positions
- All positions flow BK→Haruko for consolidated risk view

**Deribit listed options (used for hedging):**
- Most liquid crypto options exchange
- Two types: **linear** (trade in USDC) and **inverse** (premium in BTC)
- Technically options on same-day futures; future never custodied — two-step settlement: option→future→cash USDC
- Underlier: Deribit BTC USDC index; expiry 8am UTC; European style + auto-settlement
- System currently only captures expiry *date*, not time — needs enhancement

**Entity / regulatory constraint:**
- **CS Digital CT can only trade spot on Deribit — NOT options**
- **Options must trade on CS Cayman entity**
- Cayman IRS sign-off still pending — this is a blocker before options can go live
- Risk management at account/book level (not entity level); CS Cayman has multiple sub-books

**Eric's action item (from Apr 7 meeting):** Determine if Deribit options can be enabled in Pulse for testing
**Kevin's action item:** Follow up with Chris Davidson on booking OTC options in Talos
**Eric's team** is prioritizing spot execution pipeline first; options work planned for Haruko hackathon period (Apr 13+)

**Aksel & Atakan work queue (assigned Apr 8):**
1. Get up to speed on Deribit options API + `app/clearstreet-*` publisher crates
2. Learn Kafka / publisher pattern (new area for them — mostly done standalone + exchange integrations)
3. Add **index price** to Deribit mark price feed (options prep)
4. Fix **rengen arber** — update to newer Pulse releases
5. Design **options chains as refdata primitive** — schema changes to enable a full options chain per asset/venue. Must sync with Eric before implementing. **This is the scalable Deribit options integration path** — it satisfies both the CSC action item (Eric + Nikhil) and avoids manual per-instrument enablement.

**Refdata design note:** Need to add options chains as a first-class primitive in refdata so entire chains can be enabled for an asset on a venue (vs. per-instrument today).

### P4 — Loan & Borrow / Haruko (GREEN)
First loan booked 3/27. Haruko prod instance up: hcad-cls1.prod.haruko.io
**Hackathon offsite week of April 13** — Neil (Haruko, NY, likely Thu/Fri) + Rasmus (SecFin, CS) attending.

**Hackathon goals finalized (Apr 9):**
- **Primary**: Full loan/borrow lifecycle automation: Haruko → Olympus ("Vortec") → BK and back. Sequence: Day 1-2 create borrow/loan via BK API (Rasmus has PR out to expose this); Day 2-3 commitment + settlement instructions (BitGo or manual); Day 3-4 settlement confirmation (BK→Vortec→Haruko) + mark-to-market; Day 4-5 margin calls + loan amendments/cancellations. Success = full lifecycle E2E including margin calls.
- **Secondary** (parallel): Spot trades booked → BK → back to Haruko for risk view. Potential proto changes between BK and Haruko.
- **Options descoped**: Nikhil confirmed OTC options not feasible this week, not even stretch goal. If team finishes early by Wed, may do OTC options architecture discussion (not implementation). Kevin's suggestion: more impactful to talk high-level architecture with full team present.
- **Business stakeholders** (Bob, David, Brian Stern, Suley) on-call, not sitting in room. Two 15-min blocks/day reserved for questions.
- **Friday noon demo**: Haruko integration showcase (confirmed on calendar as 11am).
- **Note**: "Vortec" = Olympus or Haruko↔Olympus integration layer (Wojciech Baj + Paul Collins owners).

**Margin call routing architecture (confirmed Apr 8 meeting):**
- **Swap clients**: Voyager handles all margin calls (receives cash balances from BK via Kafka; can value swap positions)
- **Spot-only clients**: Haruko handles margin calls
- **Mixed clients** (trading both): Two separate margin calls until consolidated risk system built — expected through at least Q3 2026
  - Potential mitigation: manager consolidates Swift instructions into single cash movement to client
- **Open work**: Voyager→Haruko integration needs to be built (for swap risk visibility in Haruko front office)
- **Open work**: Lisa→Athena pipeline needs to be built (futures hedge data for swap hedge monitoring)
- **Crypto quant model**: Risk team has built a model for BTC/ETH/SOL/other coins — not yet integrated into risk engineering platform; timeline TBD
- Product complexity concerns raised: team confused by expanding scope from Suley/others (futures on swaps, ETFs in custody, etc.)
- Haruko onboarding complete: 4 roles set up (Front Office, Risk, Ops, Read) with users mapped.
- **Haruko pushing to production this week (Apr 7 week)**: Spot trade booking for risk mostly complete. Haruko→CLS trade flow dev in progress (trade pushing mostly done, ledger side still needed). Symbology mapping (internal→Haruko) still outstanding.
- **BK→Haruko**: Most flows tested in dev. Main outstanding = reconciliation. Kevin to discuss recon requirements with Jason. Kevin's eng (Wasserman) will build BK↔Haruko recon.
- **Emre — Haruko venue integration (dropcopy)**: `Venue::Haruko` PR (#1795) merged Apr 9 (+196/-0, 18 files) — initial scaffold is in pulse. Full venue integration spec (order entry / dropcopy / mktdata) so Polaris can recon positions from Haruko on an interval or restart. Start with spot; expands to options. Pull via REST poll loop into standard Pulse venue abstraction. Decision rationale: CS Digital is out of fleet (security friction), Haruko is consolidated risk source, aggressive timelines. Kevin confirmed Haruko REST API is straightforward: https://platform.haruko.io/docs/#tag/Trades-Data
- **CSC/BK as future alternative for position data**: SOD options exist — S3 ledger files, Snowflake tables, BK gRPC API. Contact: Rasmus Leijon (Euro TZ). Kafka not ideal (no server-side filter, no SOW query). Not pursuing now.
- **Warning**: Avoid Rama (Mellacheruvu) for anything recon-related — will add weeks of meetings and relitigate all decisions.
- **Loan ledger implementation**: Moving from definition to implementation. S-FIN service can already create loan legs (cash + crypto). Rasmus + Paul finalizing integration details. Rasmus's team to meet this week to finalize approach.
- Haruko→Olympus→BK (Olympus/SFIN → ledger): Target completion this week.
- **Swap margin**: Will use Haruko as data source for margin calculations — avoids building internally. Yang Wu to coordinate Haruko→Voyager integration (with Yoon Lee from Voyager).
- **Risk team (Ricky, Yang) / Haruko**: Kevin Stevens handling their engagement. Not Eric's concern.
- **P&L/Studio**: Finance team asking about P&L numbers. Brian Stern starting to look at PMS→Studio integration. Jason to push Brian to document requirements.
- **2 Prime**: $3.8M equity with high leverage — concern raised. Awaiting MLA from their lawyers (no timeline). Yang Wu following up with Bob/Sully.
- Loan structure: bilateral B2B MLA (not repo — avoids MTL requirement); BitGo as custodian; ~7–7.5% cash borrow rate; CS can rehypothecate BTC collateral
- **Margin parameters finalized (Apr 6)**: 50% initial margin, 35% maintenance after day 1. Withdrawal based on lesser of SMA New York or House excess.
- **Haruko PMS integration** (Voyager margin model): Voyager calculates margin calls but needs risk model inputs from Haruko. Waiting on Amit Kirdatt to return from vacation to progress.
- 5 margin systems currently issuing calls simultaneously: Olympus, Bezos, Wrench, Voyager, Haruko

### P5 — Payments
- Inbound (Cubix/Customers Bank): GREEN, Nostro recon in ops validation; incorrect account number found and being corrected
- Outbound: AMBER — **Apr 7 decision: Kyriba bypassed for Qubics**. Build in-house approval workflow in Studio instead ($18K/6wks vs. minimal value since Qubics = same-bank transfers, no AML needed). Wire payments still need Kyriba separately (external banks → AML required). Target: **end of June 2026**.
  - Qubics = 4th payment type alongside ACH, EFT, wire
  - Approval thresholds: <$5M STP; >$5M manual 2-level review
  - No Plaid for Qubics bank account verification — ops does callback manually
  - Studio team building new Qubics payment type screen
  - Building team has only 3 people, new hire expected next month
  - Zip process cancelled (was for Kyriba integration)
  - Action items open: confirm with Scott Gutmanstein that in-house approach OK; Yui investigating bank account capture + Qubics flag design

### ⚠️ NEW RISK: VASP/CARF Registration (Cayman Entities)
Raised at Apr 6 weekly meeting. **Potentially 3-6 month critical path blocker** for Cayman entity bookings.
- Cayman entities may require VASP (Virtual Asset Service Provider) registration — legal opinion from Patrick Wilson expected by Apr 11.
- VASP registration = 3-6 months if required.
- CARF (Crypto Asset Reporting Framework): regulations not published until October; 2026 activity filed in 2027 — can run in parallel, not the immediate blocker.
- **Scope of impact unclear**: Pure US spot trades not touching Cayman = NOT blocked. Offshore hedging via Cayman (e.g., RenGen via Cayman I) = potentially blocked.
- Action: Brian Stern to align with Sully on which specific flows are impacted.
- This has downstream implications for the Cayman entity setup timeline and any derivatives hedging flow that routes through Cayman.
- **Deadline update**: Project plan CSV shows CARF obligation confirmation expected **Apr 10** (not Apr 11 as originally noted). Patrick Wilson kicking off VASP process.

---

## Key Systems

| System | Role |
|--------|------|
| Talos | OMS — crypto order management, RFQ desk tool |
| BK (Book Keeper) | Clear Street ledger — trade booking, journals |
| BitGo | Custody — CaaS model |
| Customers Bank / Cubix | Bank / payments API |
| Haruko | Loan/Borrow vendor + front office risk |
| Voyager | Derivatives trade booking (swaps) |
| Athena | Risk/analytics for derivatives |
| FACT | Reference data + pricing feed |
| IRMA | Account master |
| Olympus | Stock loan/borrow at CS |
| Studio EMS | CS low-touch EMS for businesses |
| Active Trader | New CS OEMS, written in Rust, launching now |
| Polaris | CS Digital algo platform — RFQ/RFS, connects to Standalone |
| Chainalysis | KYT compliance (crypto wallet screening) |
| Silver | Cost basis tracking (crypto tax lots) |
| Kyriba | Treasury / AML payments review (may not be needed for outbound) |
| RenGen | Liquidity provider (LP) for spot + first swap counterparty |

---

## Key People (non-Eric's-team)

| Name | Role |
|------|------|
| Robert Rutherford | Business lead, digital assets execution + funding |
| Dalf Hammerich | Business / entity setup, Cayman entities, BitGo |
| John DiBacco | Derivatives / swap trading desk |
| Suleyman Duyar | Front office trading, risk |
| Yang Wu | Credit risk |
| Ritesh Chaudhary | EMS/OMS product |
| Jason Price | BK product owner |
| Hari / Rama Mellacheruvu | BK engineering |
| Ankit Singh | BK eng (BitGo→BK, bank recon) |
| Ani Banerjee | Risk engineering |
| Nikhil Kulkarni | FACT / reference data |
| Collin Zoll / Yoon Lee | Voyager/Athena engineering |
| Matt Lusignan | Ops / client onboarding |
| Christy Moccia | Compliance |
| David Brown | Legal |
| Andrew Masich | Entity setup / vendor onboarding |
| Peter Kim | IT / Okta |
| Atul Pawar | Market risk / derivatives |
| Ricky Gunawan | Risk |
| Wojciech Baj | Haruko↔Olympus integration |

---

## Team Work In Flight

### Talgat — upcoming priorities (as of 2026-04-06)
1. **Automated E2E tests — trade-engine + polaris** — pair with Erick Arce on end-to-end test coverage spanning both services. Close to ready.
2. **Pre-trade risk checks — credit-based** — check available credit before order execution in trade-engine. Two phases:
   - **Phase 1**: Poll available credit from Talos APIs (no new service needed).
   - **Phase 2**: A dedicated **risk abstraction service** that serves both trade-engine (pre-trade credit checks) and polaris (periodic per-customer position recon). Backend is Haruko. Encapsulated so Haruko can be replaced or additional risk calcs added without touching consumers.
   Not blocking E2E, but required for real production trading. No implementation exists yet.
3. **Team code review** — walk the team through all his trade-engine work (digital venue setup, FIX server, audit trail, etc.).

---

## Eric's Eng Ownership (from spreadsheet)

- Talos ↔ Pulse connectivity
- BitGo connectivity (out of scope for now — manual ops)
- Deribit connectivity (P2.5 OTC Options)
- Front Office Risk System connectivity
- Digital Trade Engine (RFQ/RFS routing)
- Polaris RFQ integration
- Algorithmic Pricing & Execution (via RFS)
- Option underlier pricing source (FACT → EOD prices)

---

### Client Priorities (updated Apr 7)
**Multicoin** is the highest-priority client for 2026 — described in the Apr 7 CS Digital weekly as "the largest and most profitable client this year." Primary driver of urgency on perpetual futures and spreader product.

**Apr 7 CS Digital weekly — client demand context (Eric's notes):**
- **Multicoin**: Coming to do a trade with CS in the next day or two. Spot only for now, primarily Solana. Context on their size: did a $500M+ block with Galaxy last week. CS can only support ~$25M chunks today; will work in chunks.
- **Feyman Point**: Already in FCM process. Plan is to add them into digital to give them pricing visibility and get them into the mix.
- **Perps demand**: Every single client wants to trade perpetual futures through CS. Compliance restrictions prevent them from accessing Binance directly — they want a regulated US entity with CS's balance sheet. This is framed as CS's **largest opportunity**.
- **Regulatory edge**: Clients can't get margin relief on cross-product books at native crypto venues (e.g., long ETF basket + short Binance — no margin netting). CS's regulated structure + breadth is the differentiator. "No place you can do all these things under one roof."
- **Trust factor**: Many clients don't trust Binance; prefer facing a regulated US entity.

### Crypto Options (P2.5) — updated Apr 8
- Apr 7 meeting: "Crypto Options structure" + CSC transcript (published Apr 8) — full design clarity.
- Swaps desk actively interested in trading options now (John DiBacco, Suley, Bob requested it).
- **Eric action item (confirmed in writing)**: Develop scalable Deribit options integration into Pulse — co-owned with Nikhil Kulkarni. Conditional on IRS approval of Cayman entity.
- **Kevin action item**: Check with Chris Davidson on OTC option booking in Talos; assist if needed.
- **Nikhil action item**: Ask Suley about risk offset strategies when OTC and listed options have different expiration times.
- **Parallel path confirmed**: If Cayman entity not IRS-approved in time, proceed with OTC-only on Clear Street Digital, hedging via underlier (spot). This avoids being fully blocked.
- OTC format: European-style, cash-settled, Paradigm as LP for RFQs. Symbology: `CLSD.option.[underlier].[C/P].[strike].[currency].[expiry]`. Exchange code: CLST (unlisted). Moneyness at 4pm cutoff.
- Deribit listed options: two types (linear/USDC, inverse/BTC). Two-step settlement: option→future→USDC. Both settlement legs need BK tracking. System currently only captures expiry date, not time.
- Risk model: positions flow BK→Haruko. Risk at book level (not entity). Two books under CS Cayman: Central Risk Book (CRB, accepts all firm risk, makes unified hedging decisions) + sub-books (own hedge strategies).
- Open question: how to offset risk when OTC and listed options have different expiration times.
- Key venues: Deribit (small blocks), Paradigm (large blocks) — from Polaris Options spec.
- Manual enablement of Deribit options in Pulse is not scalable per Eric. The scalable path is **options chains as a refdata primitive** — when refdata supports subscribing to a full chain per asset/venue, instruments don't need to be enabled one-by-one. This is exactly what Aksel and Atakan are assigned to design (schema first, sync with Eric before implementing).

### P3 — Client Trading & Custody (updated Apr 9)
Not started (Eric's team) — CLST as agent + MTL application.

**⚠️ New deadline from Jon Daplyn (Apr 8)**: End of June for crypto custody functionality — surprised both Kevin Stevens and Brian Stern. Kevin's assessment: "probably going to be a stretch."
- Scope unclear: June target may apply to institutional clients only, active trading clients only, or both
- Two separate builds required (institutional + active trading) with shared infrastructure
- **Critical blocker**: BitGo tri-party wallets — needed to move funds on customer's behalf without per-transaction approval. Kevin re-engaged BitGo; received unclear response about a legal agreement awaiting BitGo's internal approval. Project may not be feasible without this. **Digital Dev Sync Apr 9 confirmed BitGo verification still pending.**
- Currency conversion (BTC/stablecoin/USD): route through Pulse (BitGo fees too high)
- COPS team is heavily booked; Matt Lee given heads-up
- RenGen OTC settlement flow: stablecoin→USD primary use case; entity chain still TBD
- Travel Rule compliance + Chainalysis AML integration required
- Primarily Kevin Stevens' area; Pulse is the execution venue for currency conversions

### Perpetuals (P2.4) — from PRD (updated Apr 6)
**Architecture note (Apr 7, Suley via Slack)**: A "Spreader" component will send orders to Polaris for perps. The spreader algorithm comes from RenGen. CoinRoutes is being explored as a shortcut to support it — but direction is uncertain, pending Chris Davidson's conversation with them. Early-stage planning.
- **Phase 1**: HT OTC 5-year forward; same expiry all clients (~4y11m rolling); Pulse calculates spot index → perp/spot basis; funding tracked in Haruko, pulled daily to Voyager, billed monthly
- **Phase 2**: Streaming prices, no-expiry perp; Talos→Voyager STP; CFTC reporting via Derivs Middle Office
- Entity chain: Client ↔ CSD ↔ Cayman I ↔ RenGen/Binance
- Polaris: streams/quotes RFQ from Cayman to CSD, marks up Binance funding rate

### Polaris Options — from spec (updated Apr 5)
- Polaris currently running spot + perps on Binance; shared central delta risk book
- **Phase 1**: Back-to-back only (listed strikes/expiries); Paradigm for large blocks, Deribit for small
- **Phase 2**: Risk warehousing; off-the-run expiries
- New greek books per underlier (BTC/ETH): Gamma, Theta, Vega
- Open PM decisions: delta thresholds, greek limits, skew function, markout methodology

### CFTC Swap Dealer (P2.3) — current state
- 160/185 procedures need fixes (86.5%); Risk Mgmt, Onboarding, Trading, Financial Reporting all at 100% needing fixes
- Working with Potomac + PwC; Potomac proposal still under review
- Jun 30 application target with 6-9mo approval timeline — very aggressive

## Client Onboarding (Digital)

From COPS followup meeting (3/30):
- **Fast-track option** being introduced: spot-only, US-domiciled, no omnibus → bypasses New Client Committee (NCC) as blocker while completing all steps
- ~**75% of clients** expected to be multi-product
- ~**50 clients** expected in Q3; H2 (Q3/Q4) is when digital starts generating meaningful firm revenue
- Multi-product onboarding solution: Q1 H2 (Q3 2026) target
- Wallet address collection via COPS/Studio authenticated UI — "day two" feature for now; currently via email
- Chainalysis integration into COPS planned (API call + audit trail per wallet review)
- Multi-product onboarding: clients currently answer same questions multiple times — cloning feature as Q2 interim relief
- Strategic vision: onboard legal entity first with foundational KYC, then client selects products

---

## Entity Structure
- **CS Digital CT (CSD)**: US trading entity
- **CS Digital Cayman I**: Internal hedging/layoff desk; not client-facing
- **CS Digital Cayman II**: Client-facing international, principal dealer
- Offshore hedging framework: CSD delta-neutral facing clients; hedges like-for-like to Cayman I; Cayman I manages offshore risk book

## Stale / Resolved Planning Questions

These appeared in the "Questions Require Answer" tab but are early-planning artifacts — do not flag them as open:
- OMS clearing/settlement ownership → resolved in practice; BK handles it
- Spot vs futures routing → resolved; not a live question
- Stablecoin for 24/7 settlement → not pursued for now

## Counterparty Onboarding Status

| Counterparty | Type | Products | Status | Notes |
|---|---|---|---|---|
| RenGen LLC | OTC/Market Maker | Spot, Swap | In Progress | ISDA w/ CS Deriv executed; awaiting parental guarantee |
| FalconX | Prime Broker | Spot, Swap, OTC Option, Borrow/Lend | In Progress | NDA executed; ISDA/CSA negotiation ongoing |
| Galaxy Derivatives | Trading/Market Maker | Spot, Swap, Borrow/Lend, OTC Option | In Progress | CS lending cash to Galaxy vs BTC; guarantee from CS Group/Holdings |
| 2Prime | Asset Manager | Borrowing | In Progress | CS borrowing from them; MLA; credit DD intro done |
| Valos | Asset Manager | Borrowing | Not Started | CS borrowing from them; MLA |
| Cantor | Client/Financing | Lending | Not Started | Awaiting final commitment |
| Binance | Exchange | — | In Progress | Cayman entity |
| Bybit, OKX, Deribit | Exchange | — | Not Started | Cayman entity |
| Capital Union Group | Banking/Custody | — | In Progress | — |

## PMS / Cost Basis Roadmap

| Phase | Cost Basis | Tax Reports | Timeline |
|---|---|---|---|
| Today | Silver | Silver (1099) | — |
| Canada | CA Lot Engine | FIS | 2027 tax season |
| Strategic Global | CSPA | TallyX | 2028 tax season+ |


## Longer Horizon (from roadmap)

- Expand tradeable assets to top 50 tokens by market cap — Q3 2026
- Principal Risk Taking — Q3 2026
- Structured Products — Q2 2026
- Forwards & Exotics — Q2 2026
- BitGo CaaS (client custody) — Q2 2026
- FINRA Continuing Membership — Q3 2026
- Cross/Portfolio Margin — Q3 2026
