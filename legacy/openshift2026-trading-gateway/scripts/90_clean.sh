#!/usr/bin/env bash
set -euo pipefail
oc delete ns trading-data trading-apps trading-platform trading-ops --ignore-not-found=true
echo "Clean OK"
