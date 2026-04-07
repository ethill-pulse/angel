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

### P1.4 — LT Front-to-Back (GREEN)
Digital Trade Engine routing RFQ to RenGen → Studio EMS + Active Trader. Apr 30.

### P2.1 — Crypto Swap (Complete)
Voyager + Athena upgraded for digital assets. BK→Athena integration complete. CFTC de minimis threshold tracking built.

### P2.3 — CFTC Swap Dealer Application (AMBER)
Working with Potomac + PWC. ~40% of control gaps in progress, 60% not started. Application target Jun 30 (6-9 month approval timeline). Risk hiring just started.

### P2.5 — OTC Options (AMBER)
Manual flow and requirements captured. Deribit for pricing data (Eric owns eng). Haruko for risk. Limited eng capacity until P1.1 scale and basics close out.

### P4 — Loan & Borrow / Haruko (GREEN)
First loan booked 3/27. Haruko prod instance up: hcad-cls1.prod.haruko.io
**Hackathon offsite week of April 13** — Neil (Haruko, NY, likely Thu/Fri) + Rasmus (SecFin, CS) attending.
Goals: 4 recon layers, loan management E2E, spot trades visible in Haruko. Options + PMS P&L out of scope.
- Haruko onboarding complete: 4 roles set up (Front Office, Risk, Ops, Read) with users mapped.
- **Haruko pushing to production this week (Apr 7 week)**: Spot trade booking for risk mostly complete. Haruko→CLS trade flow dev in progress (trade pushing mostly done, ledger side still needed). Symbology mapping (internal→Haruko) still outstanding.
- **BK→Haruko**: Most flows tested in dev. Main outstanding = reconciliation. Kevin to discuss recon requirements with Jason. Kevin's eng (Wasserman) will build BK↔Haruko recon.
- **Loan ledger implementation**: Moving from definition to implementation. S-FIN service can already create loan legs (cash + crypto). Rasmus + Paul finalizing integration details. Rasmus's team to meet this week to finalize approach.
- Haruko→Olympus→BK (Olympus/SFIN → ledger): Target completion this week.
- **Swap margin**: Will use Haruko as data source for margin calculations — avoids building internally. Yang Wu to coordinate Haruko→Voyager integration (with Yoon Lee from Voyager).
- **Risk team (Ricky, Yang) still disengaged**: Not invited to hackathon offsite. Jason to invite them. They need to set up views in Haruko. Team is live-trading without them.
- **P&L/Studio**: Finance team asking about P&L numbers. Brian Stern starting to look at PMS→Studio integration. Jason to push Brian to document requirements.
- **2 Prime**: $3.8M equity with high leverage — concern raised. Awaiting MLA from their lawyers (no timeline). Yang Wu following up with Bob/Sully.
- Loan structure: bilateral B2B MLA (not repo — avoids MTL requirement); BitGo as custodian; ~7–7.5% cash borrow rate; CS can rehypothecate BTC collateral
- **Margin parameters finalized (Apr 6)**: 50% initial margin, 35% maintenance after day 1. Withdrawal based on lesser of SMA New York or House excess.
- **Haruko PMS integration** (Voyager margin model): Voyager calculates margin calls but needs risk model inputs from Haruko. Waiting on Amit Kirdatt to return from vacation to progress.
- 5 margin systems currently issuing calls simultaneously: Olympus, Bezos, Wrench, Voyager, Haruko

### P5 — Payments
- Inbound (Cubix/Customers Bank): GREEN, Nostro recon in ops validation; incorrect account number found and being corrected
- Outbound: AMBER — payment flow agreed. **Kyriba likely NOT required** — client bank-to-client bank payments don't require AML check. Studio approval workflow being built by tech team. Alignment meeting **4/7** between tech teams; Zip process to be cancelled based on 4/7 outcome. (No Notion notes yet on outcome.)

### ⚠️ NEW RISK: VASP/CARF Registration (Cayman Entities)
Raised at Apr 6 weekly meeting. **Potentially 3-6 month critical path blocker** for Cayman entity bookings.
- Cayman entities may require VASP (Virtual Asset Service Provider) registration — legal opinion from Patrick Wilson expected by Apr 11.
- VASP registration = 3-6 months if required.
- CARF (Crypto Asset Reporting Framework): regulations not published until October; 2026 activity filed in 2027 — can run in parallel, not the immediate blocker.
- **Scope of impact unclear**: Pure US spot trades not touching Cayman = NOT blocked. Offshore hedging via Cayman (e.g., RenGen via Cayman I) = potentially blocked.
- Action: Brian Stern to align with Sully on which specific flows are impacted.
- This has downstream implications for the Cayman entity setup timeline and any derivatives hedging flow that routes through Cayman.

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

### Perpetuals (P2.4) — from PRD (updated Apr 6)
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
