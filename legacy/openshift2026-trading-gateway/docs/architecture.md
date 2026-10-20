# Architecture

This platform mirrors a “Gateway / platform backend” approach, applied to trading.

```mermaid
flowchart LR
  subgraph Market Data
    MDA[market-data-adapter\n(sim)]
    BA[bar-aggregator]
  end

  subgraph Trading
    STRAT[strategy-runner]
    RISK[risk-engine]
    OMS[order-manager (API)]
    BROKER[broker-adapter-paper]
  end

  subgraph State
    PG[(PostgreSQL)]
  end

  subgraph Bus
    RP[(Redpanda\nKafka API)]
  end

  MDA -->|md.ticks| RP
  RP --> BA
  BA -->|md.bars| RP
  BA -->|store bars| PG

  RP --> STRAT
  STRAT -->|strategy.signals| RP

  RP --> RISK
  RISK -->|orders.new| RP

  OMS -->|store orders| PG
  OMS -->|orders.new| RP

  RP --> BROKER
  BROKER -->|fills.executed| RP
  BROKER -->|orders.state| RP

  RP --> OMS
  OMS -->|update state| PG
```

## Topics
- `md.ticks` : simulated ticks (symbol, price, ts)
- `md.bars` : aggregated bars
- `strategy.signals` : BUY/SELL signals
- `orders.new` : orders
- `orders.state` : order state transitions
- `fills.executed` : paper fills
