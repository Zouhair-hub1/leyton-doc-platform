# 🌳 Arbre de Travail Complet — Leyton Plateforme Documentaire

---

## Vue d'ensemble

```
LEYTON — Plateforme IA de Collecte Documentaire
│
├── 1. CADRAGE & ANALYSE
├── 2. MODÉLISATION (Documents CIR/CII)
├── 3. PIPELINE IA
├── 4. INTERFACE CLIENT (Frontend)
├── 5. WORKFLOW & STATUTS
├── 6. REPORTING & MESSAGERIE
├── 7. ADMINISTRATION
└── 8. TESTS & LIVRAISON
```

---

## Arbre Détaillé

```
LEYTON — Plateforme IA de Collecte Documentaire
│
├── 1. CADRAGE & ANALYSE
│   ├── 1.1 Réunion de lancement avec Leyton ✅
│   ├── 1.2 Identification des types de documents CIR/CII
│   │   ├── Fiches de paie
│   │   ├── Feuilles de temps
│   │   ├── Factures fournisseurs / brevets
│   │   ├── Déclaration fiscale 2069-A
│   │   ├── CR de réunion R&D
│   │   ├── Description projet R&D / état de l'art
│   │   └── Récapitulatif des dépenses (CII)
│   ├── 1.3 Mapping du workflow actuel consultant ↔ client
│   └── 1.4 Rédaction du cahier des charges fonctionnel
│
├── 2. MODÉLISATION — Référentiel Documents CIR/CII
│   ├── 2.1 Définir la checklist CIR (15 types de documents)
│   │   ├── Partie Administrative & Financière (8 types)
│   │   └── Partie Technique (5 types)
│   ├── 2.2 Définir la checklist CII (7 types de documents)
│   ├── 2.3 Définir les règles de conformité par type
│   │   ├── Format accepté (PDF, JPG, PNG...)
│   │   ├── Informations obligatoires (date, signature, montant...)
│   │   └── Règles métier spécifiques (ex: fiche de paie = nom + période)
│   └── 2.4 Modélisation base de données (schéma)
│
├── 3. PIPELINE IA (Backend)
│   ├── 3.1 Module OCR — Extraction du contenu
│   │   ├── Parsing PDF (pdfplumber / PyMuPDF)
│   │   ├── OCR images (Tesseract)
│   │   └── Contrôle lisibilité du document
│   │
│   ├── 3.2 Module Classifier — Classification par type
│   │   ├── Appel OpenAI API avec le contenu extrait
│   │   ├── Retour : type_document + score_confiance
│   │   └── Mapping vers checklist CIR ou CII
│   │
│   ├── 3.3 Module Validator — Validation conformité
│   │   ├── Vérification des règles métier (dates, montants, signatures)
│   │   ├── Inférence contextuelle (incohérences détectées)
│   │   ├── Statut : Validé / Rejeté / Cas douteux
│   │   └── Score de confiance visible (pas de boîte noire)
│   │
│   └── 3.4 Module Détection Manquants
│       ├── Comparaison documents reçus vs checklist attendue
│       └── Génération liste des pièces manquantes
│
├── 4. INTERFACE CLIENT (Frontend React)
│   ├── 4.1 Page Dropzone
│   │   ├── Upload par drag & drop
│   │   ├── Sélection CIR ou CII
│   │   └── Feedback immédiat (fichier reçu / en traitement)
│   │
│   ├── 4.2 Tableau de bord dossier
│   │   ├── Liste des documents déposés avec statut
│   │   │   ├── ✅ Validé
│   │   │   ├── ❌ Rejeté (motif affiché)
│   │   │   ├── ⚠️  En attente de vérification humaine
│   │   │   └── 🔴 Manquant
│   │   ├── Barre de progression (% dossier complet)
│   │   └── Score de confiance IA affiché par document
│   │
│   └── 4.3 Page Notifications
│       ├── Historique des alertes reçues
│       └── Lien direct vers les pièces à corriger
│
├── 5. WORKFLOW & STATUTS
│   ├── 5.1 Orchestration des statuts par document
│   │   └── Manquant → En attente → Validé / Rejeté
│   ├── 5.2 Gestion des cas douteux
│   │   └── File d'attente consultant pour vérification humaine
│   └── 5.3 Module Admin — Paramétrage de nouveaux produits
│       ├── Créer un nouveau type de dossier (ex: JEI)
│       ├── Configurer la checklist de documents attendus
│       └── Définir les règles de conformité associées
│
├── 6. REPORTING & MESSAGERIE AUTOMATIQUE
│   ├── 6.1 Génération de rapports (synthèse des contrôles)
│   ├── 6.2 Classification des anomalies
│   │   ├── Document manquant
│   │   ├── Document illisible
│   │   ├── Document non conforme (dates incohérentes...)
│   │   └── Montant suspect
│   └── 6.3 Envoi email automatique au client
│       ├── "Il manque : fiche de paie janvier, CR réunion R&D..."
│       └── Lien vers la plateforme pour déposer les pièces manquantes
│
├── 7. PRÉDICTION (Bonus si temps)
│   ├── 7.1 Prédiction des anomalies probables
│   ├── 7.2 Score de risque : dossier incomplet
│   └── 7.3 Estimation du délai de traitement
│
└── 8. TESTS & LIVRAISON
    ├── 8.1 Jeu de documents synthétiques / anonymisés
    ├── 8.2 Tests unitaires pipeline IA
    ├── 8.3 Tests end-to-end (dépôt → notification)
    ├── 8.4 Validation avec consultant Leyton
    ├── 8.5 Mesure du gain de temps vs processus actuel
    └── 8.6 Démo finale + documentation
```

---

## 📅 Répartition sur 5 jours

| Jour | Tâches prioritaires |
|---|---|
| **J1** | Cadrage (1.1→1.4) + Modélisation CIR/CII (2.1→2.3) |
| **J2** | Pipeline IA : OCR + Classifier (3.1→3.2) |
| **J3** | Pipeline IA : Validator + Manquants (3.3→3.4) |
| **J4** | Frontend Dropzone + Dashboard (4.1→4.2) + Notifications (6.3) |
| **J5** | Tests (8.1→8.5) + Démo finale (8.6) |
