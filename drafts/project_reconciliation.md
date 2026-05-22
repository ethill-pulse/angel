# Trade & Position Reconciliation

## What We're Building

Reconciliation is how we verify that every system that's supposed to know about a trade actually knows about it, and that all the numbers agree. Without it, we can't trust our risk views, our client statements, or our regulatory reporting.

Four reconciliation layers are needed for the digital asset business. They operate at different granularities and serve different purposes.

---

## The Four Layers

### 1. Talos ↔ BK (Front/Back Office Recon)

Talos is the OMS (front office). BK is the ledger (back office). Every trade that's accepted in Talos should have a corresponding booking in BK. If a trade is canceled in Talos, it should be canceled in BK. If BK settles a trade, Talos should know.

The `clearstreet-trade-updater` service (Kafka consumer on `csc.bk.trades.v2.updated`) handles the BK→Talos direction: settlement and cancellation events from BK sync back to Talos automatically. The Talos→BK direction happens via the normal trade flow.

Recon for this layer is a trade-for-trade join by order ID. If the IDs match and the state matches, the trade is reconciled.

### 2. BK ↔ BitGo (Custody Recon)

BK knows what trades happened and what settlements are expected. BitGo knows what coins actually moved. These should agree.

The build here is a daily API job: pull the day's transactions from BitGo, structure them into Snowflake, and join against BK's expected settlement records. Mismatches flag for manual review.

Today this is fully manual — ops pulls BitGo statements and compares against the BK ledger by hand.

### 3. Pulse ↔ Exchanges (Execution Recon)

Pulse executes trades on Deribit, Binance, Kalshi, etc. The exchange's record of what filled, at what price and quantity, should match what Pulse recorded. This layer catches execution bugs, venue API issues, and discrepancies in how fill reports are parsed.

This is not yet built. It's structurally the same as any standard exchange recon — pull fills from the exchange API, compare against Pulse's internal execution log.

### 4. BK ↔ Haruko (Risk Recon)

BK is the source of truth for positions (it's the ledger). Haruko is the risk system (it tracks those same positions for M2M, margin, and risk reporting). They should agree.

BK is authoritative — if they disagree, BK wins. The recon job catches drift introduced by missed Kafka messages, reprocessing events, or Haruko import errors.

---

## Where Data Lives

All reconciliation ultimately flows to **Snowflake** as the analytical and reporting layer. The plan:

- **Talos→Snowflake:** currently a JSON blob; needs to be flattened into a structured schema
- **BitGo→Snowflake:** daily API job (in progress)
- **Haruko→Snowflake:** Amit Kirdatt piping this; not yet live
- **BK (via Fleet):** BK is the ledger; Fleet is the abstraction; both feed Snowflake

---

## Street-Side Confirmation Recon

OTC trades (options, bilateral spot) are negotiated via Slack, Telegram, and Bloomberg chat. The "confirmation" of the trade is a message in one of those channels. CFTC requires that OTC positions be reconciled against counterparty confirmations daily.

The MVP approach is manual negative confirmation: ops reviews the open position list, compares against comms, and flags any discrepancy within a 12-hour window. Long-term, this could be automated via screenshot parsing or a Studio approval workflow — but that's not in scope yet.

---

## Systems Involved

| System | What It Does in This Context |
|--------|------------------------------|
| Talos | Front-office source of truth for trade state |
| BK / Fleet | Back-office source of truth for settled positions and ledger |
| BitGo | Custody source of truth for actual coin movements |
| Haruko | Risk system that must stay in sync with BK positions |
| Snowflake | Analytical layer; where all recon joins are run |
| clearstreet-trade-updater | Kafka consumer that syncs BK→Talos for cancellations/settlements |

---

## Further Reading

- [Notion: Recon Requirements (Apr 29)](https://www.notion.so/3511043d19d580da9b0ce1dd619c426f)
- [Notion: Confirm Recon Requirement (Apr 25)](https://www.notion.so/34f1043d19d580b982e1e5ae05e8427c)
