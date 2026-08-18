[🇬🇧 English Version](README.md)

# Problèmes d'Erdős

Ce projet a pour objectif de centraliser, organiser, formaliser et documenter les problèmes mathématiques posés par le légendaire mathématicien Paul Erdős, en fournissant des preuves certifiées par ordinateur en **Lean 4 (Mathlib)** ainsi que des prépublications académiques prêtes pour soumission.

Paul Erdős proposait des récompenses financières pour la résolution de nombre de ces conjectures, couvrant la théorie des graphes, la combinatoire additive et la théorie analytique et diophantienne des nombres.

## 🌐 Langues
Ce dépôt est principalement maintenu en **anglais** (par défaut), avec des versions françaises correspondantes (`.fr.md`).

## 📂 Structure du Dépôt

Le dépôt est organisé selon une hiérarchie stricte en fonction du statut de preuve et de validation par les pairs :

- **`resolved/`** : Contient les conjectures **intégralement résolues dans la littérature scientifique** par la communauté mathématique mondiale (ex. Terence Tao pour le problème de Discrépance d'Erdős #01, Granville-Ramaré pour les Coefficients Binomiaux sans facteur carré #22, Kang et al. pour la conjecture d'Erdős-Faber-Lovász #03, Green-Tao pour les Progressions Arithmétiques dans les Primes #43).
- **`preprints/`** : Contient les **travaux originaux, nouvelles réductions structurelles et certificats de preuve formelle Lean 4** prêts à être soumis aux comités de lecture / revues / arXiv. Chaque sous-dossier comprend le manuscrit académique (`.tex`), le PDF compilé (`.pdf`), le code source formel Lean 4 et la documentation :
  - `108-Erdos-Straus` : Théorème Maître de Réduction Modulo 24 ($95,83\%$ de densité) et Identité Universelle à 3 paramètres.
  - `14-Erdos-Distinct-Sums` : Minorations informationnelles certifiées ($\sum x \ge 2^n - 1$, $\max(S) \ge \frac{2^n - 1}{n}$).
  - `11-Erdos-Moser` : Bornes de sommes de puissances et exclusion formelle des modules $m \in \{4, 5\}$.
  - `35-Erdos-Szemeredi-Sum-Product` : Minorations discrètes de croissance des sumsets ($|A+A| \ge 2|A|-1$).
  - `68-Erdos-Rado-Sunflower` : Vérification formelle du seuil et du cas de base du Lemme des Tournesols d'Erdős-Rado.
- **`inprogress/`** : Conjectures en cours d'exploration, de recherche ou d'ébauche formelle.
- **`test_lean/`** : Environnement Lean 4 (Mathlib) contenant tous les fichiers de preuves formelles validés avec $0$ `sorry` par le noyau Lean 4 (`lake env lean <file>.lean`).

## 🤝 Comment Contribuer
Les contributions sont bienvenues ! Veuillez consulter `CONTRIBUTING.fr.md` pour les règles de formatage des preuves formelles et des papiers LaTeX.

Ce projet est sous licence open-source. Consultez le fichier `LICENSE` pour plus de détails.
