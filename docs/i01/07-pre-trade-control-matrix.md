# I01 — Matrice des contrôles pré-trade

## Objectif

Relier contrôle -> exigence -> composant -> décision -> preuve.

## Matrice

| Contrôle | Exemple de règle | Placement candidat | Action | Preuve attendue |
|---|---|---|---|---|
| Instrument autorisé | whitelist / restriction | OMS/Risk/Gateway | REJECT | policy + event |
| Trading permission | user/account/desk enabled | OMS/Risk | REJECT | identity + policy |
| Max order quantity | qty <= limit | Risk/Gateway | REJECT | qty, limit |
| Max notional | qty * price <= limit | Risk | REJECT | notional, limit |
| Price collar | price within band | Risk/Gateway | REJECT | ref price, band |
| Position limit | projected position <= limit | Risk | REJECT | position snapshot |
| Credit limit | exposure <= available credit | Risk | REJECT | exposure/limit |
| Message throttling | msgs/sec <= threshold | Gateway | THROTTLE/REJECT | counters |
| Duplicate ID | ClOrdID uniqueness rule | OMS/Gateway | REJECT/DEDUP | correlation |
| Market state | venue/instrument open | SOR/Gateway | HOLD/REJECT | state source |
| Stale market data | age <= threshold | SOR/Risk | STOP ROUTING | data timestamp |
| Self-trade prevention | avoid prohibited self-match | SOR/Venue | REJECT/REROUTE | account/firm IDs |
| Kill functionality | target active orders by scope | Control/Gateway | CANCEL | target set + audit |
| Route enabled | venue/route healthy | SOR/Gateway | REROUTE/REJECT | health state |

## Responsabilité

Un contrôle peut exister à plusieurs niveaux pour défense en profondeur. Il faut néanmoins définir :
- propriétaire de la règle ;
- source de données ;
- seuil ;
- latence maximale du contrôle ;
- comportement en cas d'indisponibilité ;
- journal de décision ;
- procédure de changement.

## Fail-open vs fail-closed

Pour un contrôle critique, **fail-open** peut transformer une panne de contrôle en envoi non maîtrisé. Le choix doit être explicite et documenté.

Exemples de comportements prudents :
- reject new orders ;
- cancel-only ;
- route disable ;
- kill selective ;
- require operator intervention.

## Kill functionality

Le design doit permettre de cibler les ordres non exécutés selon des périmètres opérationnels utiles :
- trader ;
- desk ;
- client ;
- algorithme ;
- venue ;
- instrument ;
- route.

Le système doit donc indexer de façon fiable les ordres actifs et leur origine.

## Traçabilité

Chaque décision de contrôle doit permettre de reconstruire :
```text
order
 -> control name
 -> rule version
 -> input values
 -> threshold
 -> decision
 -> timestamp
 -> component
 -> operator/config source
```

## Critère oral

Pouvoir expliquer où placer au moins cinq contrôles, pourquoi, et ce qui se passe si la dépendance de risque devient indisponible.
