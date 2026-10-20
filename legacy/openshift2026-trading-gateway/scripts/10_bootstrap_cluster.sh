#!/usr/bin/env bash
set -euo pipefail

echo "[1/4] Creating namespaces..."
oc apply -f cluster/namespaces.yaml

echo "[2/4] Applying quotas/limits..."
oc apply -f cluster/limitranges.yaml
oc apply -f cluster/resourcequotas.yaml

echo "[3/4] Deploying platform (redpanda + postgres)..."
oc apply -f cluster/platform/redpanda.yaml
oc apply -f cluster/platform/postgres.yaml

echo "[4/4] Waiting for platform pods..."
oc -n trading-data rollout status deploy/redpanda --timeout=180s
oc -n trading-data rollout status deploy/postgres --timeout=180s

echo "Bootstrap OK"
