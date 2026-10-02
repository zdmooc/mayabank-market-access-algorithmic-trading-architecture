# I01 — Validation humaine

## Statut

**CONTENT_COMPLETE / HUMAN_VALIDATION_PENDING**

I01 n'est pas considéré DONE tant que l'architecte ne peut pas expliquer les sujets ci-dessous sans notes.

## Questions obligatoires

1. Quelle différence entre ordre, exécution et transaction ?
2. Quelle différence entre parent order, child order et venue order ?
3. Quelle différence entre OMS, EMS, SOR, Algo et Market Access Gateway ?
4. Quelle différence entre un risk reject et un venue reject ?
5. Que signifie "Ack" dans le cycle d'ordre ?
6. Pourquoi un Cancel/Replace n'est-il pas une mutation locale ?
7. Que se passe-t-il si un Fill croise un Cancel Request ?
8. Quelle différence entre Order Reject et Cancel Reject ?
9. Quel est le rôle d'une Drop Copy ?
10. Comment réconcilier une exécution absente de l'OMS ?
11. Pourquoi un ordre en état local UNKNOWN doit-il bloquer certaines actions ?
12. Où peut-on placer les contrôles pré-trade ?
13. Que signifie fail-closed pour le risk control ?
14. Comment retrouver tous les ordres concernés par un kill switch sélectif ?
15. Pourquoi les identifiants venue et client doivent-ils être conservés ?
16. Que signifie CumQty / LeavesQty / LastQty ?
17. Pourquoi Market Data stale peut-elle arrêter le routing ?
18. Quelle différence entre broker, venue et MTF ?
19. Pourquoi le Market Access Gateway ne doit-il pas devenir un bus générique ?
20. Quelles preuves faut-il garder pour reconstruire un incident ?

## Exercice tableau blanc

Dessiner sans notes :

```text
Trader/Algo
 -> OMS
 -> EMS/SOR
 -> Pre-Trade Risk
 -> Market Access Gateway
 -> Venue

Venue
 -> Execution Reports
 -> OMS

Venue
 -> Drop Copy
 -> Reconciliation
```

Puis ajouter :
- Reject ;
- Partial Fill ;
- Cancel ;
- Cancel/Replace ;
- Fill-vs-Cancel race ;
- Kill selective.

## Validation

- **20/20 expliqué correctement** : I01 VALIDATED.
- **17-19/20** : revue ciblée puis re-test.
- **<17/20** : I01 reste HUMAN_VALIDATION_PENDING.

Le passage à I02 n'est autorisé qu'après validation de cette grille.
