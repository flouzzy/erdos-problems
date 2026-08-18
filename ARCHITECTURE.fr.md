[🇬🇧 English Version](ARCHITECTURE.md)

# Architecture du Dépôt & Standards d'Organisation

Ce document définit les règles d'architecture logicielle, la taxonomie des répertoires et les invariants d'organisation pour le dépôt `erdos-problems`.

---

## 🏛️ Taxonomie des Répertoires

```
erdos-problems/
├── README.md & README.fr.md          # Présentation globale bilingue du projet
├── CONTRIBUTING.md & .fr.md          # Guide de contribution et standards formels
├── ARCHITECTURE.md & .fr.md          # Spécification architecturale et organisationnelle
├── LICENSE & .gitignore              # Métadonnées du projet et filtres Git
│
├── preprints/                        # Travaux originaux & certificats de preuve formelle prêts pour soumission
│   ├── 108-Erdos-Straus/             # Manuscrit (.tex), PDF compilé (.pdf), code Lean 4, documentation
│   ├── 14-Erdos-Distinct-Sums/
│   ├── 11-Erdos-Moser/
│   ├── 35-Erdos-Szemeredi-Sum-Product/
│   └── 68-Erdos-Rado-Sunflower/
│
├── resolved/                         # Conjectures résolues par la communauté mathématique mondiale (Tao, Granville, etc.)
│   ├── 01-Erdos-Discrepancy/
│   ├── 03-Erdos-Faber-Lovasz/
│   ├── 22-Erdos-Squarefree/
│   └── ...
│
├── inprogress/                       # Conjectures en cours d'exploration et de recherche
│
├── test_lean/                        # Environnement Lean 4 (Mathlib) pour vérification formelle (0 sorry)
│
├── scripts/                          # Outils utilitaires Python et Bash (générateurs, extracteurs, benchmarks)
│
├── tests/                            # Suite de tests automatisés (Python unittest / pytest)
│
└── templates/                        # Modèles LaTeX et Markdown réutilisables
```

---

## 🔒 Invariants d'Organisation

1. **Règle de Propreté de la Racine :**
   * Aucun script (`.py`, `.sh`), fichier de test épars (`test_*.py`), ou fichier `.lean` isolé n'est toléré à la racine du dépôt.
   * Tous les scripts doivent être situés dans `scripts/`.
   * Tous les tests unitaires doivent être situés dans `tests/`.
   * Tous les modules Lean 4 doivent être situés dans `test_lean/`.
2. **Classification Tripartite des Problèmes :**
   * **`resolved/`** : Strictement réservé aux conjectures résolues dans la littérature scientifique à comité de lecture ou officiellement validées par les pairs.
   * **`preprints/`** : Réservé aux nouvelles formulations, réductions structurelles et certificats formels Lean 4 originaux prêts pour soumission à des revues ou à arXiv.
   * **`inprogress/`** : Réservé aux recherches en cours et ébauches de formalisation.
3. **Exigence de Bilinguisme :**
   * Chaque document structurant doit exister en version anglaise (`.md`) et en version française (`.fr.md`).
4. **Standard de Certification Formelle :**
   * Toute preuve affirmant une fiabilité de $100\%$ doit être validée par le compilateur Lean 4 avec $0$ `sorry` et $0$ axiome ad hoc via la commande `lake env lean <fichier>.lean`.
