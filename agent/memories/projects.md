# Projects / Initiatives

Current delivery roadmap for Digital Assets at Clear Street (as of 2026-04-06).
Sources: "Digital Assets Program Tracker" Google Sheet (~/Downloads CSVs, migrated from "Digital Assets Build" Apr 2026) + Notion meeting notes + Notion project docs.

---

## Phase Summary (updated Apr 20 from tracker)

| Phase | Name | Status | Target |
|-------|------|--------|--------|
| P0 | POC Single Firm Trades | **Complete** | Oct 2025 |
| P1.1 | HT Spot - Principal Execution (manual) | **Complete** | Dec 2025 |
| P1.1 scale | HT Spot - Principal Execution (automated, STP) | **GREEN** — dev complete, P0 items on track | Apr 30, 2026 |
| P1.2 (1.3) | LT - RFQ to LP (Polaris + Talos RFQ to RenGen) | **AMBER** — BK netting unclear if 4/30 achievable | Apr 30, 2026 |
| P1.4 | LT - Front-to-Back Integration (Studio EMS + Active Trader) | **AMBER** | Apr 30, 2026 |
| P2.1 | Crypto Swap (Voyager + Athena + BK) | **Complete** | Mar 31, 2026 |
| P2.2 | Crypto Portfolio Swap | **At Risk** | May 29, 2026 |
| P2.3 | CFTC Swap Dealer Application | **OFF TRACK** | Jun 30, 2026 |
| P2.4a | HT Perp (Swap) Live | Not Started | **May 15, 2026** |
| P2.4b | LT Perp (Swap) Live | Not Started | **Jun 15, 2026** |
| P2.4c | Spreader routing perp orders | Not Started | **Jul 15, 2026** |
| P2.5 | OTC Options - HT Live | **RED** — eng estimate due Apr 21 | **May 15, 2026** (at risk) |
| P2.5b | OTC Options - LT Live | **RED** / Not Started | Jun 1, 2026 |
| P3 | Client Trading & Custody (BitGo CaaS Active) | **AMBER** | Jun 30, 2026 |
| P3b | Client Trading & Custody (BitGo CaaS Institutional) | **AMBER** | Jun 30, 2026 |
| P4 (Loan) | Loan & Borrow via Haruko | **GREEN** — loan creation prod-ready | May 31, 2026 |
| P5a | Stablecoin→USD manual | **COMPLETE** | — |
| P5b | Stablecoin→USD automated | **RED** — eng confirm timeline Apr 20 | TBD |
| P5c | Cross-Entity Margin test trade | **GREEN** — ready, awaiting Julian to update Digital MLA | Apr 29, 2026 |
| P5d | Payments - Cubix/Kyriba | Not Started | Jun 30, 2026 |

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

### P1.3 — LT RFQ to LP (AMBER — updated Apr 21)
Polaris doing RFQ/RFS to RenGen as LP. Talos for post-trade.
- **E2E testing completed** (week of Mar 30).
- **Prod rollout target**: **Apr 24** for Polaris/Talos RFQ.
- **BK netting** (DA-052): obligation logic kicked off; **May 15 confirmed with confidence**. Single trade pair-off almost done; multi-trade greedy algorithm in progress (includes user-editable results). Exec Summary forecast date: **May 15** (slipped from Apr 30).
- BK team had onsite week of Apr 14 to align on open questions.

### P1.4 — LT Front-to-Back (AMBER)
Digital Trade Engine routing RFQ to RenGen → Studio EMS + Active Trader. Apr 30.
- Exec Summary tracker now shows this as AMBER; swaps requirements + resource allocation scheduled for week of Apr 21. Jun 15 target.

### P2.1 — Crypto Swap (Complete)
Voyager + Athena upgraded for digital assets. BK→Athena integration complete. CFTC de minimis threshold tracking built.

### P2.3 — CFTC Swap Dealer Application (AMBER)
Working with Potomac + PWC. ~40% of control gaps in progress, 60% not started. Application target Jun 30 (6-9 month approval timeline). Risk hiring just started.

### P2.5 — OTC Options (RED — updated Apr 21)
CSC (Clearing, Settlement, Custody) team created a formal project entry Apr 10: "Digital Asset Options" (Goal: Support OTC cash-settled crypto options).

**Apr 20 DA Status meeting — major clarification on timelines:**
- **Talos options booking** (Chris Davidson): targeting **~2.5 weeks = ~May 8 prod** (not BK — Talos is the options OMS entry point)
- **BK trade object**: Can use V1 out-of-the-box or more strategic V2. **May 15** target with Chris + Rama + Amit collaborating
- **Expiry handling**: Team will stand up simpler API (not reuse existing ENA expiry process); complexity around rollover timing + all-options-for-a-day expiry
- **Margin calls**: Haruko generates alerts; BK to use existing borrow/loan API for commitments. Open: does Haruko support webhooks?
- **Athena integration**: Should work out of the box for trades + journals (expiries)
- **IM/VM money transfer**: Two parts — source from Haruko, book via BK API. **May 22 dev complete** (with caveats)
- **Back-to-back bookings**: All OTC options transferred to CS Cayman; Cayman entity in BK needs to be stood up with full infrastructure
- **CFTC approach for options**: still TBD — team to determine approach this week
- **Pre-trade risk limits**: Using Talos; Greek limits not yet determined (would require different approach)
- **Deribit integration**: Already complete; custom pricing for options still TBD

**Talos options UI — findings from Chris (Apr 21):**
- "Vanilla Options" tab exists in Talos UI. Linear instruments only for now (not crypto-settled).
- No expiry field on option instrument in Talos — Tenor field is optional and not the right fit.
- Hardcoded European style only — matches our requirement.
- Talos requires an index to be selected for UI pricing — everyone needs to be aware of this.
- Expiry can be set down to the minute when booking a trade.
- **Plan**: create template option without expiry on Talos side; Atlas sets expiry in our UI. **MUST USE ATLAS for HT options booking** (confirmed).
- **Open**: how to add underliers beyond BTC/ETH? Counterparty field blank. Can perps be booked as a Forward in Talos?

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

**Pricing — two separate streams required from Pulse (UPDATED Apr 17 Slack thread):**

**Stream 1: M2M / reference price** (daily marks, margin calls, expiry settlement)
- **Mechanism: Pulse publishes to Kafka topics** — same pattern as any pricing to FACT. Not a special integration; just a matter of where we pull the prices from.
- **Source: Haruko's vol surface → fair market price** (CONFIRMED Apr 21, Bob 1:1 + Suley). Bob and Anton both want 3rd party data source, not internal models. Haruko generates FV from its vol surface. Mechanism: book synthetic trade into test account for bilateral linear option → Haruko returns a price. Chris Davidson has test account. Needs model validation — risk team's job. Future: pull FV from consolidated risk system once all data flows there.
- Do NOT use raw Deribit prices. Suley confirmed concerns: **pin risk at expiry** (OTC expiry times may not converge with Deribit listed expiry times), **price divergence around expiry**, and **interest rate differential** (Deribit uses same-expiry futures as forward proxy, not spot + rate — creates model gap for linear pricing).
- **Expiry/settlement price source — RESOLVED (Apr 23 Options Pricing meeting)**: Deribit index price − strike, using a **30-minute TWAP** (1-minute slices over 30 min period before expiry) to prevent manipulation. Same mechanism Deribit itself uses. This unblocks Eric's eng estimate for expiry work.
- **Hedge vs price relationship**: no direct constrained relationship between hedge price and client-facing price. May be tunable over time but no guarantees. Expected for an OTC dealer.
- **Long-term vision**: unified model between pricing (M2M) and quoting (desk). Validated base model, front-office discretion for markups. Easier from audit/regulatory perspective.

**Stream 2: Quoting / sales price** (desk quotes to clients)
- MVP: **fully manual** — desk quotes by hand, RenGen manually provides quotes and follows up with hedges. No Pulse connectivity to Paradigm/Deribit needed for MVP.
- Phase 1: automated back-to-back RFQ via Atlas/Polaris (zero risk threshold = most efficient path per Suley).
- Phase 3 (future): Polaris generates its own vol surface and pricing model; risk sharing across the book. *This is what the Blockfills guy on Apr 20 built at his previous firm.*
- Not published to FACT. Used only by the desk. Configured in Haruko with CS parameters over time (Bob: can use Haruko's option model day 1).
- Alignment still needed (Bob + Suley + Anton + Eric) on quoting model specifics.

**Execution pipes (MVP → future):**
- MVP: fully manual. No Paradigm/Deribit connectivity required. Only Deribit expiry contracts quoted.
- Phase 1: back-to-back with Deribit and Paradigm (automated RFQ via Polaris at zero risk threshold).
- Phase 3: Polaris risk sharing with full vol surface.
- **Anton's open question (unresolved)**: Is the desk using Haruko to price custom-expiry OTC options without relying on Polaris at all? Eric's answer: high-touch day 1 execution E2E is not yet fully defined. This is what needs to be finalized.

**Alignment needed (Bob, Suley, Anton, Eric — sync early week of Apr 20):**
1. Exact fixing methodology for M2M reference price (which Deribit strikes/expiries to interpolate against)
2. Expiry cutoff convention for bespoke contracts (MVP: use Deribit expiries? Or custom times?)
3. Whether Haruko's model can continuously update from live vol surface inputs (Suley testing)
4. How Paradigm/Deribit fits into execution pipes for Phase 1

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

**Pending action items (updated Apr 17):**
- **Eric + Anton + Bob/Suley**: sync early week of Apr 20 — finalize fixing methodology, expiry convention, Haruko live-update capability, Paradigm/Deribit execution pipe placement
- **Eric (Pulse platform)**:
  1. Refdata: support arbitrary expiry *timestamp* (not just date) in option symbol — Bob confirmed custom expiry times per contract
  2. Refdata: correlate Pulse option instrument definitions with FACT/Haruko/Talos instruments
  3. M2M pricing: pull from Haruko via API, publish to FACT + BK (daily + at expiry)
  4. Expiry: Pulse fires per-contract event at expiry with settlement price → BK triggers settlement workflows
  5. Execution pipes: define how Trade-Engine/Polaris/RenGen handle option contracts from the desk — not yet scoped
- **BK team (Hari/Kevin)**: trade booking ~3 weeks; expiry process ~2 weeks additional
- **Kevin + team**: Haruko→BK margin call API/webhook design; day-1 fallback = manual ops
- **David Sherby**: BK→Core Financial CFTC reporting path (can they piggyback on Voyager's pipes?)
- **Chris + team**: Talos integration for options; instrument setup + refdata ~3 weeks
- **Suley**: test whether Haruko FV model supports continuous live vol surface inputs (real-time vs on-demand)
- **Bob/Suley (decision)**: expiry convention for MVP — use Deribit expiry times (Anton's strong recommendation; avoids vol interpolation complexity) vs. custom times
- **Team**: project plan socialization week of Apr 20

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

### P4 — Loan & Borrow / Haruko (GREEN — updated Apr 21)
First loan booked 3/27. Haruko prod instance up: hcad-cls1.prod.haruko.io
**Hackathon week Apr 13-17 — COMPLETE.** All features built.
- **Apr 20 DA Status**: functionally happy path complete. Haruko integration piece needs final confirmation. Want deletes + settlement functionality before go-live.
- **Go-live target: April 30** (everything from hackathon to prod by end of this week, including trade confirms going out weekend of Apr 19)
- BitGo instructing code mostly complete → rolling out by end of week Apr 25.

**Hackathon demo results (Apr 17 noon):**
- E2E loan creation flow demonstrated: Haruko → Olympus → BK. 7 scenarios tested (all combinations of cash/USDC/BTC for loan + collateral sides). Uncollateralized loans working.
- Loan balances flowing to ledger correctly (USD loan 2.6M→2.7M, BTC collateral 21.86→~24 demonstrated live)
- Spot trade cancel flow working bidirectionally (Talos→BK and BK→Talos via WebSocket)
- Settlement: ops initiates from Ops Portal, flows back to Talos automatically. Rita no longer manually posts settlements.
- RFQ pipeline (Polaris stack, non-Talos) to RenGen demonstrated. Margin checks working (rejection on insufficient margin shown).
- Exchange trade scenarios (BitGo, Coinbase): contractual settlement, no outstanding instructions. Instrument vs currency and coin-to-coin conversions working. Bookings automated.
- Trade confirmations: automated EOD process, email to clients, Studio portal access. Brian's template + legal/compliance disclosure language.
- Custom pricing from Pulse pushed to Haruko every minute.

**Remaining gaps (not demo-ready):**
- Automated collateral settlement recognition from BK (still manual)
- Netting for multiple trade settlement
- Margin flow (attempted but not ready)
- Recall/unwind business processes documented, implementation in progress
- Cash commitments cleanup still manual (crypto auto-cleans)

**Key operational detail**: Borrower type must be set to "Internal" (not OTC) for correct Arma mapping. Active flag: new loans start inactive, must be manually activated after collateral receipt (will be automated — Rita's task for now).

**Hackathon retrospective**: First on-site hackathon was challenging (interruptions, other projects going live). Strong consensus: **next hackathon should be remote off-site**. Business partners (Brian, Suley, Bob) were valuable clarifiers.

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

### VASP/CARF Registration — RESOLVED (Apr 22)
Per Eric (Slack thread): VASP not applicable. No longer a blocker for Cayman entity trading.

### ⚠️ ~~NEW RISK: VASP/CARF Registration (Cayman Entities)~~ — RESOLVED
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
| Robert Rutherford (Bob) | Business lead, digital assets execution + funding |
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

## Blockfills — Potential Acquisition (evaluated Apr 20)

Blockfills is a crypto institutional OMS/trading platform in bankruptcy. CS is considering acquiring.

**Demo verdict (Apr 20, Eric + Anton)**: Underwhelming. Integration lift would outweigh feature benefits — **not a tech play**. If CS proceeds it would be a **people + books play** (talent retention, customer acquisition). Eric is monitoring but stepping back from actively contributing to the acquisition conversation. Not a Talos/Haruko replacement candidate.

Three original rationale pillars: (1) tech stack, (2) people, (3) customer book. Pillar 1 is off the table per Eric's assessment.

---

## Cross-Entity Margin & Stablecoin→USD Flow (Apr 17, 9:30am) — NEW

Whiteboard design session. Full product design for two related workflows:

**Workflow 1: Stablecoin→USD (client deposits stable coin, gets prime cash)**
- Client sends USDC/stable coin to Digital wallet → Digital instructs LLC to credit client's prime account with equivalent cash
- Reverse: client uses PB cash to buy stable coins from Digital, delivered to crypto wallet
- Works with any crypto asset, not just stablecoins; all stablecoins must be Genius Act compliant
- Three counterparties for selling stable coins: BitGo (simultaneous settlement), Circle ($30M/day limit, same-day wire via Customers Bank, AAA risk), OTC (Coinbase, WinterMute)
- Default approach: accumulate and sell in batches, not instantly
- Client must pre-fund stable coins before allocation; timing risk between receiving and converting managed by charging spread
- BMO does not accept crypto flows → Customers Bank (Cubix) used for this workflow; 24/7 instant inter-entity money movement via Cubix

**Technical implementation:**
- Each PB client needs corresponding counterparty account in Digital + dedicated wallet address
- Sweep accounts between Digital and LLC track inter-entity obligations
- MVP: manual approval button before automation (ops clicks to approve allocation)
- Phase 1: once-daily settlement with automated booking
- Phase 2: more frequent / real-time allocation
- Trade books in Digital when client deposits stable coin, triggering sweep account commitments

**Statements**: Separate from LLC and Digital initially; consolidated PDF deferred; Studio provides single view across entities.

**Priority**: T-minus 0.5 — slightly lower than options (T-minus 1). Both in flight simultaneously.

**Open: Workflow 2 (lending: crypto collateral for cash borrowing)** — deferred; follow-up scheduled **Wed Apr 22** (calendar confirmed: "Blocked for Digital: Cross Entity & Collateral Framework" 11am).

**Stablecoin→USD requirements doc published (Apr 17)** — key additions vs. whiteboard notes:
- Default counterparty is Circle (up to $30M/day, same-day wire via Customers Bank)
- Netting process runs continuously to track net cash obligations
- Risk: crediting client before settlement completes puts firm at risk; manual button MVP guards against this
- Stablecoin→USD priority is **T-0.5** (more urgent than options which is T-1); both run simultaneously
- Cross-entity lending workflow ("v1.5") scheduled for next week

**Apr 22 stablecoin meeting — three-trade model confirmed:**
1. Counterparty sells USDC to Digital
2. Digital sells USDC to LLC (USDC → LLC BitGo wallet)
3. LLC settles USD into Digital prime; Digital credits counterparty account

Settlement sequencing: **coin first, then simultaneous bookings** — prevents unfunded client liability. Digital→LLC = payment vs. payment at 4pm; Digital←LLC = delivery vs. payment (Digital delivers cash first). LLC holds USDC inventory with 2% capital haircut; exits by selling back to Digital→market makers.

SSI: each counterparty gets a dedicated USDC deposit address; SSI table maps counterparty↔address. Matching engine enforces exact qty + address on settlement date — quantity mismatch (e.g. 10.1 vs 10.0) = no match, manual resolution.

Dalf concern: synthetically crediting client accounts before real cash — resolved by coin-first sequencing.
@sduyar to align with @aprincipato on timing today.
Cross-entity & collateral framework deferred — Lily to schedule separate call.

**Action items (updated):**
- **Rama + Mahendra**: estimates still pending (cross-entity collateral deferred again)
- **Lily**: schedule cross-entity & collateral follow-up
- **Eric**: connect with exchange gateway team re: Circle/stablecoin conversion flows

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

## Tech Roadmap with Brian Stern (Apr 20 10am)
Brian Stern (COO, Clear Street Digital) reviewing tech roadmap using his spreadsheet. Eric should come prepared on where digital eng is against Phase 1/2/3 milestones.

## Blockfills Tech Demo (Apr 20 11am) — MOVED from Apr 17
Calendar shows "Blockfills tech" at 11am Mon Apr 20 — **moved from Apr 17 1pm** (original slot). Still the first diligence touchpoint for the potential CS acquisition. Eric should come prepared to assess vs. Talos (OMS/RFQ) and Haruko (loan/borrow/risk). No decision made yet.

## Suley's Tech Roadmap (posted Apr 18, ahead of planning call week of Apr 20)

Strategic context: Bob + David + Suley aligned — **perps are the major revenue driver** after core work (spot, options, lending + ongoing ops support). Perp risk noted (could become exchange-traded) but framed as manageable — CS is an OTC swap dealer, there's no shortage of OTC swap dealing. Longer-term: perps collateralized with tokenized assets (stocks, commodities, currencies — today just crypto).

**Three stated goals for 2026:**
1. Smart, fast enough dealing/hedging system for tokens, options, and perps
2. Clients can trade perps on anything; add new perps quickly
3. Clients can use Spreader + Fox River algos for perps

**Roadmap table (Suley's draft, now also in Google Drive "Digital Tech Roadmap - pulse.csv"):**

| Item | Owner | Priority | Notes |
|------|-------|----------|-------|
| Unexpected ops workflow/venue integrations | ? | 1 | |
| Automate options RFQ (back-to-back w/ Paradigm + Deribit) | Anton | 1 | Eric to speak to Raja + Sven about derivs post-trade risk |
| Autoliquidation | Anton/Thill? | 1 | |
| Perps funding rate | Anton/Thill? | 1 | |
| Perps booking | Thill | 1 | |
| **Getting off Talos — time estimate** | **Thill** | **1** | **NEW (Apr 20): Eric to estimate Talos replacement timeline** |
| Spreader | Anton | 2 | To Polaris or Binance depending on perps booking timeline; Eric to speak to Chris D about Talos booking perps + CoinRoutes to Polaris |
| Predictions perps streaming | Anton/Thill? | 2 | |
| Persist OEMS orders (CoinRoutes first, then own system) | Thill | 2 | |
| Options central risk book + legging strategy | Anton | 3 | Suley to play with Paradigm |
| Fox River algos | Thill | 3 | |
| Polaris pre-trade checks for PM Pro | Anton | 4 | |
| Multicasting/cross-exchange | Anton/Thill? | 4 | |

**Eric's note (Apr 18 7:31pm)**: OEMS order management is a natural dependency of perps booking — you need an OEMS to book perp orders, so OEMS must come first. Not a disagreement with Suley's list, just the correct sequencing. On multicast (P4): Eric is not pushing to raise its priority, but wants to be personally involved when it happens — he has deep experience with multicast-based exchange buildouts from prior jobs.

**"Getting off Talos" (P1 in roadmap CSV) — Eric's proposed 3-step migration (Apr 21):**

1. **Migrate external write actions to our services**, which then write to Talos — Talos becomes read-only for the firm. Our systems own the write path.
2. **Move Talos to backup ledger** — our services are authoritative; Talos is a shadow/fallback.
3. **Kill Talos** — clean cutover once we trust our own ledger.

Rationale: graceful migration, no big-bang cutover. Each step is independently valuable and de-risks the next. Blockfills/Marvel ruled out as a shortcut (demo Apr 20 was underwhelming — integration lift > feature benefits). Time estimate still needs to be produced for this 3-step approach.

**Prerequisites for step 1 (what needs to exist before Talos write path can be migrated):**
- **Account onboarding + account management** — must be owned by our services before we can be authoritative
- **Available margin calcs** — must live in our stack, not depend on Talos for this
- **Atlas** — already in flight; handles high-touch desk booking (Estiven's work). This is the booking UI layer that sits in front of whatever the write path becomes.

**Context for Brian Stern meeting (Apr 20 10am)**: Brian's priority is putting timelines on all of the above. Come prepared on what's realistic given current team capacity.

---

## Apr 23 — Options Pricing Methodology Meeting (1pm) — RESOLVED

**Priority list confirmed** (Eric's team, as of Apr 23):
0. Existing spot and loan/borrow maintenance
1. Streaming spot
2. Finish options
3. Perps
(Side: ongoing counterparty/LP integrations)
4. Future roadmap planning

**Expiry settlement — RESOLVED**: Deribit index − strike using 30-min TWAP (1-min slices). Unblocks eng estimate for expiry work.

**M2M source — CONFIRMED**: Haruko vol surface FV. Mechanism = synthetic test-account trade → Haruko price. Chris Davidson owns test account.

**Deribit inverse pricing — NOT appropriate** for linear products. Pin risk + rate model mismatch confirmed.

---

## Apr 24 — Go/No-Go Review Results (Apr 23, May 1 Confirmed)

**May 1 go-live: ALL ENGINEERING TEAMS GREEN.** This is the 7-day rollover infrastructure, not specifically digital assets. Full-firm change enabling weekend (Saturday/Sunday) settlement processing. Digital assets (Kalshi, crypto) are among the first-movers.

**Key decisions from Apr 23 Go/No-Go (10:30am) + "7 day rollover take 2" (2:30pm):**
- Go-live **May 1** confirmed. First rollover: Saturday May 2.
- Sunday May 3 rollover will run at **noon (not 9pm)** — temporary for first month to give ops 4-5 hours Sunday afternoon. Fri/Sat rollovers stay at 9pm. After visibility enhancements complete, reverts to normal schedule.
- **Hard block** on weekend securities postings — BK enforces by settle date. Short-term regression; ops team members who typically work weekends cannot post during this window. Target **June 1** for queued transaction improvement.
- **Reporting: 7-day opt-in** — IRMA flag at org level, unchecked by default. Existing clients unaffected. When a traditional client starts trading digital assets, **entire org** moves to 7-day reporting cycle.
- Kalshi-specific: Sunday rollover at noon extends crypto/Kalshi trading window from 9pm-midnight to 12pm-midnight. Low volume in May; acceptable tradeoff.

**⚠️ Eric action item from Go/No-Go**: "Confirm with Eric Thill about crypto pricing at noon on Sunday." The official Sunday price snapshot shifts to noon. Eric's team needs to ensure crypto prices are captured from exchanges at noon on Sundays (currently Pulse provides pricing to FACT; Sunday prices for Kalshi only normally). Flagged as "needs escalation" in Go/No-Go notes.

**Eric action item from "take 2" meeting**: "Eric to communicate weekend blocking changes to operations team."

**7-day rollover — status by team (all GREEN for May 1):**
- CSC: one more prod deploy this weekend, blocking changes merged
- Studio Reporting: 2-3 PRs ready, ARMA flag in dev/prod
- Finance: NetSuite tested, UK using full files
- Billing: no blockers, daily billing changes in progress
- Esfin, Grinch, XRT, Futures: all green
- ProdEng: green with pending alerting review (may generate noisy alerts on weekends)
- Digital (Kevin): follow-up offline (Eric's team not mentioned as a blocker)

**SECFIN release** (Apr 24): "Link digital trade to contract" (fleet PR #72536). Signal that digital trade↔contract linkage in Fleet is landing.

---

## Apr 23 Week — Current Focus (updated Apr 23 heartbeat)

**Options Pricing Methodology — RESOLVED (Apr 23 1pm)**:
All three open items closed (from Eric's notes in `20260423_options_pricing_chat.md`):
1. **M2M source**: Haruko vol surface FV via synthetic test account trade (Chris Davidson owns test account). Standard Black-76/88 model. Risk team responsible for validation.
2. **Expiry settlement price**: Deribit index − strike using 30-minute TWAP (1-minute slices). Same mechanism as Deribit itself. **Unblocks Eric's eng estimate for expiry work.**
3. **Deribit inverse pricing**: Confirmed NOT appropriate for linear products. Pin risk at expiry, price divergence, and interest rate model mismatch (Deribit uses same-expiry futures as forward proxy, not spot + rate).
- Unified long-term vision: same base model for pricing (M2M) and quoting (desk), with risk-validated base and front-office discretion for markups.
- Priority list confirmed: 0=spot+loan maintenance, 1=streaming spot, 2=finish options, 3=perps.

**Apr 23 calendar — new meeting**: "Low touch swaps" at 4:15pm. Not previously tracked — may relate to Derivatives Swaps workstream (AMBER, Jun 15 target) or perps LT planning.

**Go/No-Go Review (Apr 23 9:30am)**: This is a recurring Thursday slot — confirmed on calendar for both Apr 23 and Apr 30. The May 1 target is still in play; Apr 23 is the first go/no-go check.

**Talgat's new `ClearStreet Account Manager` service** (PR #1955, Apr 23) — initial scaffold. This is likely the account management prereq for Talos migration step 1. Worth tracking as a signal that the Talos migration has started.

**`digital-asset-contract-manager` deployed (Apr 22)** — new SFIN service. Loan creation from Haruko → BK; adding/returning collateral. This automates part of the Haruko→BK loan lifecycle that was previously manual.

**BitGo CaaS Custody — Engineering Handoff Packet published (Apr 23)**:
- Full solution design for P3 custody (Active retail + Institutional/Studio)
- Eric's team owns Core CaaS Service (L-size) — builds #3 (OTC trading via Polaris), #4 (settlement automation), #5 (unified cash)
- Polaris = execution venue; Fleet/BK = system of record for balances
- Open: BitGo org strategy (one org vs two) — consult BitGo before implementing
- Day 1 assets: BTC/ETH/SOL/USDC/USDT. No withdrawals Day 1. Cash-only MVP (no margin).
- Pen test required pre-go-live (infosec confirmed Apr 23, Kevin Stevens)

**Cross-Entity & Collateral Framework (Apr 22 meeting) — KEY DECISIONS**:
- Stablecoin 3-trade + 1 journal entry model confirmed sufficient for eng to start
- Cross-entity money movement (CSD↔Cayman) = **"due from affiliate" account** — no physical wire transfers
- **Eric + Chris Davidson + Rasmus** assigned offline to determine mechanism for pushing CSD cash balances into Talos for pre-trade risk
- Interest on client balances: Billing = long-term system; Jason Price + Aditi investigating Voyager vs Billing
- Suleyman to write DVP/PVP Notion doc and send 3 cross-entity workflows to Rama for netting review
- CSD can post collateral to Cayman and re-hypothecate margin
- SSI: multiple deposit addresses per token confirmed for institutional clients (one address per asset/network for active clients)

**Eric's open action items (as of Apr 23 EOD):**
1. **Push CSD cash balances → Talos** (pre-trade risk for options) — offline w/ Chris Davidson + Rasmus (from Apr 22 meeting)
2. **"Getting off Talos" time estimate** — P1 roadmap, still pending
3. Connect with Yoon Lee on Talos→Voyager integration for perps
4. Connect with exchange gateway team on Circle/stablecoin conversion flows
5. Respond to Suley's chat (Talos integration details + Cayman swap: Voyager vs Haruko)
6. **Fri Apr 24 1:30pm Eric/Raja** — pre/post-trade risk for derivs (options RFQ automation context)
7. Investigate client trading restriction feasibility short-term vs long-term (Rama to reach out)
8. **Options eng estimate** — expiry settlement now unblocked (TWAP resolved Apr 23). Can now produce estimate.

**This week's remaining meetings:**
- **Fri Apr 24**: Eng Lunch & Learn 11am (AI dev workflow showcase — Eric presenting), AWS 12:30pm, **Eric/Raja 1:30pm**
- **Mon Apr 27**: Brian Stern roadmap 9am, **Buying power/pre-trade architecture 11am**, Bob 1:1 11:30am, DA Status 1pm
- **Tue Apr 28**: Tech Monthly Open Forum 9am, Dev Sync 10am, FACT requirement for Swap Perp 11am, CS Digital weekly 1:30pm
- **Wed Apr 29**: Atakan/Aksel 9:30am
- **Thu Apr 30**: Go/No-Go Review 9:30am (final check before May 1), Dev Sync 10am, Eng Leads Sync 11:30am

---

## Apr 22 Week — Current Focus (updated Apr 22 EOD heartbeat)

**VASP/CARF legal opinion**: Patrick Wilson / Ogiers call was Apr 21 — should close by end of this week from legal perspective.

**Weekend rollover go-live: May 1** — confirmed in Notion (Apr 21 Client Comms meeting). Controlled rollout. Clients on 24/7 products (Kalshi, crypto) get weekend reports; traditional securities clients see no change. System built to support 24/7 capability long-term. May be related to the Thu Apr 23 Go/No-Go at 9:30am.

**Haruko loan creation going live this weekend (Apr 26)** — confirmed in PnL Dashboard meeting (Apr 21). Data will flow all the way to Fleet/BK. Next week: test loan to verify data flow and P&L calculation.

**Trade-by-trade P&L (new)**: Bob (Robert Rutherford) drove this at the Apr 21 PnL Dashboard meeting. Plan:
- Stamp transaction ID into every trade in Pulse linking client trade to its hedge
- Downstream: Snowflake groups by transaction ID for granular P&L
- Two scenarios: (1) immediate delta hedge (80% of trades) — link 1:1; (2) book to risk account and work out later
- Erick's #1901 (Apr 21) "Stamp secondary ids for Talos" is the Pulse implementation
- Action: Robert to talk to Pulse team (likely Eric) about adding transaction identifiers
- Parallel: Lily to confirm Haruko loan/borrow data into Snowflake timeline; Diana to walk through Fleet rec with Robert

**Digital Assets Tax Discussions (Apr 21)** — Patrick Wilson + Lily Chen + Brian Stern meeting. Key points:
- CS operates as **principal**, not agent — avoids "digital asset broker" regulatory definition
- CT entity handles all US transactions; NY entity reserved/dormant
- Cayman 1 = non-VASP hedging/exchange (not client-facing); Cayman 2 = VASP, future international clients
- 1099-DA: 2025 = gross proceeds only; 2026+ includes cost basis
- Complex: multi-broker scenarios, USDC→BTC conversions create cost basis situations
- Patrick Wilson to work with Lily Chen + Brian Stern on transaction diagrams
- Income reporting regulations (staking, lending) expected by end of 2026 or early 2027

**CME futures CQG desk integration: GOING LIVE** — confirmed in Apr 20 DA Status (CSC notes). Not previously tracked as near-term.

**OTC options full prod target: May 22** — confirmed in CSC Apr 20 meeting notes (BK trade object + Haruko + expiry). Previously captured as individual milestones; May 22 is the full-stack production target.

**Stablecoin cross-entity prioritized over options** — Apr 20 DA Status decision: prioritize estimating stable coin cross-entity flow first due to higher business value. Rama/Mahendra estimates still pending.

**Eric's open action items this week (updated Apr 22 EOD):**
1. Connect with Yoon Lee on Talos→Voyager integration for perps
2. Produce "getting off Talos" time estimate (P1 roadmap)
3. Thu Apr 23 1pm Options Pricing Methodology — resolve (a) expiry convention, (b) fixing methodology, (c) Haruko live vol surface
4. Connect with exchange gateway team on Circle/stablecoin conversion flows
5. Respond to Suley's chat invite (Talos integration details + Cayman swap: Voyager vs Haruko)
6. Talk to Raja about pre/post-trade risk — Fri Apr 24 1:30pm ("Eric / Raja")
7. **NEW (from Apr 21 Rama/Bob/Suley Options catchup)**: Investigate short-term vs long-term feasibility of client trading restrictions when margin/premium isn't delivered (event of default question)
8. **Mon Apr 27 11am**: "DSDigital: Confirm buying power/pre-trade limit architecture" — NEW meeting on calendar; directly tied to Anton's polaris pre-trade risk gate (#429) landing today

**This week's key meetings (updated Apr 22 EOD):**
- **Wed Apr 22**: Eric 9:30am (1:1), Atakan/Aksel 9:30am, Cross-Entity & Collateral Framework 10am (lending), Doctor 11:45am, FACT requirement for Swap Perp 2pm
- **Thu Apr 23**: **Go/No-Go Review 9:30am (May 1 go-live)**, Dev Sync 10am, **Options Pricing Methodology 1pm**, Chat with Vince 2pm
- **Fri Apr 24**: Eng Lunch & Learn 11am (AI dev workflow showcase), AWS Office Hours 12:30pm, **Eric / Raja 1:30pm** (pre/post-trade risk for options/derivs)
- **Mon Apr 27**: Brian Stern roadmap 9am (recurring), **DSDigital: Confirm buying power/pre-trade limit architecture 11am** (NEW), Bob 1:1 11:30am, DA Status 1pm
- **Tue Apr 28**: Tech Monthly Open Forum 9am, Digital Dev Sync 10am, FACT requirement for Swap Perp 11am, CS Digital weekly 1:30pm, Gamma Booking 1:30pm (conference room reservation)
- **Wed Apr 29**: Atakan/Aksel 9:30am

**"Gamma Booking" (Tue Apr 28 1:30pm)** — conference room reservation (Gamma = room in Lisle office). Not a substantive meeting.

---

## New Developments — Apr 22 EOD

### BK Incident: Wrong Fees on ~70k Trades (Apr 21, Sev1)
A new bkgate version deployed at 4:31pm switched from legacy rates service to tp-rates. Bug: bkgate double-multiplied fees (by price *and* notional) due to a rate type interpretation mismatch. ~70k trades were booked with wrong sec/taf/orf fees. Rolled back within ~1 hour; remediation script ran through ~8:30pm. Ops team detected it. Root cause: bad data interpretation when switching fee data sources without validating output correctness. Action items: better communicate roll-forwards as announcements; validate data equivalence before switching sources. **Not Eric's team's issue** (BK/CSC teams only), but worth knowing since digital trades flow through BK.

### Bitcoin Depository Receipt (BTCDR) — New Client Opportunity (Apr 21)
David Martin (CSC) pitched a workflow to do a ~$1M proof-of-concept BTCDR trade with client UTXO (account 116206) before David speaks at a Bitcoin conference in Vegas Mon Apr 28. BTCDRs mirror ADRs — BTC held in TradFi infrastructure (DTCC-settled, CUSIP-assigned, no management fees). Flow: CS Digital buys BTC → delivers to Anchorage → Broadridge issues DR shares via DWAC → T+1 settlement. Many open questions: booking model (Digital→LLC→client), legal review needed, compliance/ORF reporting TBD. **Not Eric's primary concern** but CS Digital is the execution/pricing leg of this.

### Options Detail: Rama/Bob/Suley Catchup (Apr 21)
New clarity on options operational questions:
- **Client trading restrictions**: Failure to deliver margin/premium = event of default after cure period. Team has flexibility to restrict trading. **Eric action item**: investigate feasibility short-term vs long-term.
- **Options structure**: Bilateral (counterparty model), not cleared. CS short, client long. Positions remain on books until expiry (like swaps, unlike spot BTC).
- **Cash segregation**: CSD has existing reserve calc — balances flow to treasury, algorithm locks capital into segregated accounts weekly. Need to confirm if this works for derivatives.
- **Liquidation**: Sell option into market; all fees/slippage charged to client. Need liquidation runbook + booking model.
- **Interest on posted collateral**: Billing system can handle (calculates interest on long balances). Need to feed derivatives margin data into billing.
- **Statements**: No easy consolidation yet — Voyager handles swaps, separate system for options. Short-term: stitch PDFs. Decision: Rama + Yoon Lee to determine.
- **Tax**: Forms needed (1099-IN, 1099-TA, 1099-S, 871-M). Currently manual; TallyX automation project in progress but not top priority.

### CAAS Flow Design (Apr 22, published)
Design doc published for BitGo CaaS client wallet architecture. Key details:
- KYC: Plan A = CS does own KYC, BitGo does rubber stamp; Plan B = full BitGo async KYC (seconds for retail, days for institutional).
- Wallet creation: CS generates key, stores keychain in Vault, whitelists CS↔client wallets. Upstream gets wallet address stored as SSI.
- Internal CAAS Gateway routes all BitGo API calls. Chainanalysis invoked per transfer. Events fired (webhook/kafka) if score exceeds limits.
- Org structure: separate BitGo orgs for Institutional (bespoke policies, high limits) and Active (uniform policies).
- Pre-trade check gap: BitGo does NOT expose how close you are to daily limits — cannot use for pre-trade risk. Must track separately.
- Scope by team: COPS (L), Digital/Eric's team (L), Active (L), Studio (L), IRMA (S), Risk (S), CSC/BK (S).
- **Eric's team (Digital)**: owns the CAAS Service integrating BitGo/Chainanalysis — this is the P3 custody build.
- **Infosec alignment — COMPLETE (Apr 23, Kevin Stevens)**: Separate Vault instance (Kevin + infra), pen test required pre-go-live, clean slate standard (no critical vulns), enhanced monitoring for irregular access, existing auth + K8s deployment approved. Pen test is on the pre-go-live critical path.

## Apr 21 Week — Current Focus (updated Apr 21)

**CARF/VASP legal opinion**: Patrick Wilson had call with Ogiers Apr 21 to finalize guidance (misinterpreted facts were the delay). Should close by end of this week from legal perspective. Still critical blocker for Cayman entity trading.

**Cayman entities in IRMA**: Team setting up today (Apr 20) pending final internal approval.

**Reconciliation**: Big open question — trade-by-trade vs position-based? Jason (BK) suggested position-based; Brian suggested 3-way recon. Sidebar scheduled (Jason + Brian + Lily + Haros from Haruko). Talos data currently JSON, needs flattening. Talos recon is behind.

**Eric's open action items this week:**
1. Connect with Yoon Lee on Talos→Voyager integration for perps (action item from Apr 20 perps call)
2. Produce "getting off Talos" time estimate (P1 roadmap item — Blockfills context relevant)
3. Options alignment: expiry convention, fixing methodology, Haruko live vol (Thu Apr 24 1pm: Options Pricing Methodology meeting on calendar)
4. Connect with exchange gateway team on Circle/stablecoin conversion flows
5. Respond to Suley's chat invite (Talos integration details + Cayman swap: Voyager vs Haruko)

**This week's key meetings:**
- **Tue Apr 22**: Plan for Perps Workflow 9am, Sync on Talos 9:30am, Dev Sync 10am, Eric/Bob 1:1 10:30am, FACT requirement for Swap Perp noon, CS Digital weekly 1:30pm
- **Wed Apr 22**: Atakan/Aksel 1:1 9:30am, Cross-Entity & Collateral Framework 10am (lending workflow)
- **Thu Apr 23**: **Go/No-Go Review 9:30am (May 1 go-live)**, Dev Sync 10am, **Options Pricing Methodology 1pm** (NEW — not previously on calendar)
- **Fri Apr 24**: Eng Lunch & Learn 11am (AI dev workflow showcase)

**VASP legal opinion**: decision expected end of week (Patrick / Ogiers call Apr 21)
**Haruko to prod**: target April 30 (all hackathon features)
**BK options booking (Talos side, Chris Davidson)**: ~May 8
**BK trade object for options**: May 15 (Chris + Rama + Amit)
**Options IM/VM money transfer**: May 22 dev complete

**Options system stack (confirmed from CSC Notion page, Apr 16):**

| System | Role |
|--------|------|
| Talos | Trader manually inputs client-facing trade |
| BK | Books all 4 bilateral legs |
| Haruko | Daily MTM, margin calls, risk |
| **Vera** | **Bilateral option pricing (desk quoting tool)** |
| Pulse | Publishes Deribit reference price + final fixing price at expiry |
| Core Financial | CFTC reporting |
| Deribit | Reference price source for MTM |

**Vera is a CS internal system** (not Haruko's FV model, not a vendor). It sits in the desk quoting/pricing layer — the desk uses it to price OTC options bilaterally. Likely builds on Deribit order book markups initially, proprietary vol surface longer-term. ActAnt was mentioned as an alternative in earlier scoping notes. **Pulse is upstream of Vera** — Pulse supplies Deribit index/options data; Vera consumes it. Pulse does not integrate with Vera directly.

**Apr 22 Lily Slack summary — new options clarity:**

- **Premium**: debited from client CSD account at trade time; reduces buying power immediately
- **Pre-trade risk**: need mechanism to push cash balance events to Talos; long-term = Haruko as single source. Action: Lily to host call (Eric + Ani + Rama + Chris Davidson + Rasmus + Amit Kirdatt)
- **Liquidation**: treated as a trade (not expiry). CSD books opposite-side trade at market + costs; CSD captures spread; can result in debit balance
- **Interest on cash**: open — Billing vs. Haruko vs. Voyager. Separate call needed
- **Statements**: merge Voyager + options statements? Rama + Yoon Lee to decide
- **Tax/1099**: Patrick Wilson to advise on cost basis for early-terminated options
- **Instruments**: same contract terms for CSD↔Cayman hedge as client trade; margin rates differ and are configured separately in Haruko
- **Cross-entity deferred**: not covered today; Lily to schedule follow-up

**Eric's "calculate option pricing methodology" action item** = specifically what Pulse publishes at expiry as the fixing price, not building pricing logic in Pulse itself. Robert Rutherford + 4WTC Copernicus to define fixing price source offline.

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

### Perpetuals (P2.4) — Cash Flows & Booking Design (Apr 22 — new doc)

New Notion doc published: "Perp (Client ↔ CSD) — Cash Flows & Booking (Daily Reset)" (https://www.notion.so/fa2d0eab81494366b9b724d6d9b26069)

**Compact cash flow model (client Prime account):**
| Date | Event | Client cash | CSD cash |
|------|-------|-------------|----------|
| T0 | Client buys perp from CSD | No cash | No cash |
| T+1 | Client posts IM | Prime → CSD: IM posted | Receives IM |
| T+2 | VM due for T+1 mark up | CSD → Prime: VM paid | Pays VM |
| T+3 | Client sells (unwind) | CSD → Prime: Unwind P&L + interest − VM already paid | Pays net |

**Key design decision: daily reset model**
- VM and realized P&L up to daily reset time can be re-used as margin for new trades (subject to house limits)
- After reset, open perp is re-marked to new level for future P&L accrual

**CSD booking (principal to client):**
- T0: position established, no cash
- T+1: Dr Cash (IM collateral), Cr IM collateral liability
- T+2: Dr VM/MtM P&L, Cr Cash (VM paid to Prime)
- T+3 unwind: Dr Realized P&L + interest, Cr Cash (net: Unwind P&L + interest − VM paid)
- IM release: Dr IM collateral liability, Cr Cash

**LLC booking (Prime broker perspective):**
- Client cash flows settle into client's Prime account at LLC; LLC exchanges with CSD via intercompany receivable/payable
- IM: Cr Client cash, Dr Due from CSD
- VM: Dr Client cash, Cr Due to/from CSD
- Close-out: LLC receives net from CSD, credits client Prime
- IM return: Dr Client cash, Cr Due from CSD

**Implication for Pulse/eng**: Pulse needs to generate the T0 trade, and downstream the daily reset + VM/IM settlement flows need to be bookable (BK/Voyager). Funding rate snapshots (0 UTC, 8am UTC, 4pm UTC) tie to VM calculations. This doc formalizes the accounting model for what's in the perps PRD.

### Perpetuals (P2.4) — Requirements defined (Apr 20, confirmed in Notion)

Formal dates:
- **HT Perp Live**: May 15, 2026 — manual entry, Talos
- **LT Perp Live**: ~mid/late June (2 weeks after HT) — FIX protocol
- **Spreader routing**: Jul 15, 2026

Call attendees: Robert Rutherford, Suley Duyar, Brian Stern, Yoon Lee, Collin Zoll, David Sherby.

**Action items from Apr 20 "Review swap perps" meeting (Notion):**
- Suley to open chat with Yoon + Eric Thill on Talos integration details
- Suley to connect with Eric on Cayman swap booking: Voyager vs Haruko (open decision)
- Engineering (Eric) to provide timeline for manual booking capability in Voyager with funding calculator
- FACT team meeting needed: M2M calcs + funding rate integration
- Engineering to determine feasibility of true intraday funding calcs (3x daily snapshot complexity)
- Eng to confirm FIX protocol spec + docs for booking trades
- Team to create comprehensive trade flow diagram with full entity structure
- CFTC reporting automation: discuss with Core on volume capacity
- **Open decision**: Cayman 1 swap — book in both Voyager and Haruko, or just one system?

**From Apr 20 Suley/Brian/Anton planning meeting:**
- Eric to talk to Raja about pre/post-trade risk (derivs context)
- Eric to speak to Chris D about Talos perps booking + CoinRoutes to Polaris
- Someone to start Paradigm integration (not yet assigned)
- CME perps: CFTC framework in progress; CS may want CME as a route (likely Polaris, not client flow)
- Pre-market trading demand (SpaceX etc.) — CS can aggregate liquidity better than CME; relevant for Polaris longer-term

**P&L / trade-to-hedge correlation (Bob 1:1, Apr 21):**
- Bob wants trade-by-trade PnL, tying client trades to hedges 1:1 for now
- Longer-term: unhedged risk books to risk account; unrealized gains/losses tracked there
- Stamp trade ID into Polaris for offsetting position reporting — Akshay involved
- Need to correlate offsetting trade + client trade: still "easier said than done"

**Product:**
- No expiry; use year **2199** for CFTC reporting
- HT: 20-50 orders/day. LT: high-freq, ~$10M trades broken into $500k lots

**Funding rate mechanism:**
- Snapshot-based: **0 UTC, 8am UTC, 4pm UTC** (3x daily)
- Only charged if position held at snapshot time; intraday round-trips not charged
- Interest on net settled position only (same-day trades netted)
- Custom benchmark rates fed to system; M2M accrues funding for early exits

**Trade flow: Talos → Voyager → Athena**
- **Two back-to-back swaps per client trade:**
  1. Client-facing swap (CSDerivatives entity)
  2. Offsetting hedge: CSDerivatives → Cayman I
- Both booked in Talos → Voyager; hedge is 100% swap-to-swap, no physical hedge

**Risk:**
- CSDerivatives → Athena (both legs visible)
- Cayman I → Haruko
- **Voyager → Haruko feed needed** (not yet built; newly added to tracker as TBD)

**Pricing architecture (confirmed Apr 21):**
- **Pulse → FACT → rest of firm** is the canonical crypto mark price pipeline. Pulse is the source of truth for crypto pricing firm-wide.
- Specific mark price methodology (how Pulse calculates the benchmark/funding rate) still TBD — Lily chasing down requirements (Eric asked Apr 21).
- FACT needs real-time API access (current Snowflake path ~15 min delay is insufficient for snapshot-time funding calcs).
- Streaming prices needed for market value calcs at 0 UTC / 8am UTC / 4pm UTC snapshot times.

**Technical open questions:**
- Is 4pm EOD processing sufficient or true intraday snapshots needed?
- Intraday funding calc complexity — eng to assess
- Voyager perf improvements targeting end of Q2; current volume fine for HT

**CFTC reporting:** manual now; automation required for LT volume

**Eric's action item: connect with Yoon Lee on Talos→Voyager integration details.**

Eric owns perps booking (Thill, P1 on roadmap). OEMS is a hard dependency that must come first.

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
