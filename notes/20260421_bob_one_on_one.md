finance team PnL report.
2 ways: opening balance, credits and debits, closing balance
works until it doesn't from experience. no granular reporting, not a good job of building up risk positions in the long term.
sometimes when you start working on derivs, risk is more than physical balance, works fine for spot because physical credit or debit
ideal world is trade by trade, have to tie client trades to hedges, 1:1 for now, longer term any time you don't hedge 1:1 you book to risk account.
push problem to risk account, unrealized gains and losses in risk account, perfect if treat as ...
tie client orders to positions, need to correlate both offsetting trade and client trade: Akshay
easier said than done, right way to do it.
stamp ID into polaris for offsetting position reporting.
every pair in each exchange. from a risk perspective we need to know what we have where always.
outstanding question on this: pricing is pricing, reference data is fixing number, pricing is m2m from suley, confusing to bob (he sees it backwards).
suley worried about pin risk, gamma, volatility into expiry like if using end of month expiry to hedge monday morning expirty, won't converge at same price and then exposure at that price (pin risk or gamma risk, same thing). suley is very concerned about that. neither one of us options traders.
Anton fell in same camp as Bob, which is use 3rd party data source instead of our own models for M2M pricing.

Use Haruko for vol surface to generate fair market price.
Need to do model validation with them which is risk team's job.
Use that as fair market value. That's kind of what it's done. Calculating based on vol surface what it thinks is value of option.

In future once all data goes into current risk system, we'll be able to pull fair value from there.

general complaints about onboarding (bob venting):
1 client through onboarding so far, not a very good client.
why not more? very stupid processes with very speed not being a priority. lots of dumb processes that are linear but should be in parallel that are not driven by compliance.
why can't i send out an ISDA contract prior to them onboarding? takes forever
