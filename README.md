# 🏢 Leyton — Plateforme IA de Gestion Documentaire

> Projet Innovation — Groupe B002

## 📌 Problématique

Leyton collecte des documents clients via des échanges manuels (emails, relances).  
Il n'y a aucune visibilité en temps réel sur ce qui manque ou ce qui est incorrect,  
ce qui ralentit fortement le delivery des consultants.

## 🎯 Objectif

Concevoir une plateforme où le client dépose l'ensemble de ses documents via une **dropzone**.  
L'IA analyse automatiquement chaque document pour :

1. **L'extraire** — lire et comprendre le contenu
2. **Le classifier** — identifier le type de document
3. **Valider sa conformité qualité** — vérifier s'il est correct et complet
4. **Détecter les pièces manquantes** — identifier ce qu'il reste à fournir

Le client est informé **en temps réel** des documents à fournir ou à corriger,  
sans intervention manuelle du consultant.

## 🗂️ Structure du Projet

```
leyton-doc-platform/
├── frontend/          # Interface React (dropzone, dashboard, notifications)
├── backend/           # API FastAPI + moteur IA
│   ├── ocr/           # Extraction de contenu (OCR)
│   ├── classifier/    # Classification des documents
│   ├── validator/     # Validation conformité
│   └── notifier/      # Système de notifications automatiques
├── docs/              # Documentation, cahier des charges, maquettes
└── tests/             # Tests unitaires et d'intégration
```

## 👥 Équipe

- Hamza Bouhani
- Zouhair IMAD
- *(membres à compléter)*

## 🛠️ Stack Technique

| Composant | Technologie |
|---|---|
| Frontend | React + react-dropzone |
| Backend | FastAPI (Python) |
| OCR / Parsing | PyMuPDF, pdfplumber |
| IA / Classification | OpenAI API |
| Notifications | SMTP / SendGrid |
| Base de données | PostgreSQL |

## 🚀 Lancement rapide

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm start
```

## 📅 Planning

| Phase | Description | Statut |
|---|---|---|
| 1 | Cadrage & Analyse | 🔄 En cours |
| 2 | Conception | ⏳ À venir |
| 3 | Développement | ⏳ À venir |
| 4 | Tests & Validation | ⏳ À venir |
| 5 | Livraison | ⏳ À venir |
