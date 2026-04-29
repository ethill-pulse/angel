# OTC Options — Pulse Eng Estimate
*Draft — Eric Thill, Apr 2026*

---

## Scope

This estimate covers the Pulse-side work required to support HT OTC Options live (P2.5, target May 30). It does not cover BK booking, Talos instrument setup, or Haruko configuration — those are tracked separately.

Pulse's role in the options stack:
- Publish Deribit reference data (options chains, index price) to FACT and downstream consumers
- Publish M2M pricing (Haruko FV) to FACT + BK daily
- Fire per-contract expiry event with settlement price → BK triggers settlement workflows
- Push CSD account cash balances → Talos for pre-trade risk (buying power)
- Instrument refdata: support arbitrary expiry timestamp and correlate with FACT/Haruko/Talos

---

## Work Items

### 1. Deribit options refdata — options chains as a primitive
**Owner**: Atakan + Aksel (in progress, PR #1933 open)
**What**: Options chain type in Pulse refdata — subscribe to a full chain per asset/venue rather than enabling instruments one-by-one. Publishes chain data to FACT so downstream systems (Haruko, Vera, Talos) have consistent instrument definitions.
**Why it's a blocker**: Manual per-instrument enablement doesn't scale past a handful of strikes/expiries. FACT needs the chain data to build instrument definitions that correlate across Pulse/FACT/Haruko/Talos.
**Known complexity**: Schema changes across refdata layer; Deribit API integration for chain enumeration; instrument correlation logic (Pulse instrument ID ↔ FACT ↔ Haruko ↔ Talos).
**Estimate**: 1–2 weeks (Atakan driving, Aksel supporting; #1933 is already open and in review)

---

### 2. Expiry timestamp support in option symbology
**Owner**: Eric / whoever owns refdata
**What**: Option instruments currently support expiry *date* only. OTC contracts have custom expiry *times* (e.g., 3pm EST on a specific date). Need to store and propagate a full UTC timestamp — through Pulse instrument definitions, into FACT, and into the expiry event.
**Estimate**: 1–3 days (schema change + propagation; low complexity, high blast radius — touches all instrument definitions)

---

### 3. Deribit index price feed
**Owner**: Atakan + Aksel (adjacent to #1933)
**What**: Pulse already publishes Deribit mark prices. Needs to publish the **Deribit index price** specifically (the underlying index, not the option contract price) — this is what the 30-min TWAP at expiry runs against.
**Status**: May already be in flight with the options chain work. Verify with Atakan.
**Estimate**: 2–3 days if not already included in #1933

---

### 4. Expiry event + settlement price calculation (TWAP)
**Owner**: Eric or Atakan/Aksel
**What**: At option expiry time, Pulse:
1. Computes the settlement price — Deribit index price − strike, using a 30-minute TWAP (1-minute slices, same mechanism Deribit uses)
2. Fires a Kafka event with: instrument ID, expiry timestamp, settlement price, underlying index TWAP
3. BK consumes this event to trigger cash settlement journals

**Dependencies**: Deribit index feed (item 3), expiry timestamp in refdata (item 2). Pulse needs to know which contracts are expiring — either driven by a scheduled check against live instruments or an inbound trigger from ops/Talos.

**Known unknowns**:
- Does Pulse poll for expiry or does something else trigger it? (Assume Pulse owns the timer, checks instrument expiry timestamps)
- How does Pulse know about all open OTC contracts at any given time? (Needs to consume or be notified of live option instruments — probably from Talos via existing trade/instrument feed)
- 30-min TWAP requires Pulse to be collecting Deribit index prices at 1-minute intervals for the window. Is that already happening? If not, need to add a timestamped price buffer.

**Estimate**: 1–2 weeks
- TWAP accumulation / calculation: 3–5 days
- Kafka expiry event schema + publishing: 2–3 days
- Integration testing with BK consumer: 2–3 days (coordination with Rama/Chris)

---

### 5. M2M pricing — Haruko FV → Kafka → FACT + BK
**Owner**: Chris Davidson (has the Haruko test account) or Emre (owns Haruko venue integration)
**What**: Daily, Pulse calls Haruko's pricing API to fetch fair value for each live OTC option contract, then publishes to Kafka (same pattern as any pricing to FACT). BK consumes for MTM journals. FACT consumes for daily marks.
**Mechanism**: Book a synthetic test trade into Chris's Haruko test account for each contract → Haruko returns a fair value price from its vol surface (Black-76/88). Pull daily, or on demand pre-close.
**Known unknowns**:
- Does Haruko have a batch pricing endpoint, or does each contract require a separate synthetic trade call?
- Rate limits / latency on Haruko pricing API at scale (dozens of contracts → manageable; hundreds → need to know)
- Does this need to be real-time (continuous) or scheduled (once daily + at expiry)?

**Estimate**: 1–2 weeks
- Haruko pricing API integration: 3–5 days
- Kafka publishing (existing pattern): 1–2 days
- FACT/BK consumer validation: 2–3 days (coordination)

---

### 6. CSD cash balances → Talos (pre-trade risk / buying power)
**Owner**: Chris Davidson + Rasmus (offline design in progress); Ani Banerjee is the integration point on the CS risk side
**What**: Talos needs to know the client's available cash (CSD account balance) to run pre-trade checks on option premiums. Currently Talos doesn't receive cash balance events from CS. Mechanism TBD (Eric + Chris + Rasmus offline).
**Dependencies**: Call with Ani Banerjee, Rama, Rasmus, Amit Kirdatt (Lily to schedule). Design not yet locked.

**Known unknowns**:
- What API/event mechanism does Talos accept for cash balance updates? Push (Kafka/webhook) or pull (Talos polls)?
- Does Pulse own this feed, or does BK/Fleet own it and Pulse just needs to wire it?
- How frequently do balances need to update? (Real-time? SOD + intraday events?)

**Estimate**: Cannot estimate until design call with Ani. Likely 1–2 weeks once mechanism is locked.
**Risk**: This is the loosest item. If the mechanism requires net-new infrastructure (new Kafka topic, new BK feed, new Talos API integration), the estimate grows. Flag to Lily to prioritize scheduling this call.

---

## Summary Table

| # | Work Item | Owner | Estimate | Blocker? |
|---|-----------|-------|----------|----------|
| 1 | Options chains refdata primitive | Atakan/Aksel | 1–2 wks | Yes — feeds items 2, 3, 4 |
| 2 | Expiry timestamp in symbology | TBD | 1–3 days | Yes — feeds item 4 |
| 3 | Deribit index price feed | Atakan/Aksel | 2–3 days | Yes — feeds item 4 |
| 4 | Expiry event + TWAP settlement calc | TBD | 1–2 wks | Yes — critical path |
| 5 | M2M pricing (Haruko FV → Kafka) | Chris/Emre | 1–2 wks | No — parallel |
| 6 | CSD cash balances → Talos | Chris/Rasmus | 1–2 wks* | No — parallel |

*Item 6 estimate contingent on design call with Ani Banerjee.

---

## Critical Path

Items 1 → 3 → 4 are sequential dependencies. The minimum time from now to a working expiry event in Pulse is roughly:

- Refdata schema work (item 1 + 2): ~2 weeks (partly in flight)
- Index price feed (item 3): ~3 days, can overlap with tail of item 1
- TWAP + expiry event (item 4): ~2 weeks, starts when items 2+3 land

**Critical path total: ~4–5 weeks from now** → puts Pulse-side expiry capability at late May / early June.

Items 5 and 6 run in parallel and don't gate expiry, but both gate a live first trade (BK needs M2M prices; Talos needs buying power feed to approve pre-trade).

---

## What's Not In Scope (Pulse)

- Talos instrument setup and options template configuration (Chris Davidson)
- BK trade booking, clearing method, and transfer/allocation trade logic (Rama's team)
- Haruko margin configuration per contract (ops)
- Atlas UI expiry field on option booking (Estiven, likely small)
- Pre-trade risk calculation methodology (Risk team / Atul Pawar / Ani Banerjee)
- CFTC reporting via Core Financial (David Sherby)

---

## Open Questions Before Finalizing

1. **Who owns the expiry timer in Pulse?** Does Pulse self-schedule against instrument expiry timestamps, or does an external signal (Talos, ops) trigger the expiry event? This affects item 4 design significantly.
2. **Haruko pricing API shape**: batch or per-contract? Need Chris Davidson to confirm based on test account experience.
3. **Buying power mechanism** (item 6): What does Talos accept? Eric + Chris + Rasmus need to close the design and loop in Ani before this can be estimated.
4. **Atakan's #1933 status**: Is the options chain PR close enough to merge that items 2 and 3 can be parallelized now, or is it still in early review?
5. **TWAP data buffer**: Is Pulse already collecting 1-minute Deribit index snapshots, or does that infrastructure need to be added?
