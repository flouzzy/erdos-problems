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

---

## 4. Standards de Rédaction Académique & Pédagogie (Style Terence Tao)
- **Titres Mathématiques Directs et Épurés** : Le titre principal d'un article dans `preprints/` doit être rigoureusement centré sur la conjecture ou le problème mathématique lui-même (ex. *"On the Erdős Conjecture on Consecutive Powerful Numbers"*), et non formulé sous forme de log technique d'informatique. La certification Lean 4 est précisée dans le sous-titre, l'abstract et la section dédiée.
- **Démonstrations Intégrales sans Ellipse** : Chaque lemme, corollaire et théorème doit être démontré étape par étape, sans raccourci ni omission calculatoire.
- **Profondeur & Pédagogie Monographique** : Les manuscrits doivent adopter une structure riche et didactique (table des matières, contexte historique, exemples numériques détaillés, liens avec les grandes conjectures contemporaines telles que l'hypothèse $abc$ ou le théorème de Szemerédi-Trotter).
- **Métadonnées de Publication (Zenodo / arXiv)** : Pour toute soumission externe, préparer des résumés structurés en HTML riche avec équations LaTeX/MathJax, garanties de vérification formelle (0 `sorry`), classification MSC et références bibliographiques complètes.

