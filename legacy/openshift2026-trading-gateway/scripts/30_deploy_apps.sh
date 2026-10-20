#!/usr/bin/env bash
set -euo pipefail

echo "Deploying apps..."
oc apply -k deploy/overlays/dev

echo "Waiting for app deployments..."
for d in market-data-adapter bar-aggregator strategy-runner risk-engine order-manager broker-adapter-paper; do
  oc -n trading-apps rollout status deploy/$d --timeout=180s
done

echo "Order Manager route:"
oc -n trading-apps get route order-manager -o wide || true
