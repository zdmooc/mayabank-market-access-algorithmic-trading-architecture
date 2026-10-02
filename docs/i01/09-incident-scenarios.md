# I01 — Dix scénarios d'incident

## S01 — Rejet pré-trade
Un ordre dépasse une limite de notionnel.
- Attendu : aucun message venue.
- Questions : quelle règle ? quelle version ? quelle preuve ?

## S02 — Venue Reject
L'ordre passe les contrôles internes mais la venue le rejette.
- Attendu : statut REJECTED côté OMS.
- Questions : comment préserver le motif et distinguer ce rejet du risk reject ?

## S03 — Cancel croisé avec Fill
Le trader annule, mais la venue exécute avant de traiter le cancel.
- Attendu : FILLED + Cancel Reject ou séquence équivalente selon venue.
- Risque : croire à tort que CANCEL_PENDING = CANCELED.

## S04 — Déconnexion après envoi, avant acknowledgement
Le gateway envoie l'ordre puis perd la connexion.
- État local : ambigu.
- Attendu : ne pas renvoyer aveuglément ; passer par recovery/reconciliation.

## S05 — Exécution présente en Drop Copy mais absente du flux principal
- Risque : position sous-estimée.
- Attendu : alerte, gel de l'ordre, réconciliation.

## S06 — Market Data stale
Le SOR reçoit un prix trop ancien.
- Attendu : arrêter/réduire routing selon politique.
- Risque : exécuter sur une hypothèse de marché obsolète.

## S07 — Sequence gap sur flux Market Data ou session d'ordre
- Attendu : détecter le gap et déclencher le mécanisme adapté.
- I01 : savoir expliquer le risque métier.
- I02 : savoir détailler le recovery FIX.

## S08 — Venue throttling
Le rythme d'ordres dépasse une limite.
- Attendu : throttling local, queue bornée, rejet contrôlé ou dégradation.
- Risque : accumulation et explosion de latence.

## S09 — Clock drift
Les timestamps des composants divergent.
- Risque : causalité impossible à reconstruire, métriques de latence fausses, audit dégradé.
- Attendu : alerte, mesure d'offset, procédure de correction.

## S10 — Kill switch sélectif
Une stratégie ou un trader doit être stoppé sans fermer toutes les routes.
- Attendu : identifier tous les ordres non exécutés du périmètre, envoyer les cancels, tracer le résultat et empêcher de nouveaux ordres du même périmètre.

## Exercices oraux

Pour chaque scénario, expliquer :
1. l'événement déclencheur ;
2. l'état local ;
3. l'état venue potentiel ;
4. le risque ;
5. l'action immédiate ;
6. la preuve nécessaire ;
7. la condition de reprise.
