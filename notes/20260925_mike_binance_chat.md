# administration stuff aside, tech only, buildout

## Questions

## General

Binanace perps first, front-to-back get all the FIX drops, normalized those, get all trades and feed to us. No brainer.
Our version of TPMO, can handle via FIX.

We'll have single account, multiple account, multiple clients with different "FIX connections with keys". Through that individual trades of those clients. Get drop, use what we have, same time could pass those orders back to BASIS for booking.

Trade event activity, those are just fills?
Taxonomy, nikhil, one thing he should now do.
Asset creation real-time, structure is FACT.
Bought BASIS and they want to get up so fast.
Futures is fucked up relationship. We listen to CME secdef file.
We send to FACT, which is bad.

Mark to market PnL, Trade Booking, Reporting - BASIS will do
They'll own booking piece of that just like.
kalshi and kalshi clear, kalshi buffer fund in background we have to rec buffer fund and our positions and value-add to people is BASIS will do a backend, settlement cycle daily, snap, basis will produce downstream data for people to look at. Now for perspective basis is real-time, people hit systems, accounts are updated real-time.
Processing perspective: snap and run. Flows into snowflake. If Paul Solebo or Yang or anyone wants that, available throughout day.
For studio consumption of data, Pulse will feed LISA, which feeds studio and risk.
groove ATS, will have to recon.

processing and account structure setup, that's fine for individual client, nothing crazy.

liquidation event handling. what they do here is they capture liquidation events, book as market close kind of and wipe out, "Buffer fund" vs .
BK mo's there, BASIS flows everything real-time into BK. They create economic events in BASIS, they create right topics and segements, BK posts those, available to all CSC. wire into account, withdrawawl, whatever it is it'll just flow. BASIS and accounting guys talking to Mo to determine what's needed there.

Pulse integration to LISA
Studio display, FACT
Position display, Margin collateralization display, correct.

don't care about risk stuff, won't bore me with it.
don't have clear answer on Atul's perspective, there is cross-margin withing the account in binance. what i see is a bunch of positions that look like futures and act like futures, they margin different and trade different. But within binance perp is valuable for offset of spot position. i don't have an answer, can provide them to him intraday or whatever, not sure on what it looks like. margin call generated for perps not for cash crypto. how does risk want to see that, what will that look like?

Suley dropped me on binance API connectivity. Will talk to BASIS what we want to do there.

compliance, don't care, somebody will need to sign off on legal entity, that's fine. listen to them talk about AML/KYC.

make sure treasury guys on USD stablecoin stuff, money movements, etc. bitgo.

i'm suley, customer sub-account for binance perps, they want to wire in a million stablecoin, they send it. 

in futures seg vs non-seg. kalshi is LSOCK which is a F-PITA. we have to report to CFTC daily LSOCK balance to kalshi. treasury kind of function.

treasury has never f-ing does this.

reg reporting, zero there.
no trade confirms needed, big

niha ran the bulk of kalshi, Mike might run this, but it's in Jira.



### what does a buildout like this look for you?



### any jira project from a prior integration i can look at to see what's involved (kalshi?)



### how big of a lift do you think the perpetual swap lifecycle is?



### how do we plan to charge fees? on top of funding intervals and/or existing position?



### based on the feeds i shared, any major missing pieces?



### do we want to handle any common order routing & management stack for studio integration, or will we launch with pure DMA and we are post-trade / drop-copy only?




