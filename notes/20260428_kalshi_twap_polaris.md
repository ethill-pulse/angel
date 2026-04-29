meeting w/ jon daplyn on kalshi

will lave block trading to side for this convo, separate concern

have been working on studio EMS to trade in market for house and clients, trying to get to prod tomorrow
that's part of flow
rest of flow is booking flow. at back of doing trade need to send to infra for it to be accounted for in ledgers. that goes EMS -> TPMO -> lisa -> basis
lisa needs two side (kalshi clear side, our side, match to basis)
we are a few weeks away from really having that fully done
complexity: trade to midnight and weekends, lots of infra to support that flow at that timeframe. normally we do our rollover way before midnight or else that will be late.
can support execution through that channel
suley is asking for TWAP capability, anton building, would execute directly on kalshi
what we need to agree on, what does booking model look like after that.
fine can execute, need to be able to book it.
at the moment, it'd have to be manual, don't see any way to connect to anything at the moment
only possibility is kalshi clear CSV files into lisa -> Jon confused on if used lisa to listen to clearing feed, how does that flow into TPMO? Nikhil: it won't
lisa into basis
maybe listen to feed and manaully book into back of it
book average price?
maybe an upload? direclty into lisa
basis side we can do manual booking

kafka to TPMO? They take execution reports.
TWAP into the close for 2 hours! This is for the chunk of the ETF we say we can execute.
Book into Lisa or Basis.

takeaways
TWAP order needs proper account ID
confirm TPMO + Lisa available in prod (then kafka and format)
otherwise need to agree on file format so ops can book it.

