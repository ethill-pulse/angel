gotcha: needs our positions to price it
2 options:
- push all positions in array and then get from there, some limitations if positions too big, cumbersome and so on. benefit: positions don't have to be in haruko (stateless).
- have all trades in haruko, specify the accounts that need to be considered for positions, and specify in payload, then get prices back. downside it needs state. in theory it has it and we could do that.


### Get OTC Price
POST https://clst-sbx.haruko.io/cefi/api/derivatives/pricing/price_positions/v2
Authorization: Bearer {{token}}
Content-Type: application/json

{
   "aggregateGroups":true,
   "aggregateSymbols":true,
   "stickinessMicro":1,
   "tenorPivot":0.7,
   "outputs":[
      "markPxAsk",
      "markPx",
      "markPxBid",
      "askIv",
      "markIv",
      "bidIv",
      "volatilityAsk",
      "volatility",
      "volatilityBid",
      "premiumAsk",
      "premium",
      "premiumBid",
      "deltaBase",
      "deltaTerm",
      "deltaAdjBase",
      "deltaAdjTerm"
   ],
   "valuationTs":1776786632588,
   "positions":[
      {
         "baseAsset":"BTC",
         "termAsset":"USD",
         "notional":1,
         "expiryTs":1779350400000,
         "strike":80000,
         "referenceVenue":"DERIBIT",
         "premiumCurrency":"USD",
         "notionalCurrency":"BTC",
         "label":"1776786623858",
         "optionSide":"CALL",
         "positionType":"VANILLA"
      }
   ],
   "parameters":[
      {
         "futuresConfigName":"BTC (DERIBIT SR)",
         "instrument":{
            "baseAsset":"BTC",
            "termAsset":"USD"
         },
         "interestRateDefaults":{
            "override":true,
            "alpha":0
         },
         "surfaceConfigName":"BTC (DERIBIT SVI)"
      }
   ]
}

