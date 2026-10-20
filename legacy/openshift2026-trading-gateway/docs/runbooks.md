# Runbooks (starter)

## Incident: no bars
**Checks**
- `oc -n trading-apps logs deploy/market-data-adapter -f`
- `oc -n trading-apps logs deploy/bar-aggregator -f`
- `oc -n trading-data get pods`

**Fix**
- `oc -n trading-apps rollout restart deploy/bar-aggregator`

## Incident: orders never filled
**Checks**
- `oc -n trading-apps logs deploy/broker-adapter-paper -f`

**Fix**
- `oc -n trading-apps rollout restart deploy/broker-adapter-paper`
