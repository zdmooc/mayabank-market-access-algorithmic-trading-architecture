# Baseline transverse — réglementation, temps, protocoles et entitlements

## Statut

**REFERENCE_BASELINE — à intégrer progressivement dans I01→I12**

Ce document n'avance pas I02. Il fixe seulement les références qui doivent orienter la suite.

## 1. Regulatory / Controls

### MiFID II — Article 17
Points d'architecture :
- résilience et capacité suffisante ;
- seuils et limites ;
- prévention des ordres erronés ;
- monitoring et tests ;
- business continuity ;
- conservation des enregistrements.

Source officielle :
https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifid-ii/article-17-algorithmic-trading

### RTS 6 — Règlement délégué (UE) 2017/589
La kill functionality doit permettre l'annulation immédiate d'un ou plusieurs ordres non exécutés selon un périmètre identifiable. Le système doit pouvoir attribuer chaque ordre à son algorithme et à son trader/desk/client selon le cas.

Source officielle :
https://eur-lex.europa.eu/eli/reg_del/2017/589/oj/eng

## 2. Time Architecture

### MiFIR Article 22c
Les horloges servant à enregistrer les événements reportables doivent être synchronisées.

Source officielle :
https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifir/article-22c-synchronisation-business-clocks

### Règlement délégué (UE) 2025/1155
Les articles 11 à 16 s'appliquent depuis le **2 mars 2026**. Le règlement 2017/574 est abrogé à cette date.

Architecture à couvrir :
- UTC comme référence ;
- chaîne de traçabilité vers UTC ;
- NTP/PTP selon exigences ;
- hardware/software timestamps ;
- maximum clock offset ;
- drift/holdover ;
- point exact d'application du timestamp ;
- corrélation décision -> contrôle -> ordre -> ack -> exécution -> Drop Copy.

Source officielle :
https://eur-lex.europa.eu/eli/reg_del/2025/1155/oj/eng

## 3. Protocol Landscape

```text
Application semantics
├── Order lifecycle
├── Execution reports
├── Allocations / post-trade
└── Market data semantics

Session and reliability
├── FIX Session
├── FIXT profile
├── FIXP
└── Venue-specific session mechanisms

Encoding and framing
├── FIX TagValue
├── SBE
├── FAST
├── SOFH
└── Native binary encodings

Transport
├── TCP/TLS
├── UDP multicast
├── WebSocket where applicable
└── Venue-specific transport
```

Références FIX officielles :
- FIX Session : https://fixtrading.org/standards/fixsession/
- FIX standards / FIXP / SOFH / FIXS : https://www.fixtrading.org/online-specification/introduction/

## 4. Market Data Entitlements

À couvrir progressivement :
- user/application/service identity ;
- droits par fournisseur, venue, service et contenu ;
- real-time / delayed / snapshot / depth ;
- redistribution ;
- usage audit ;
- licence et maîtrise des coûts.

LSEG documente DACS comme système d'entitlements pour RTDS, anciennement TREP.

Références :
- DACS / RTDS : https://developers.lseg.com/en/article-catalog/article/introduction-dacs-entitlement-system-opendacs-developers
- RTDS : https://www.lseg.com/en/data-analytics/market-data/data-management/real-time-distribution-system
- RTMDS : https://www.lseg.com/en/data-analytics/market-data/data-management/real-time-managed-distribution-service

## 5. Legacy terminology

- **RTDS** : terminologie actuelle LSEG pour la plateforme anciennement TREP.
- **TREP** : legacy, utile dans le glossaire et les annonces historiques.
- **RMDS** : legacy antérieur, à ne pas présenter comme appellation courante.
- **RTMDS** : service managé LSEG à traiter dans la partie Market Data.

## Règle

Ces blocs sont transverses : ils ne sont pas repoussés à une seule itération finale. Ils doivent enrichir les livrables métier, FIX, Market Data, contrôles, time architecture, RUN et hybrid placement.
