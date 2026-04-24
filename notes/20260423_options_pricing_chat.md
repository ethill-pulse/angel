deribit inverse pricing not as accurate for our linear pricing
long term not a good idea
haruko if you book synthetic trade into test account for bilateral option for linear and it will generate a price
haven't checked accuracy
chris davidson -> test account -> will put in sandbox
we can tweak that so it becomes accurate -> probably right way to do it.

vol surface is vol surface assuming they are using a standard model (black 88 or something? might have made that up). 
always had model of some quant working on model validation making sure that model converges with market price where getting hedges at.

did you price with deribit inverse product or own model? think own model but heavily reliant on deribit.

suley, what is your concern with inverse? - pin risk, price would diverge around expiry & what I don't know
interest rates are different so should be consistent pricing differential
deribit uses futures with same expiry for deriving interest rate
don't use specific interest rate, look at future
DBT doesn't create price market does
when you try to calc implied vol based on those prices, what they use is future price as forward instead of spot price plus interest rate
cost of capital different? interest rate etc

is there some connection between hedge and price we are going to deal with? sounds like no direct constrained relationship.
might be some relationship we could tune with time but no guarantees.

firm needs pricing source for option based off standard market variables so they can know PnL.
It's m2m price essentially
Pricing an OTC option for a client.


First what price to mark positions to market.
Trade on, captured more than paid, that's PnL
Tomorrow what is value? Use this value to mark every day up until expiry.
If choose Haruko, always use as price for m2m source.
Used different price source for actually quoting to client.




Expiry price of bilateral. 
Value at m2m? In reality we need actual calculation of index price * strike price * blah blah blah -> price building contract.
index to strike * contract price -> only problem is index. strike is know. 
index from haruko?
30 mins out of expiry use TWAP to prevent price manipulation.
deribit index to start.

deribit index price for expiry value 
deribit index minus strike is expiry value, using TWAP. slices 1 minute over 30 min period.

every day pull their symbol list of options and create synthetic to get prices.
unified model between pricing and quoting one day.

long term for regulatory perspective, easier if building off same base model and front-office can tweak base models to create price to show client
from audit and validation perspective, same model and validated, front-office has discretion when it comes to pricing things

priority list:
0. existing spot and loan/borrow maintenance
1. streaming spot
2. finish options
3. perps
(on side doing integration with new counterparties, LPs, etc)
4. future roadmap step planning: info gathering, discussion on what has upside and people available

wintermute best product because offer CFD's

did they shift focus from perps to kalshi, esp now adding perps?
us: liquidity hard to access, perps and predicutions fall into that, both hot and over next two years will have their moments


