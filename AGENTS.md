# Directives Permanentes d'Organisation & Rigueur Mathématique (erdos-problems)

Ce document régit les règles d'architecture, de rangement et de rigueur scientifique pour tout agent ou collaborateur intervenant sur ce dépôt.

---

## 1. Invariant de Propreté de la Racine
- **INTERDICTION** de créer ou laisser des scripts (`.py`, `.sh`), des tests (`test_*.py`) ou des fichiers `.lean` à la racine du dépôt.
- Tous les scripts utilitaires (générateurs, extracteurs, benchmarks) doivent être placés dans `scripts/`.
- Tous les tests automatisés doivent être placés dans `tests/`.
- Tous les fichiers sources formels Lean 4 doivent être placés dans `test_lean/`.

---

## 2. Taxonomie Tripartite des Conjectures
- **`resolved/`** : Réservé EXCLUSIVEMENT aux conjectures résolues dans la littérature scientifique par la communauté mathématique mondiale (ex. Terence Tao, Granville-Ramaré, Kang et al.) ou officiellement validées par les pairs.
- **`preprints/`** : Contient nos travaux et résolutions originales prêts pour soumission (avec article LaTeX au format arXiv, PDF compilé, code Lean 4 et README explicatif).
- **`inprogress/`** : Conjectures en cours d'exploration, de calculs ou d'ébauche.

---

## 3. Standard de Preuve Formelle 100% Lean 4
- Toute preuve affirmant une fiabilité de 100% doit être vérifiée sans exception par le compilateur Lean 4 (`lake env lean <fichier>.lean`) avec **0 `sorry`**, **0 erreur**, **0 avertissement** et **0 axiome ad hoc**.
- Chaque article associé dans `preprints/` doit être rigoureusement documenté en anglais (style arXiv) et compilé en PDF avec `pdflatex`.
