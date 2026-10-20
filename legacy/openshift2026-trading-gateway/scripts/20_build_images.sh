#!/usr/bin/env bash
set -euo pipefail

SERVICES=(
  market-data-adapter
  bar-aggregator
  strategy-runner
  risk-engine
  order-manager
  broker-adapter-paper
)

for s in "${SERVICES[@]}"; do
  echo "Building ${s}..."
  podman build -t "${s}:0.1.0" "services/${s}"
done

echo "Build OK"
