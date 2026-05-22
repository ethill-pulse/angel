# Kalshi / Prediction Markets

## What We're Building

CS trades event contracts on Kalshi — a CFTC-regulated prediction market exchange. Contracts are binary: they settle at $1.00 if the event occurs, $0.00 if it doesn't. Events include economic indicators, financial outcomes, and other measurable real-world events.

The business runs two parallel tracks:

1. **CS as LP/hedge:** CS LLC runs a proprietary FCM account on Kalshi and executes hedges there directly
2. **CS as dealer:** CS LLC writes EDC (Event-Driven Contract) swaps to institutional clients (e.g., Roundhill, Bitwise) referencing Kalshi contracts. CS hedges 1:1 on Kalshi to stay flat

---

## Why Prediction Markets

Prediction markets are a CFTC-sanctioned way to trade on event outcomes. For an institutional client that wants exposure to, say, the outcome of a Fed decision or an election result without taking a directional bond or equity position, an event contract is the instrument. Kalshi is currently the primary regulated venue for this in the US.

The EDC swap structure (CS writes a bilateral swap to the client that references a Kalshi contract) gives clients exposure to the event without having a Kalshi account themselves — CS handles the exchange relationship.

---

## The Key Risk Constraint

Unlike calendar-dated instruments, Kalshi contracts reference **event dates**, not calendar dates. Kalshi can accelerate settlement (if the event outcome is determined early), delay it, or invoke a Market Outcome Review process to challenge a result.

Any engine handling Kalshi positions must consume Kalshi's lifecycle events — not just a settlement calendar. A hardcoded "this contract settles on date X" approach will break.

---

## Execution

The execution side (Pulse's job) is largely done. Emre built the `Venue::Kalshi` scaffold and `PredictionProduct` type in Pulse, which gives Polaris the ability to route orders to Kalshi the same way it routes to any other venue.

For the TWAP use case (executing a large chunk of an ETF hedge over 30 minutes into the close), Anton built a full TWAP engine in Polaris — supervisor, slicer, and pegger stack. This handles large block execution without moving the market.

---

## Booking

Execution is automated. Booking is not — yet.

When Polaris executes on Kalshi, the resulting trades need to flow into CS's back office:

```
TWAP execution → Kafka → TPMO → Lisa → BASIS
```

**TPMO** takes execution reports from Kafka. **Lisa** needs two sides to match: the Kalshi Klear side (Kalshi's clearing system) and the CS side. **BASIS** is the trade booking system.

Complexity: Kalshi trades on weekends and at midnight. The rollover infrastructure (which normally runs before midnight for securities) has to accommodate this. Lisa matching requires both sides to be available, and Kalshi Klear files may not arrive on the same schedule as a standard exchange.

The fallback is a file upload directly to Lisa or BASIS — ops manually uploads execution reports. This is the current state while the Kafka→TPMO path is being validated.

---

## Studio EMS

CS has a Kalshi workspace in Studio EMS — deployed and live as of late April. It includes:

- Symbol picker for Kalshi contracts
- L2 market depth
- Fractional trades (down to $0.10)
- Full Kalshi workspace with dedicated layout

This is for CS's internal traders. External client access to Kalshi contracts is through the EDC swap product (CS is the counterparty; client doesn't need a Kalshi account).

---

## Systems Involved

| System | What It Does in This Context |
|--------|------------------------------|
| Pulse / Polaris | Execution layer; Venue::Kalshi; TWAP engine |
| Studio EMS | Internal trading UI for Kalshi contracts |
| TPMO | Takes execution reports from Kafka after TWAP execution |
| Lisa | Two-sided matching (Kalshi Klear + CS side) |
| BASIS | CS trade booking for the exchange-cleared side |
| Voyager | Booking for the CSD↔client EDC swap side |
| Kalshi Klear | Kalshi's clearing system — provides the clearing-side of the trade |

---

## Further Reading

- [Notes: Jon Daplyn meeting on Kalshi/Polaris booking flow](../notes/20260428_kalshi_twap_polaris.md)
- [Notion: Kalshi Swap Trade Overview for Risk](https://www.notion.so/34c1043d19d58026bceae357206f0b68)
- [Notion: [Prod] Kalshi Trading checklist](https://www.notion.so/32c1043d19d58074ae89f9f80e7c7d4c)
