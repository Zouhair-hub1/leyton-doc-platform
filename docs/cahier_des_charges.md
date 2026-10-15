# Cahier des Charges — Leyton Plateforme Documentaire

## 1. Contexte
Leyton collecte des documents clients via des échanges manuels (emails, relances).
Aucune visibilité en temps réel sur les manquants ou incorrects.

## 2. Objectifs
- Automatiser la collecte et l'analyse des documents clients
- Réduire le temps de traitement consultant
- Informer le client en temps réel

## 3. Fonctionnalités attendues

### Côté Client
- [ ] Dépôt de documents via dropzone
- [ ] Vue du statut de son dossier (complet / incomplet)
- [ ] Réception de notifications automatiques

### Côté Système IA
- [ ] Extraction du contenu des documents (OCR)
- [ ] Classification automatique par type
- [ ] Validation de conformité (règles métier)
- [ ] Détection des pièces manquantes

### Côté Consultant
- [ ] Tableau de bord des dossiers clients
- [ ] Alertes sur dossiers bloquants
- [ ] Accès aux documents validés

## 4. Contraintes
- Respect RGPD (données clients sensibles)
- Sécurisation des uploads
- Performance : analyse < 30 secondes par document

## 5. À compléter après réunion Leyton
- Liste exacte des types de documents traités
- Règles de conformité par type
- Intégration avec outils existants
