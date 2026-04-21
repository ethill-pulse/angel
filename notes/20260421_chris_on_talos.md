Been experimenting with vanilla OTC options - "Vanilla Options" in UI.
Everying linear for now, but can do crypto settled
No concept of expiry tied to option
"Tenor" field - optional, probably don't want to use it
hardcoded european, only one support
makes us pick an index to price - will use to price in UI - need to make sure everyone is aware
when book it can pick expiry date option down to minute

Good from our UI: we'll set expiry in our UI, will create template option that doesn't have expiry.
Create without expiry on the talos side

Need to use Atlas to book options for high touch!!!!!!!!!!!!!!


Open Q's:
- How do we add more underlyings? UI only has BTC and ETH.
- Why is counterparty blank?
- How enter a perp position?


Can we create perps in this model? Forward?