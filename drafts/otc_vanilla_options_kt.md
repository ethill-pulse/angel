# Vanilla OTC Options

*An overview of how vanilla OTC options work, how they are priced, and how risk is managed — with notes on crypto-specific considerations.*

---

## What Is a Vanilla OTC Option?

An **option** is a contract that gives the buyer the **right, but not the obligation**, to buy or sell an asset at a fixed price (the **strike**) on or before an agreed date (the **expiry**).

**Vanilla** means it has no exotic features — just the standard payoff structure.

**OTC (Over-The-Counter)** means it's a bilateral contract negotiated directly between two counterparties (us and a client), rather than traded on an exchange with a central clearinghouse. This gives flexibility in terms, but introduces counterparty credit risk.

### The Two Flavors

| Type | Buyer Right | In the Money When |
|------|-------------|-------------------|
| **Call** | Buy the asset at strike | Spot > Strike |
| **Put** | Sell the asset at strike | Spot < Strike |

### Exercise Styles

- **European** — can only be exercised at expiry. Most crypto OTC options are European.
- **American** — can be exercised at any time up to expiry.

> **Note:** At launch, we support European-style options only.

### Key Terms

| Term | Definition |
|------|------------|
| **Underlying** | The asset the option is written on (e.g., BTC, ETH) |
| **Notional** | The quantity of the underlying the contract covers |
| **Strike** | The agreed price at which the option can be exercised |
| **Expiry** | The date/time the contract expires |
| **Premium** | The price paid by the buyer to the seller for the option |
| **Settlement** | How the payoff is delivered at expiry — cash or physical delivery |

---

## Payoff at Expiry

The payoff is deterministic once expiry price is known.

```
Call payoff = notional × max(S - K, 0)
Put payoff  = notional × max(K - S, 0)
```

Where `S` = spot/index price at expiry, `K` = strike, `notional` = quantity of the underlying.

**Example — BTC Call:**
- Strike: $80,000, Notional: 1 BTC
- Expiry index price: $95,000
- Payoff: `max(95,000 - 80,000, 0)` = **$15,000**

If spot expires below strike, the option expires worthless and the buyer loses only the premium paid.

### Expiry Index Price

For crypto OTC options the expiry "spot" price is calculated as a **TWAP of Deribit's composite index, sampled every 4 seconds over the final 30 minutes before expiry**. This prevents price manipulation at the moment of settlement.

> **Note for implementers:** Deribit's index is itself a multi-venue composite with specific exchange weighting and outlier rejection — it is not simply "Deribit's spot price." Engineers building settlement logic should consult [Deribit's published index methodology](https://www.deribit.com/pages/docs/index) rather than rely on this description, as the exact composition matters for settlement dispute resolution and pin-risk analysis.

---

## How Options Are Priced

### Black-Scholes / Black-76 Model

The standard pricing model for vanilla options. Given inputs, it produces a fair-value premium.

**Inputs:**
- `S` — current spot (or forward) price
- `K` — strike
- `T` — time to expiry (in years)
- `r` — risk-free interest rate
- `σ` — implied volatility

For crypto specifically, **Black-76** (using the forward price rather than spot + rate) is often preferred because it sidesteps the complexity of crypto funding rates and cost of carry.

### Implied Volatility

Volatility is the only input you can't observe directly — it's backed out from market prices. If an option is trading at a certain premium in the market, you can reverse-engineer the `σ` that makes the model price match. This is **implied vol (IV)**.

IV is the primary way market participants quote options:

> "I'll sell you that BTC 80k call at 55 vol"

means: price it with σ = 55%, everything else equal.

### The Volatility Surface

IV varies by:
- **Strike** — options OTM (out-of-the-money) or ITM (in-the-money) often trade at higher vol than ATM. This shape is called the **vol smile** or **skew**.
- **Expiry** — longer-dated options typically have different vol than shorter-dated ones (term structure).

Together, strike × expiry → IV forms a **volatility surface**. Pricing any option requires looking up or interpolating the right point on this surface.

For crypto, Deribit is the primary reference market. We pull the Deribit vol surface (SVI-parameterized) as our pricing input.

---

## The Greeks — Risk Sensitivities

The Greeks describe how an option's value changes as market conditions change. These are the language of options risk management.

| Greek | What It Measures | Direction of Risk |
|-------|-----------------|-------------------|
| **Delta (Δ)** | Change in option value per $1 move in the underlying | Exposure to spot direction |
| **Gamma (Γ)** | Rate of change of delta per $1 move in spot | Acceleration of delta; high near expiry ATM |
| **Vega (ν)** | Change in value per 1 vol point move in IV (e.g., 55% → 56%); positive for long, negative for short | Exposure to volatility |
| **Theta (Θ)** | Change in value per day passing (time decay) | Options lose value as time passes |
| **Rho (ρ)** | Change in value per 1% move in interest rates | Relevant for longer-dated options |

### Delta in Practice

A call option has delta between 0 and 1 (expressed as a fraction of notional):
- Deep ITM call ≈ delta 1.0 (behaves like holding the asset)
- ATM call ≈ delta 0.5
- Deep OTM call ≈ delta ~0

If we sell a client a 1 BTC call, our book is **short delta** by 0.5 BTC — if BTC goes up $1, we lose $0.50. To hedge this, we buy 0.5 BTC in the spot market, bringing our net delta to zero. Note: the option's delta (0.5) is a property of the instrument; "short delta" describes our book position after selling it.

---

## Delta Hedging — Managing Directional Risk

The most fundamental risk management technique for options dealers.

**Goal:** neutralize directional exposure (delta) so that P&L is driven by volatility, not spot moves.

### How It Works

1. Sell option to client, calculate resulting delta.
2. Immediately hedge delta by trading the underlying spot or futures.
3. As spot moves, delta changes (due to gamma). **Rebalance the hedge** periodically.

This is called **dynamic delta hedging** or **delta-gamma hedging**.

### Hedging Frequency

Continuous hedging is theoretically ideal but impractical. In practice, dealers:
- Rehedge at fixed time intervals (e.g., every hour)
- Rehedge when delta moves past a threshold (e.g., ±0.05 BTC)
- Use a combination of both

The cost of hedging (bid/ask spread on each rebalance trade) is a real P&L drag. This is one reason the premium charged to clients includes a spread.

### Delta Base vs Delta Term

In crypto, delta can be expressed in the base asset (BTC) or the term asset (USD):
- **Delta base** — how much BTC to hedge
- **Delta term** — how much USD equivalent to hedge

Both are valid; which one matters depends on how the trade is settled and how the desk manages its book.

---

## Vega Risk — Managing Volatility Exposure

When you sell an option, you are **short vega** — if IV goes up, the option becomes more expensive and you lose mark-to-market value.

### How to Hedge Vega

- Buy other options with similar vega to offset.
- Maintain a **vega-neutral book** across strikes and expiries.
- In practice, most dealers run a structured book and accept some residual vega within risk limits.

### Vol Spread as P&L

The difference between the vol at which you sold (to the client) and the vol at which you can hedge (in the market) is your **vol spread** — the core source of revenue for an options dealer.

---

## Mark-to-Market (M2M)

Options positions must be revalued continuously to compute unrealized P&L.

**Process:**
1. Pull the current vol surface (e.g., from Deribit via Haruko).
2. Re-run the pricing model against each open position with current inputs (spot, vol, time to expiry).
3. The new fair value is the **mark price**.
4. P&L = (current mark) - (previous mark).

This is important for:
- Internal risk reporting
- Margin and collateral requirements
- Accounting

The pricing source used for M2M should be consistent for the life of a trade.

---

## The Trade Lifecycle

```
1. QUOTE REQUEST   Client asks for a price on a specific option
       ↓
2. PRICING         We price using vol surface + model (Haruko or internal)
       ↓
3. QUOTE           We send bid/ask premium to client
       ↓
4. EXECUTION       Client accepts; bilateral trade is confirmed
       ↓
5. BOOKING         Trade entered into our system; Greeks computed
       ↓
6. HEDGING         Delta hedge placed immediately
       ↓
7. M2M PRICING     Position revalued every 5 minutes against current market
       ↓
8. ONGOING HEDGING Delta rebalanced as spot moves
       ↓
9. EXPIRY          Index price calculated (TWAP); payoff determined
       ↓
10. SETTLEMENT     Cash payoff delivered to winning party
```

---

## Settlement

### Cash Settlement

The most common for crypto OTC. At expiry:
- Calculate index price (TWAP).
- Compute payoff: `max(S - K, 0)` for a call.
- Net cash transferred between counterparties.

No physical delivery of BTC. Simpler operationally.

### Physical Settlement

The buyer receives (call) or delivers (put) the actual BTC. Less common in OTC crypto but used in some institutional trades.

> **Note:** For MVP we only support cash settlement.

---

## Key Risk Summary

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Delta risk** | Spot price moves against position | Dynamic delta hedging |
| **Vega risk** | IV increases after selling | Hedge with offsetting options; vol spread as buffer |
| **Gamma risk** | Delta moves rapidly near expiry (esp. ATM) | Monitor and rehedge more frequently near expiry |
| **Theta** | Time decay works in seller's favor | Not a risk for option sellers; buyers must monitor |
| **Index/expiry risk** | Dispute or manipulation of settlement price | Use robust TWAP from trusted index (Deribit) |
| **Counterparty risk** | Client defaults at expiry | Collateral agreements, credit limits |
| **Model risk** | Vol surface or model is wrong | Model validation; cross-reference multiple sources |
| **Liquidity risk** | Can't hedge or unwind efficiently | Prefer dated futures or spot for delta hedges; perps carry continuous funding rate exposure that must be tracked separately |

---

## Crypto-Specific Considerations

- **No standard clearing** — crypto OTC options are fully bilateral; credit risk is real.
- **Vol surface sourced from Deribit** — Deribit is the dominant listed crypto options market. Its vol surface is the primary reference for BTC and ETH OTC pricing.
- **Inverse vs linear products** — Deribit historically used BTC-margined (inverse) contracts. For inverse contracts, P&L is denominated in BTC rather than USD, making the payoff nonlinear in spot price. This affects the effective delta and the shape of the vol surface. **Inverse IV is not directly substitutable into a Black-76 pricer for a linear (USD-settled) contract** — particularly for deep ITM/OTM strikes or longer expiries where the convexity difference is material. Our product is linear; Haruko is the source of truth for pricing and is assumed to handle this adjustment internally. This assumption should be validated by the quant team during model review.
- **Interest rates and funding** — crypto cost-of-carry includes funding rates (for perps) or futures basis, not a clean risk-free rate. Black-76 using the forward price avoids this complication.
- **24/7 market** — options can move into or out of the money at any time, including weekends. Hedging and monitoring need to account for this.
- **Settlement index** — Deribit's index is the de facto standard for crypto expiry settlement. Using a 30-minute TWAP is market convention to prevent manipulation.

---

## Glossary

| Term | Definition |
|------|------------|
| ATM | At-the-money — strike ≈ current spot |
| ITM | In-the-money — option has intrinsic value |
| OTM | Out-of-the-money — option has no intrinsic value, only time value |
| Premium | Price of the option contract |
| IV / Implied Vol | Volatility implied by the market price of an option |
| Vol surface | 2D map of IV across strikes and expiries |
| TWAP | Time-Weighted Average Price |
| Delta hedge | Spot/futures trade to neutralize directional exposure |
| Black-76 | Options pricing model using forward price instead of spot |
| SVI | Stochastic Volatility Inspired — a parameterization that describes the shape of the vol smile across strikes for a given expiry |
| M2M | Mark-to-market — current fair value of a position |

---

*For how these concepts map to our systems and booking model, see [OTC Options](project_otc_options.md).*
