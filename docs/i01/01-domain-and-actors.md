# I01 — Domaine Market Access et acteurs

## Objectif

Savoir expliquer le fonctionnement métier d'un accès marché sans se réfugier dans l'infrastructure.

## Chaîne de valeur simplifiée

```text
Client / Portfolio Manager / Trader
            |
            v
         OMS
            |
            v
      EMS / Algo
            |
            v
           SOR
            |
            v
  Pre-Trade Risk Controls
            |
            v
  Market Access Gateway
       /          \
    FIX/FIXT     Native
       \          /
        Broker / Venue / MTF
            |
            v
      Execution / Reject
            |
            +--> Drop Copy / Surveillance / Reconciliation
```

## Acteurs

### Buy-side
Gestionnaire d'actifs, fonds, assureur, hedge fund ou autre investisseur institutionnel. Il initie une intention d'investissement et peut transmettre des ordres à un broker ou utiliser des mécanismes d'accès électronique selon son modèle.

### Sell-side
Banque d'investissement, broker-dealer ou intermédiaire fournissant exécution, liquidité, algorithmes, accès aux venues et services associés.

### Trader
Utilisateur ou fonction qui prend une décision de négociation et soumet une instruction à l'OMS/EMS ou à un algorithme.

### Market maker
Participant publiant des prix acheteur/vendeur et fournissant de la liquidité selon son modèle d'activité et les règles applicables.

### Broker
Intermédiaire qui reçoit et exécute des ordres pour le compte d'un client, ou fournit un accès électronique au marché.

### Venue
Lieu de négociation ou destination d'exécution. Selon le contexte européen : marché réglementé, MTF, OTF ou autre destination autorisée.

### MTF
Multilateral Trading Facility : système multilatéral de négociation. Pour I01, l'objectif est de savoir le distinguer d'un broker et d'un composant interne de routing.

### Clearing / CCP
La chaîne de clearing est postérieure à l'exécution. Elle ne doit pas être confondue avec la décision de routing ni avec la confirmation d'exécution.

## Objets métier à distinguer

- **Order** : instruction de négociation encore active ou terminée.
- **Execution** : tout ou partie de la quantité effectivement exécutée.
- **Transaction / Trade** : résultat économique enregistré à partir d'une exécution selon le modèle du système concerné.
- **Parent order** : ordre source pouvant être découpé.
- **Child order** : ordre dérivé adressé à une destination ou une stratégie particulière.
- **Venue order** : instance de l'ordre vue par la venue.
- **Execution report** : événement de workflow utilisé pour annoncer un état ou une exécution.
- **Drop copy** : copie indépendante d'événements d'ordres/exécutions utilisée pour contrôle, surveillance et réconciliation.

## Responsabilités fonctionnelles

| Capacité | Responsabilité principale |
|---|---|
| Capturer l'ordre client | OMS |
| Gérer l'exécution | EMS / Algo |
| Choisir une destination | SOR / stratégie |
| Contrôler avant envoi | Pre-Trade Risk |
| Gérer la connectivité venue | Market Access Gateway |
| Gérer session/protocole | FIX/native adapter |
| Publier état/exécution | Venue + chaîne de retour |
| Contrôler indépendamment | Drop Copy / surveillance |
| Réconcilier les écarts | OMS / middle-office / contrôle selon organisation |

## Frontière importante

Le **Market Access** n'est pas l'OMS complet, le SOR complet, la plateforme de risque complète ni la Market Data Platform complète. C'est la frontière d'exécution et de connectivité vers les destinations de marché, avec des contrôles et états suffisamment proches pour garantir sécurité, fiabilité et performance.

## Critère de sortie I01 associé

Pouvoir expliquer oralement :
1. la différence buy-side / sell-side / venue / broker ;
2. la différence order / execution / transaction ;
3. la différence parent / child / venue order ;
4. pourquoi le Market Access Gateway est une frontière et non un bus d'intégration générique.
