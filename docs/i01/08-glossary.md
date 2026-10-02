# I01 — Glossaire Market Access

1. **Algorithmic Trading** — génération ou gestion automatisée de décisions d'ordre selon des règles/algorithmes.
2. **Algo** — composant ou stratégie algorithmique exécutant une logique de trading.
3. **Ask** — meilleur prix vendeur ou offre selon le carnet.
4. **Bid** — meilleur prix acheteur selon le carnet.
5. **Broker** — intermédiaire donnant accès à des marchés ou exécutant pour le client.
6. **Buy-side** — acteurs d'investissement tels que gestionnaires d'actifs, fonds ou institutionnels.
7. **Sell-side** — banques/brokers fournissant exécution, liquidité ou services de marché.
8. **Venue** — destination/plateforme de négociation.
9. **MTF** — Multilateral Trading Facility.
10. **Market Maker** — participant fournissant des prix acheteur/vendeur selon son modèle.
11. **Order** — instruction de négociation.
12. **Parent Order** — ordre source pouvant être découpé.
13. **Child Order** — sous-ordre dérivé d'un parent.
14. **Venue Order** — ordre tel qu'identifié sur la venue.
15. **Execution** — réalisation partielle ou totale d'un ordre.
16. **Fill** — exécution d'une quantité.
17. **Partial Fill** — exécution partielle.
18. **OrderQty** — quantité de l'ordre.
19. **CumQty** — quantité cumulée exécutée.
20. **LeavesQty** — quantité restante.
21. **LastQty** — quantité de la dernière exécution.
22. **Limit Order** — ordre avec contrainte de prix.
23. **Market Order** — ordre visant l'exécution selon conditions de marché disponibles.
24. **Time in Force** — règle de durée/validité d'un ordre.
25. **Ack / Acknowledgement** — concept d'acceptation de l'ordre par l'étape suivante.
26. **Reject** — refus d'un nouvel ordre ou d'une action.
27. **Cancel Request** — demande d'annulation d'un ordre actif.
28. **Cancel/Replace** — demande de modification d'un ordre ouvert.
29. **Cancel Reject** — refus d'une demande d'annulation/remplacement.
30. **Execution Report** — événement de statut/exécution dans le workflow FIX.
31. **OMS** — Order Management System.
32. **EMS** — Execution Management System.
33. **SOR** — Smart Order Router.
34. **Market Access Gateway** — frontière de connectivité vers broker/venue.
35. **Pre-Trade Risk** — contrôles exécutés avant transmission de l'ordre.
36. **Kill Functionality** — mécanisme d'urgence permettant d'annuler tout ou partie des ordres non exécutés ciblés.
37. **Throttling** — limitation du rythme de messages/ordres.
38. **Market Data** — données de marché : prix, carnet, transactions, états.
39. **Feed Handler** — composant recevant et décodant un flux de Market Data.
40. **Snapshot** — état complet du carnet ou d'un jeu de données à un instant.
41. **Incremental Update** — mise à jour partielle appliquée à un état existant.
42. **Order Book** — carnet d'ordres.
43. **Stale Data** — donnée trop ancienne pour être considérée fiable pour la décision.
44. **Gap** — perte détectée dans une séquence de messages.
45. **Recovery** — mécanisme de reconstitution après perte/déconnexion.
46. **Drop Copy** — flux indépendant de copie d'ordres/exécutions.
47. **Reconciliation** — rapprochement de sources pour restaurer un état cohérent.
48. **FIX** — famille de standards de messagerie Financial Information eXchange.
49. **FIXT** — profil/session séparant historiquement session et version applicative.
50. **FIXP** — session haute performance de la famille FIX.
51. **SBE** — Simple Binary Encoding.
52. **SOFH** — Simple Open Framing Header.
53. **Session** — relation logique durable entre pairs avec état/protocole.
54. **Connection** — connexion transport pouvant être recréée au cours d'une session.
55. **Sequence Number** — numéro permettant ordre, détection de gap et recovery.
56. **Latency** — délai entre événements mesurés.
57. **Jitter** — variation de latence.
58. **p99** — percentile sous lequel se trouvent 99 % des mesures.
59. **Colocation** — hébergement proche ou dans l'infrastructure de la venue pour réduire distance et variabilité.
60. **Clock Synchronisation** — alignement des horloges avec une référence afin de rendre les timestamps cohérents et auditables.
