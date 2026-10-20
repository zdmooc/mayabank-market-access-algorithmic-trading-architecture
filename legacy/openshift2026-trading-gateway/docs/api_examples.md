# API examples

## Create an order
```bash
HOST=$(oc -n trading-apps get route order-manager --template='{{ .spec.host }}')
curl -sS -X POST "http://$HOST/orders" -H 'Content-Type: application/json' -d '{
  "symbol":"AAPL","side":"BUY","qty":10,"type":"MARKET"
}'
```

## Get an order
```bash
curl -sS "http://$HOST/orders/<ORDER_ID>" | python -m json.tool
```
