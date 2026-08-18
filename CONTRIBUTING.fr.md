[🇬🇧 English Version](CONTRIBUTING.md)

# Contribuer aux Problèmes d'Erdős

Merci de votre intérêt pour le projet **Problèmes d'Erdős** ! Ce document définit les directives d'organisation du dépôt, les exigences de preuve formelle et le flux de contribution.

---

## 🌐 Exigence de Bilinguisme

Ce dépôt est strictement bilingue :
- **Anglais** est la langue par défaut (`.md`).
- Les traductions en **Français** doivent être fournies pour chaque document et énoncé de problème (`.fr.md`).

---

## 📂 Structure du Dépôt & Règle de Propreté

Afin de maintenir un dépôt structuré et conforme aux standards académiques, toutes les contributions doivent respecter l'architecture définie dans [`ARCHITECTURE.fr.md`](ARCHITECTURE.fr.md) :

1. **`preprints/`** : Pour les résolutions originales, réductions structurelles et certificats formels Lean 4 prêts pour soumission/publication.
2. **`resolved/`** : Pour les problèmes intégralement résolus par la communauté mathématique mondiale dans la littérature scientifique à comité de lecture.
3. **`inprogress/`** : Pour les recherches en cours et ébauches de preuves.
4. **`scripts/`** : Tous les scripts automatisés, générateurs et benchmarks (aucun script à la racine).
5. **`tests/`** : Tous les fichiers de tests unitaires (`test_*.py`). Aucun test ne doit être placé à la racine.
6. **`test_lean/`** : Tous les fichiers sources Lean 4 et dépendances Mathlib.

---

## 📐 Rigueur Mathématique & Vérification Formelle en Lean 4

Ce projet applique les plus hauts standards de rigueur scientifique :

1. **Politique Zéro-Sorry :** Tout théorème formalisé doit compiler avec **0 `sorry`**, **0 axiome ad hoc**, et être validé sans erreur par le noyau Lean 4 (`lake env lean <fichier>.lean`).
2. **Publications LaTeX Standardisées :** Chaque sous-dossier de `preprints/` doit contenir un manuscrit LaTeX autonome (`.tex`) et son PDF compilé (`.pdf`) au format arXiv.
3. **Typage et Fondements Axiomatiques :** Tous les objets mathématiques, bornes, indices et hypothèses doivent être explicitement typés et démontrés.
