#!/usr/bin/env bash
set -euo pipefail

HOST="$(oc -n trading-apps get route order-manager --template='{{ .spec.host }}' 2>/dev/null || true)"
if [[ -z "${HOST}" ]]; then
  echo "Order Manager route not found."
  exit 1
fi

BASE_URL="http://${HOST}"
echo "Base URL: ${BASE_URL}"

echo "Creating an order..."
curl -sS -X POST "${BASE_URL}/orders" -H 'Content-Type: application/json' -d '{
  "symbol": "AAPL",
  "side": "BUY",
  "qty": 10,
  "type": "MARKET"
}' | tee /tmp/order.json

ORDER_ID="$(python - <<'PY'
import json
print(json.load(open("/tmp/order.json")).get("id",""))
PY
)"
echo "Order ID: ${ORDER_ID}"

echo "Watching order state (10s)..."
for i in $(seq 1 10); do
  curl -sS "${BASE_URL}/orders/${ORDER_ID}" | python -m json.tool || true
  sleep 1
done
