# Projects / Initiatives

Current delivery roadmap for Digital Assets at Clear Street (as of 2026-04-06).
Sources: "Digital Assets Program Tracker" Google Sheet (~/Downloads CSVs, migrated from "Digital Assets Build" Apr 2026) + Notion meeting notes + Notion project docs.

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

### P1.1 Scale — HT Spot Automation (RED — updated Apr 14)
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
- **BitGo exchange flow — RESOLVED (Apr 13)**: Settlement Models Discussion meeting defined the full architecture. Two settlement types: **contractual** (exchange/pre-funded: BitGo, Binance, Deribit — settles instantly, no fail) vs **obligated** (bilateral: RenGen, etc. — tracks obligations, allows partial settlement). BK action item: implement contractual settlement on TradeV2 object for exchange trades, PR target Apr 17. **BK approach (Apr 15 clarification)**: BK will hardcode detection in their Kafka handler — if the trade is from a Deribit account, treat as exchange trade. No trade type indicator needed from Pulse for now. **Pulse indicator deferred** until Pulse adds more exchange account types (Binance etc.) beyond Deribit, at which point hardcoding won't scale. Medium-term (end of April): automate BitGo→Talos flow. Longer-term (no date): Pulse as universal exchange gateway/normalizer — reverse proxy that normalizes exchange messages, starts with Deribit.
- **CS→Talos state sync — NEW (Apr 14)**: `clearstreet-trade-updater` app (Chris Davidson PR #1823) now in repo. Kafka consumer on `csc.bk.trades.v2.updated` topic; syncs trade cancellations and settlements back to Talos via API. Closes the CS-to-Talos feedback loop for STP. PR is +1037/-0 (new app, not yet deployed).
- **Studio counterparty access / activity screen**: Counterparty login to view trade activity timeline in Studio. Dev completing this week (Apr 14 week); go-live targeted next week.
- **BitGo Trade Review (DA-024)**: Backend done Apr 14 (confirmed); UI end of next week (~Apr 24).
- **Cayman company codes confirmed (Apr 10)**: CSDGKY1 and CSDGKY2 added to IRMA — CS Digital Cayman entities now have company codes. Unblocks entity-level booking once VASP sign-off received.
- **BitGo-as-exchange "Trade scenario" meeting (Apr 13 3pm)**: Addressing the design gap where BitGo-as-exchange (USDC→USD conversions) must be handled differently from BitGo-as-custodian (physical instruction). Contractual settlement for exchange trades, not physical instruction, to prevent double-instructing.

**4 reconciliation layers (defined, not yet built):**
1. Talos ↔ BK (front/back office)
2. BK ↔ BitGo (real-time + EOD snapshot)
3. Pulse ↔ Exchanges (independent execution verification)
4. BK ↔ Haruko (EOD; BK is source of truth)

**Trade reconciliation architecture (Apr 6, high priority, not started)**: Two Snowflake-based services — (1) EOD snapshot upload, (2) independent polling for updates. Customers Bank transactions/balances already pulling every 5 min into nostro recon (Ankit confirmed).

### P1.3 — LT RFQ to LP (GREEN)
Polaris doing RFQ/RFS to RenGen as LP. Talos for post-trade.
- **E2E testing completed** while Eric was out (week of Mar 30). Team reports "looking pretty good" but Eric hasn't reviewed yet (as of Apr 6). Starting to test native in-house piping.
- **Prod rollout target**: **Apr 24** (confirmed in program tracker Apr 13; slipped from ~Apr 17).
- **Digital Dev Sync Apr 9**: "Production readiness for Polaris to Talos RFQ" confirmed as a topic — review in progress. Chris Davidson's PR #1789 (remove Talos refdata filters, +1419/-86) merged same day, likely related cleanup.

### P1.4 — LT Front-to-Back (GREEN)
Digital Trade Engine routing RFQ to RenGen → Studio EMS + Active Trader. Apr 30.

### P2.1 — Crypto Swap (Complete)
Voyager + Athena upgraded for digital assets. BK→Athena integration complete. CFTC de minimis threshold tracking built.

### P2.3 — CFTC Swap Dealer Application (AMBER)
Working with Potomac + PWC. ~40% of control gaps in progress, 60% not started. Application target Jun 30 (6-9 month approval timeline). Risk hiring just started.

### P2.5 — OTC Options (AMBER) — CSC project formally created Apr 10
CSC (Clearing, Settlement, Custody) team created a formal project entry today: "Digital Asset Options" (Status: Not Started; Goal: Support OTC cash-settled crypto options). This is the CSC-side counterpart to Eric's Deribit integration work. Indicates CSC is now formally planning their side of the options build.

### P2.5 — OTC Options: Full Architecture Session (Apr 16, 1pm) — MAJOR
2-hour options design whiteboard. 14 participants. Full F2B design confirmed:

**Legal/entity structure:**
- Client options booked against CS Derivatives (US-licensed entity to sell options in US)
- CS Derivatives → passes risk to CS Cayman (back-to-back, Cayman stays delta-neutral)
- CS Cayman holds all risk, trades around positions, may hedge with Deribit/Paradigm
- CS Derivatives is flat (delta-neutral) for the foreseeable future

**4-leg trade booking model:**
1. Client buys option → booked on client account (CS Derivatives entity)
2. CS Derivatives sells to client → short position on CS Derivatives internal account
3. CS Derivatives buys from CS Cayman → flat on CS Derivatives (legs 2+3 net to zero)
4. CS Cayman sells to CS Derivatives → short on CS Cayman; Cayman now owns/manages the risk

Pulse generates legs 2+3 as bilateral trades when Talos sends leg 1.

**Booking system: BK** — BK already handles equity options and can support crypto underliers. BASIS doesn't book OTC options. BK estimated **3 weeks** of work for the options booking build. This is now the committed timeline target.

**Pricing distinction (KEY — clarified in Slack post-meeting, Suley + Bob):**
- *Sales/quoting price* = desk quotes to client; CS proprietary model; skewed to tilt the book or price to win/miss. Different from FV.
- *Fair value (FV) / M2M price* = Haruko's built-in FV model; used for internal mark-to-market PnL, margin calls, expiry settlement. **Do not use raw Deribit prices for bilateral options M2M** — they are different instruments with different prices.
- Haruko supports both models independently. Day 1: use Haruko's FV model for M2M. CS proprietary pricing model uploaded separately when ready.
- **Open question (Suley investigating)**: Can Haruko's FV model take continuous market inputs (e.g. live vol surface) and update in real-time, or only on-demand? Suley will test. This determines whether Pulse needs to push market data to Haruko for live pricing or just EOD.

**Margin calls:**
- Haruko generates margin calls (based on daily mark-to-market)
- BK records/tracks margin settlements via commitments mechanism (tracks expectation vs reality)
- Happy path: assume cash; allow manual override to coin
- Haruko→BK margin settlement flow needs to be wired (webhook/API — Kevin's team, mechanism TBD)
- Separate margin calls per position (spot vs options vs swap) until cross-margining/netting agreements in place

**CFTC reporting gap:**
- Only Voyager currently connected to KOR Financial (CFTC reporting)
- Options will be in BK, not Voyager — need to build BK→KOR Financial pipe
- David Sherby to own CFTC reporting through KOR Financial
- Action item: team to figure out integration path (can they piggyback on Voyager pipes?)

**Expiry:**
- Pulse acts as OCC-equivalent — publishes which options expire in-the-money and at what price
- BK runs similar process to listed options expiry (target ~2 weeks of work in BK)
- Cash settled in USD; no physical delivery; contract size = custom (usually 1:1)
- Expiry time is custom per contract (8pm EST or whatever was agreed)

**CFTC/regulatory:**
- No LOPR (Large Option Position Reporting) — that's listed only
- No open/close indicator in Talos for OTC — not blocking for OTC; default open
- Confirms sent to client = the "clearance" for OTC contracts
- No OCC involvement; CFTC reporting only

**Pending action items (Apr 16):**
- **Eric**: finalize pricing methodology (sales vs reference/valuation price distinction; exact reference calculation)
- **BK team (Hari/Kevin)**: implement trade booking for options (~3 weeks). Expiry process: 2-3 weeks additional.
- **David Sherby**: own CFTC reporting via KOR Financial / Core Financial (same system — called "Core Financial" in official Notion notes)
- **Kevin + team**: determine Haruko→BK margin call API design (investigating webhooks, PagerDuty, Slack integrations)
- **Team**: figure out BK→Core Financial integration path for CFTC reporting (Voyager has existing pipe; can they piggyback?)
- **Chris and team**: complete Talos integration work for options; instrument setup + refdata ~3 weeks
- **Pulse team (Eric)**: implement refdata setup + option pricing feeds (Deribit proxy price → Pulse → FACT). Also: expiry pricing (Pulse acts as OCC-equivalent)
- **Team**: project plan with estimates to be socialized starting week of Apr 20

**Additional confirmed details (Notion AI summary, Apr 16):**
- Exchange-traded Deribit options explicitly **out of scope for MVP** — OTC vanilla only
- Inter-affiliate margin (CS Derivatives ↔ CS Cayman): **may not be required** due to exempt foreign affiliate structure (legal to confirm)
- Margin commitment APIs (cash + coin): "a couple of days" of BK work
- Haruko margin calls: two separate APIs planned — one for cash commitments, one for coin commitments. Default = cash unless manually overridden.
- Portfolio margining / cross-margining: explicitly out of scope for now

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
**Hackathon offsite week of April 13 — NOW UNDERWAY.** Neil (Haruko, NY) + Rasmus (SecFin, CS) attending. Daily goal-setting 9am; daily status call 4pm.

**Hackathon goals finalized (Apr 9):**
- **Primary**: Full loan/borrow lifecycle automation: Haruko → Olympus ("Vortec") → BK and back. Sequence: Day 1-2 create borrow/loan via BK API (Rasmus has PR out to expose this); Day 2-3 commitment + settlement instructions (BitGo or manual); Day 3-4 settlement confirmation (BK→Vortec→Haruko) + mark-to-market; Day 4-5 margin calls + loan amendments/cancellations. Success = full lifecycle E2E including margin calls.
- **Secondary** (parallel): Spot trades booked → BK → back to Haruko for risk view. Potential proto changes between BK and Haruko.
- **Options descoped**: Nikhil confirmed OTC options not feasible this week, not even stretch goal. If team finishes early by Wed, may do OTC options architecture discussion (not implementation). Kevin's suggestion: more impactful to talk high-level architecture with full team present.
- **Business stakeholders** (Bob, David, Brian Stern, Suley) on-call, not sitting in room. Two 15-min blocks/day reserved for questions.
- **Friday Apr 17 noon demo**: Haruko integration showcase + AI Coding WG Guest slot 1pm.
- **Note**: "Vortec" = Olympus or Haruko↔Olympus integration layer (Wojciech Baj + Paul Collins owners).

**New loan flow requirements (documented in SFIN Notion, Apr 12):**
1. User enters loan in Haruko
2. Olympus captures → sends to BK
3. BK sets up receivable legs
4. BitGo movement → BK captures settlement
5. BK matches settlement to receivables
6. BK sends status update to Olympus
7. Olympus marks settled once coin movements confirmed
8. Olympus passes status to Haruko → loan flips to Active

**Contract management scenarios documented (SFIN team, Apr 12):**
- Collateral returns (margin excess): clean return, hard-block if would breach margin %, re-calc after principal repayment
- Margin calls (deficit): open loan = accept partial principal repayment or recall; fixed-term = require collateral, not principal repayment
- Recall/termination: notice period from Confirmation, not just MLA default (may be 5-10 days for open loans)
- Post-default partial liquidation: CS Digital has **full discretion** on how much collateral to sell — target initial LTV, custom level, or full liquidation. Haruko should support ops selecting resolution mode.
- Post-default full liquidation: proceeds applied in order (replacement assets → fees → excess returned to borrower). Shortfall = borrower liability at Fed Funds Rate.
- **Haruko design**: liquidation level field in Confirmation is anchor; Haruko should not hardcode a single liquidation path.

**Code progress (pre-hackathon PRs landed):**
- Emre #1795 (Venue::Haruko scaffold, +196/-0, 18 files) — already in
- Emre #1796 (HRKO refdata fetcher, +490/-8, 9 files) — already in
- Emre #1798 (HRKO position update, +737/-7, 9 files) — **positions pipeline live**
- Emre #1804 (HRKO balance update, +631/-7, 3 files) — **balance tracking live**

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
- **Deadline update (revised Apr 13)**: Original Apr 10 deadline missed. Outside counsel call scheduled for week of Apr 14. Decision expected by **April 24** (additional 1-2 weeks if alternative opinion needed). Even with Cayman entity set up in IRMA (Matt/Ryan targeting Apr 17), **cannot book trades until regulatory opinion received**.

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

### Talgat — upcoming priorities (updated 2026-04-14)
1. **Automated E2E tests — trade-engine + polaris** — pair with Erick Arce on end-to-end test coverage spanning both services. Close to ready.
2. **Pre-trade risk checks — credit-based** — check available credit before order execution in trade-engine. Two phases:
   - **Phase 1**: Poll available credit from Talos APIs (no new service needed). **DONE**: #1797 merged Apr 10 — risk check messages + cache initial setup.
   - **Phase 2**: Credit feed consumer in trade-engine. **IN PROGRESS**: #1812 merged Apr 14 (+276/-2, 6 files) — trade-engine now consumes a credit feed. Follow-up cleanup #1825 also merged. Dedicated risk abstraction service planned but not yet started.
   Not blocking E2E, but required for real production trading.
3. **Team code review** — walk the team through all his trade-engine work (digital venue setup, FIX server, audit trail, etc.).

---

## Kalshi / Prediction Markets (venue integration — Apr 15)

Emre merged `PredictionProduct` (#1833) and `Venue::Kalshi` (#1835) into pulse on Apr 15. This is a **firm-wide CS initiative**, not a Pulse-specific project — RenGen requested the integration and Clear Street has been building Kalshi support across the stack since at least January 2026.

**CS-wide Kalshi integration flow**: FACT (refdata/pricing) → Studio EMS (order entry) → Kalshi Klear (exchange connectivity) → BASIS (trade booking) → CSC (settlement economics) → RENG (position distribution) → Studio (position UI).

**Pulse's role**: Venue integration layer — execution bridge to Kalshi, same pattern as any other exchange. Emre's PRs add the `PredictionProduct` type and `Venue::Kalshi` scaffold so Pulse can route orders to Kalshi on behalf of RenGen.

Kalshi is CFTC-regulated. Contracts are binary Yes/No event contracts (economic indicators, financials, sports, etc.) settling at $1 or $0. A test trade using an S&P price range contract was being validated as of late March ([Prod] Kalshi Trading runbook exists in Notion).

**Status**: Production readiness checklist in Notion (`[Prod] Kalshi Trading`) — instrument setup, routing, and BASIS connectivity were mostly complete as of ~Mar 25. Pulse venue integration (Emre's work) lands this week.

---

## AI Review Roles (added Apr 14)

Eric added `repos/pulse/roles/` + `make review` target to the pulse Makefile. Three review personas:
- `rust-critic.md` — Rust idioms, safety, performance, error handling
- `trader-critic.md` — trading domain correctness (precision, order state machines, venue API usage, message ordering)
- `architecture-critic.md` — Pulse architecture (layer violations, venue boundary, service/worker patterns, workspace placement)

Usage: `make review role=rust-critic` or with extra prompt. Diffs from merge-base with main (committed + uncommitted). PR #1828 merged Apr 14.

---

## Blockfills — Potential Acquisition (NEW — Apr 16)

Blockfills is a crypto institutional OMS/trading platform currently **in bankruptcy**. CS is considering acquiring them. Three-part rationale:

1. **Tech stack** — Blockfills has a crypto-native OMS that could potentially replace both **Talos** (OMS) and **Haruko** (loan/borrow risk/front office). This is a major strategic angle.
2. **People** — small number of experienced staff remaining
3. **Customer book** — Blockfills clients would welcome CS stepping in; good customer acquisition opportunity

Eric is attending a **tech demo tomorrow (Apr 17 1pm)** — the "Blockfills/Clear Street: Tech" calendar item. This is the first diligence touchpoint. No decision made. Could be transformative (eliminates two major vendor dependencies) or could go nowhere.

**Watch for**: capabilities vs. Talos (OMS, RFQ, counterparty connectivity) and vs. Haruko (loan/borrow lifecycle, front office risk, positions). Eric is best positioned to assess the tech stack fit.

---

## Digital Milestones Alignment Meeting (Apr 15, 11:30am) — MAJOR

High-level leadership meeting (Uri Gruenbaum mentioned as having made crypto the top priority, expecting faster results). Significant new context:

### Three-Phase Roadmap Published
**Phase 1: Bread and Butter** (by beginning of June):
- Spot trading ✓ (near-complete)
- **Options trading** — on the Phase 1 list; test trade by end of April, automated by end of May (at risk)
- Lending/borrow loans — 3-4 days from E2E production readiness as of Apr 15

**Phase 2: Advanced** (by end of summer):
- Cross-entity margin collateral posting (BTC/ETH/SOL → digital)
- Automated lending across BD, FCM, CSD swap accounts
- Stablecoin USD funding
- Automatic loan topping up/pulling based on margin requirements

**Phase 3: Best in Class** (end of Q3):
- Low-touch swaps through CSD
- High-throughput trading via Talos with batch booking to Voyager

### High-Touch Execution Definition of Done (target end of April)
- Trades flow Talos→BK with no manual ops intervention
- Clients see orders and positions in Studio
- Trade confirmations complete
- Remaining: payments automation (incoming ahead of schedule, outgoing behind), full trade lifecycle in Haruko, automated BitGo instructions in prod
- Eric's team = ~4 people; ~12 person-months over 3.5 months (Dec–mid-April) including significant one-time groundwork

### Options — KEY ESCALATION
- **Blocker**: Kevin has been waiting 2+ weeks on Chris Davidson to confirm Talos can push options trades
- **Action item**: Kevin to message Chris Davidson AND Eric Thill about Talos options trading capability
- **Next step**: Wednesday Apr 16 2-hour whiteboard session to finalize options design (Rama, Rasmus, and team)
- OTC options: treat similarly to existing OTC options in BK; book through BK with expiry enhancements; test what breaks with digital underlier
- Exchange-traded options can result in perps — modeling approach unclear, needs design
- Timeline risk: test trade by end of April / automated by end of May is at risk
- Needs at least one additional developer dedicated to options

### Borrow/Loan Status
- ~3-4 days from E2E production readiness (as of Apr 15)
- Core coding mostly complete; manual booking corrections worked through
- Next steps: wire to instructions, then address margins
- Strategy: single-thread team to finish this before shifting to options

### Cross-Entity Funding — Two Separate Flows
- Flow 1: Loan cash lending across entities (from crypto collateral posting)
- Flow 2: Spot trade settlement across entities (stablecoin→USD conversion)
- Both involve similar mechanics; significant implementation overlap
- **Friday Apr 17 1-hour whiteboard session** scheduled to finalize design

### Custody (Silver)
- Silver cost basis support: issues taking 1+ month to resolve; tax reporting issues
- Options: in-source (3-5 year build), third-party alternatives (Gamekeeper), or fix Silver
- New provider = 5-7 months implementation

### CSC Infrastructure Deployments (Apr 15-16)
- **ssis with crypto wallet instructions** (Apr 15, prod verified): ssisgate + ssismaster updated to support crypto wallet instructions. This is Annika Wei's Crypto SSI spec work landing in prod.
- **commitments release for crypto** (Apr 15): creation, cancellation, and amends for digital asset trades
- **obligations release for crypto support** (Apr 16): cancellation of digital asset trades in obligations
- **settlementproxy fails crypto commitments** (Apr 16): update settlement status for failed crypto settlements

---

## Go/No-Go Review (Apr 23 10:30am) — May 1 Go-Live Target
Calendar: "7 Day Rollover | Go-No Go Review [New Go Live Date: May 1st]". Something is targeting May 1 go-live and entering final review next Thursday. Most likely candidates:
- **P1.1 Scale** (HT automation) — was RED, target was originally Apr 3, slipped. End-of-April was the revised target for BitGo automation and STP.
- **P1.3 LT RFQ** (Polaris) — April 24 target in tracker; could be a related go/no-go.
**Calendar confirmed for Apr 23 10:30am.** Digital Dev Sync 11am same day. This is a hard date — not to miss.

## Tech Roadmap with Brian Oliveira (Apr 20 10am)
Brian Oliveira is the new operational COO for CS Digital (~1 month in role). First meeting with Eric on tech roadmap using "Brian's spreadsheet." Agenda unknown — could be resource discussion, priority alignment, or roadmap review. Eric should come prepared on where digital eng is against Phase 1/2/3 milestones.

---

## Quarterly Product Update (Thu Apr 16 10am)

CS-wide engineering quarterly (Q1 lookback / Q2 lookahead). Format: 1.5 hours, ~30 sections, ~15 speakers, 2-3 min each, 3 live demos. **All presenters must update Global Jira by tonight (Apr 14, 8pm extract cutoff).** Items past due and gray (not started) need start dates updated or marked in-progress/delayed. Digital team has items to present. Studio EMS screens are still being refactored — not client-ready for demo until next quarter. Prep meeting notes in Notion: `3421043d-19d5-8023-89eb-f98fbc446389`.

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
**Architecture note (Apr 7, Suley via Slack)**: A "Spreader" component will send orders to Polaris for perps. The spreader algorithm comes from RenGen.

**CoinRoutes — confirmed direction (Apr 13, Eric + Suley conversation)**: CoinRoutes will be used for algo order execution (TWAP and similar algos). CoinRoutes routes orders to Pulse's trade-engine as the execution system. Direction is confirmed; previously was uncertain pending Chris Davidson's conversation with them.
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

### COPS Digital Onboarding Scope (Apr 13 kickoff)
Three product tranches all targeted Q2 end (in COPS):
1. **Spot trading** — Purchase and sale agreement (simplest)
2. **Credit agreement** — More complex
3. **Derivatives** — Most complex (ISDA), longest tail

**Crypto trading and custody** (BitGo subcustody model): NOT Q2 — needs more requirements + BitGo onboarding clarity. Will have institutional and retail flavors (~60% requirements overlap).

Multi-digital product onboarding (client wants spot + credit together) targeted Q2. Cross-business-line onboarding (digital + PB/FCM) may not make Q2.

**Apr 15 scope meeting** — team to agree on scope, prioritization, and build workflow diagram.

Current state: manually "bending but not breaking" — Q2 volume will exceed manual capacity. Urgency is real.

AI acceleration discussion: COPS engineering (offshore, WISN) already using Claude Code. Brian raised using it more formally as a case study for COPS digital onboarding build.

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

## Open Items / New Gaps (from Apr 13 DA Status)

### Stablecoin → USD Funding Flow
Clients want to send USDC and have it land as dollars in their prime account. Similar to existing (manual/hacky) RenGen flow. Requires Treasury and margin involvement due to conversion timing. Will create cost basis reporting requirement for Silver. Breakout session needed: Joe Pergola, Dolph, Brian Oliveira, others. Not yet scheduled.

### Portfolio Swap Capital Requirements (Mixed Assets)
Need to finalize capital treatment for portfolio swaps with mixed asset types (security-based swap vs non-security assets). Described as "critical linchpin" — will drive capital needs decisions. Most punitive approach taken until resolved. Target: early May. David Sherby + Charlie re-engaging Brian Oliveira.

### Token Expansion (Top 50)
Low-touch trading flow: token expansion to top 50 assets not started. Need to understand token due diligence lead time. Brian investigating.

### Two Prime
MLA still not received. Credit risk meeting this week. Target completion end of April. Small counterparty (lending to CS); sanity check of financials required.

### Capital Union Bank
On hold.

### Customers Bank → Kyriba (wire payments)
Alternative path being explored: Mahindra's (CS internal) payments team. Requirements meeting Apr 14. Actualize DocuSign sent for Kyriba but may be reversed if internal team can deliver by May/June.

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
