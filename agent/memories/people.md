# People

Key contacts outside Eric's direct team.

## Clear Street Leadership

| Name | Role | Notes |
|------|------|-------|
| Jon Daplyn | COO, Clear Street | Pushing for eventual Pulse/CS tech stack merger; needs proper staffing + compliance work first |
| Brian Stern | COO, Clear Street Digital (new hire) | Needs to document P&L integration requirements; owns finance sign-off on first live loans |
| Brian Oliveira | COO, CS Digital (operational) | Joined ~1 month ago. Introduced at Digital→Netsuite meeting Apr 13. Working on Finance/ops side — bank recon, P&L automation, GL feeds to Netsuite. |

## Digital Assets — Business

| Name | Role | Notes |
|------|------|-------|
| Robert Rutherford ("Bob") | CEO, CS Digital — Eric's direct boss | Hired at acquisition to run the digital team. Day-to-day coordination and operations. |
| Suleyman Duyar ("Suley") | Founder of RenGen; now focused on big-picture business strategy for CS Digital | Was Eric's boss before Bob was hired. Stepped back from coordination/ops to focus on business direction. Trader by background. Not an engineer — proposes solutions from a business/trading lens. Eric's job is to take his wishlist and turn it into a real, viable product. |
| Dalf Hammerich | Entity/ops — Cayman entities, BitGo | Ops owner for digital trades |
| John DiBacco | Derivatives/swap trading desk | |
| Colin Farrell | Digital sales desk (new hire, May 26 2026) | |
| Yang Wu | Credit risk | |
| Atul Pawar | Market risk / derivatives | Made the call to bypass Risk team for initial Haruko integration |
| Ricky Gunawan | Risk | Not currently engaged enough per meeting notes |
| Matt Lusignan | Ops / client onboarding | Responsible for securing Irma company codes for Cayman 1 & 2; defining manual spot crypto onboarding process |
| Christy Moccia | Compliance | Owns OTC options disclosure/disclaimer language (CSD); risk model sign-off coordination (June 9 Swap/Deriv). |
| Christine | Risk / trade limits (business) | Owns OTC option trade-limit (aggregated notional) requirements. June 9: to provide Eric + Chris test cases + spreadsheet examples for limit calcs before Halo coding can proceed. |
| David Brown | Legal | |
| David Martin | CRO, CS Digital | Chief Revenue Officer for digital assets. |
| Andrew Masich | Entity setup / vendor onboarding | |
| Lily Chen | PM — project tracking (Notion portfolio system) | Runs the weekly project tracking spreadsheet |
| Ritesh Chaudhary | EMS/OMS product | |

## Digital Assets — Engineering (non-Eric's-team)

| Name | Role | Notes |
|------|------|-------|
| Jason Price | BK product owner | Weekly DA status meetings, holistic coordination |
| Rama Mellacheruvu | BK engineering lead | |
| Hari | BK engineering | |
| Ankit Singh | BK/CSC eng — BitGo→BK, bank recon | Taking ownership of CaaS (custody/BitGo integrations) as of May 2026. BK is part of CSC. |
| Ani Banerjee | Risk engineering | **Owns the margin rate file, events, and requirements** (per Raja, Apr 24). Primary integration point for anything touching CS-wide margin rate pipeline (RENG → BK → Snowflake). |
| Raja | Derivatives pre/post-trade risk (CS-wide) | Walked Eric through the firm's existing risk architecture Apr 24: FACT (instruments, real-time) + RENG (margin rates, SOD file, event-driven from SQS) feeds pre/post-trade risk; BK = ledger on custody side; Snowflake amalgamates BK + margin rates. Auto-liquidation exists institutional-side only, not retail. |
| Nikhil Kulkarni | FACT / reference data | Setting up listed options instruments manually; co-owns scalable Deribit options integration into Pulse with Eric (Apr 8 action item, conditional on Cayman IRS approval) |
| Collin Zoll / Yoon Lee | Voyager/Athena engineering | |
| Wojciech Baj | Haruko↔Olympus integration | |
| Rasmus | SecFin/S-FIN engineer (CS side) | Quarterly NY visit; attending Apr 13 hackathon |
| Madhu Subbu | SecFin/S-FIN team lead (CS side) | |
| Kevin Stevens | Eng lead, CS Digital (CS-side) — **laid off May 4, 2026** | Reports to Jon Daplyn (traditional CS eng org). Hired pre-acquisition to build crypto at CS — accelerated when Pulse was acquired. Background: Hidden Road (senior eng). Motivated by pre-funding-round equity. Eric and Kevin had developed a strong working relationship despite the potential for org friction. Division of ownership was emerging: Kevin on cash-settled (OTC options, loan/borrow, CaaS/CAST); Eric on crypto-native (Talos interop, LP pipelines, exchange integrations, execution, PMS). **Laid off May 4**. Ownership of cash-settled work (OTC options lifecycle, CAST/CaaS) is now unresolved. CAS Gateway POC Kevin built (BitGo proxy + Chainalysis) now has no clear owner. Kevin's team: Amit Kirdatt (Haruko/CaaS), Wasserman (BK↔Haruko recon). |
| Christopher Davidson | Eric's team — Talos config, Okta, Haruko | |
| Erick Arce | Eric's team — architecture, flow diagrams | |
| Peter Kim | IT / Okta | |

## RenGen-Connected

| Name | Role | Notes |
|------|------|-------|
| Anton Ronis | Head of Quant, CS Digital (under Bob/Suley) — just hired | Based in Israel. Was acting CTO of RenGen when Eric joined Pulse; they worked together to retire RenGen's legacy systems in favor of the Pulse platform. Prior military involvement — can be unavailable for weeks at a time due to the ongoing war. |
| Omer Yilmaz | RenGen FTE + unpaid CS consultant; technically reports to Eric | Still fully employed by RenGen. CS consultant role is essentially a mechanism to get him a CS laptop and access — Eric and RenGen eng teams collaborate closely and this formalizes it. |
| Selman (GitHub: `SelmanB`) | RenGen / CS consultant, same arrangement as Omer | Doing venue-integration work (Coinbase, Ibkr, Coinbase National, Bitso) as of Jul–Aug 2026. |

## CaaS (CAAS MVP project, kicked off Jul 23 2026 — Rama/Ankit Singh's org, not Eric's team)

| Name | Role | Notes |
|------|------|-------|
| Zack Yu | CaaS eng | Action items: verify new account structure with compliance/legal; add enterprise ID + wallet ID on the "Irma" side. |
| Ram Kollengode Kalyanakrishnan | CaaS eng | Manually testing BitGo onboarding APIs to scope automation requirements. |
| Lisa Yen | PM — SSI roadmap | Consolidating SSI (Securities Settlement Instruction) project tasks into a roadmap workbook; looping in Studio team on CaaS. |
| Christie | Compliance | Reviewing/approving KYC requirements for the BitGo digital extension (retail clients). |
| Mammud | Risk/product | Evaluating whether the existing Active-retail risk-check platform should be reused for new retail crypto customers. |
| Raj Patel | (role TBD) | Invited to CAAS MVP meetings per Rama's request (Jul 23) — context not yet established. |
| Cindy Guo | CaaS eng/PM | Surfaced Aug 4 CAAS MVP meeting — scheduling a CSSE wallet-ownership meeting and a wallet breakout session (with Lisa Yen). |

## Digital Ops (loan-booking incident, Jul 31 2026 — not Eric's team)

| Name | Role | Notes |
|------|------|-------|
| Rita | Ops — manual journaling | Handles manual journal corrections for mis-booked loans (e.g. the Jul 31 120.5 BTC / $5M loan-booking error). |
| Anoop Ismail | Ops | Works alongside Ritik Chandak on Parataxis/CaaS operational access and manual booking. |
| David | (role TBD) | Booked the incorrect Jul 31 loan entry; Lily Chen following up to understand why. |
| Aditi Dekhane | Payments (CSC↔CSE) | Owns the AML approval workflow and first-ever CSC↔CSE payments integration; not Eric's team. |

## Vendors / External

| Name | Role |
|------|------|
| Neil | Haruko contact (NY-based); attending Apr 13 hackathon offsite (likely Thu/Fri) |
| Shlomi Avivi | BitGo VM / security setup | Also referenced as "Shalomi" in Aug 4 CAAS MVP notes — Ankit Singh sharing OAuth/MFA design with him for feedback; syncing with Lisa Yen on wallet security/control risk-review minimums. |
| Paul Collins | Olympus product (CS) |
| Timir Naik | BitGo VM / ops coordination | Following up with Shlomi on VM readiness timeline; removed BitGo VM responsibility from Brian Stern |
| Joe Pergola | CS Holdings finance | Lent funds to cover 50% IM margin call on first digital trade (Reg T account issue) |
| Angelo Principato | Margin / risk ops | Confirmed fix for Reg T maintenance margin override — excess funds reflect next morning |

## CS Engineering (Other)

| Name | Role | Notes |
|------|------|-------|
| Annika Wei | CSC (Clearing, Settlement, Custody) team | Authored the "Crypto SSI enhancement" design spec (Apr 7) — defines inbound/outbound wallet address model in ssigate |
| Wasserman | Kevin Stevens' team | Assigned to build BK↔Haruko reconciliation once Jason Price defines requirements |
| Ankur | BK engineering | Working on Qubics/Customers Bank API integration (may be same as Ankit Singh or different person) |
| Amit Kirdatt (akirdatt) | Haruko integration — **now reports to Eric** (as of May 2026) | Owns Haruko integration. Previously owned CaaS (custody/BitGo integrations) but CaaS ownership is moving to Ankit Singh (BK/CSC team). Transferred to Eric's org May 20, 2026 from Rama/BK. May 7 action items still open: (1) clarify Haruko margin model for long call options with business, (2) provide Haruko API endpoint details to Ani, (3) connect Haruko buying power data to Talos (routing through Range, with Chris Davidson). |
| @kvangala | CaaS Gateway — unknown team | Mentioned in May 21 CaaS design review; Rasmus to talk to them about CaaS Gateway interface for account onboarding. Full name unknown. |
| Patrick Wilson | Legal counsel | Providing VASP/CARF legal opinion for Cayman entity registration obligations; expected by ~Apr 11 |
| Stephen Sullivan | Quant | Reviewing quant model inputs for swap margin; update expected this week (Apr 6 action item) |
