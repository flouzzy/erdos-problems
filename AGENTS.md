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

## 3. Standard de Preuve Formelle 100% Lean 4 & Règles Mathlib
- Toute preuve affirmant une fiabilité de 100% doit être vérifiée sans exception par le compilateur Lean 4 (`lake env lean <fichier>.lean`) avec **0 `sorry`**, **0 erreur**, **0 avertissement** et **0 axiome ad hoc**.
- **Arithmétique rationnelle (`ℚ` / `Rat`)** : Utiliser impérativement `norm_num` (ou `ring`) pour toute égalité ou inégalité sur `ℚ`, car `decide` échoue à réduire le type `Decidable` des rationnels dans le noyau Lean 4.
- **Structures d'opérateurs polynomiaux** : Utiliser `[CommRing R]` avec la tactique `ring` pour les calculs dans les sous-anneaux polynomiaux, ou `noncomm_ring` dans le cadre non-commutatif.
- **Racines de monômes & puissances** : Utiliser `by_contra` et `pow_ne_zero d hx` pour démontrer l'unicité des racines non nulles dans un anneau intègre.

---

## 4. Standards de Rédaction Académique & Soumission aux Comités de Lecture (Peer-Review)
- **Format Monographique Approfondi (5 à 10+ pages)** : Tout article destiné à `preprints/` ou `resolved/` doit être rédigé sous la forme d'un traité scientifique complet et autonome (*self-contained*), avec table des matières, contexte historique, lemmes intermédiaires, théorèmes principaux et perspectives.
- **Démonstrations Intégrales sans Ellipse** : Chaque lemme, corollaire et théorème doit être démontré étape par étape, sans raccourci ni omission calculatoire.
- **Certification Formelle Lean 4 à l'Appui (0 `sorry`, 0 axiome)** : Toute soumission doit être accompagnée de son fichier `.lean` compilant avec succès via le noyau Lean 4 et Mathlib, fournissant au comité d'évaluation une preuve informatique infaillible et reproductible.
- **Titres Mathématiques Directs et Épurés** : Le titre principal d'un article dans `preprints/` doit être rigoureusement centré sur la conjecture ou le problème mathématique lui-même (ex. *"On the Erdős Conjecture on Consecutive Powerful Numbers"*), et non formulé sous forme de log technique d'informatique. La certification Lean 4 est précisée dans le sous-titre, l'abstract et la section dédiée.
- **Interdiction de l'étiquetage méta de style** : Ne JAMAIS mentionner "style Terence Tao" ou "(style Terence Tao)" dans les titres, textes, READMEs ou communications. Le style rigoureux, didactique et non-elliptique doit être appliqué naturellement sans étiquetage superflu.
- **Illustrations et Diagrammes Géométriques Pertinents (TikZ & tikz-cd)** : 
  - Inclure systématiquement des schémas géométriques, diagrammes commutatifs (`tikz-cd`), arbres combinatoires ou graphes de cribles/densités lorsque cela éclaire la combinatoire ou l'arithmétique de la démonstration.
  - Veiller à la robustesse syntaxique (ex. grouper par accolades `{...}` les étiquettes complexes dans `tikzcd` contenant des virgules ou symboles mathématiques).
- **Conformité Stricte aux Standards de Publication Académique Pure (AMS / Annals of Mathematics)** :
  - **Symbole de Halmos $\blacksquare$** : Utiliser impérativement `\renewcommand{\qedsymbol}{\ensuremath{\blacksquare}}` pour marquer clairement la complétion de chaque démonstration en fin d'environnement `\begin{proof} ... \end{proof}`.
  - **Proscription du Formatage et Vocabulaire Corporatif** : Ne JAMAIS inclure de « Tableau Récapitulatif Exécutif » ou de terminologie managériale/entreprise. Les résultats majeurs sont annoncés dans l'Introduction (*Section 1 : Introduction and Main Results*).
  - **Section Conclusive Académique** : Intituler sobrement la dernière section *« Concluding Remarks and Open Problems »* (ou *« Perspectives and Open Directions »*) pour discuter des obstructions mathématiques fondamentales, des questions ouvertes et des horizons de formalisation interactive.
- **Préparation Complète pour l'Évaluation par les Pairs** : Fournir systématiquement le PDF compilé via `pdflatex`, le code source `.tex`, le fichier de test `.lean`, ainsi que les métadonnées de dépôt (`presentation.md` avec classification MSC 2020 et abstract bilingue/anglais standard).

---

## 5. Gestion Disque & Cache `.lake` Partagé
- **Liaison symbolique multi-dépôt** : Partager le cache `.lake` (~8 Go) entre dépôts via lien symbolique (`ln -s ...`) pour préserver l'espace disque du serveur.
- **`.gitignore`** : Toujours ignorer `.lake` et `test_lean/.lake` sans slash final pour éviter que Git ne suive les liens symboliques.

