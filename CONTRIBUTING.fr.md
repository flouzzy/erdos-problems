# Contribution aux Problèmes d'Erdős

Nous vous remercions de l'intérêt que vous portez à la contribution au **Dépôt des Problèmes d'Erdős** ! Ce document établit les directives de contribution afin de garantir que l'ensemble des énoncés, démonstrations et discussions satisfassent aux exigences de rigueur inhérentes à ce projet.

## 🌐 Exigence Bilingue

Ce dépôt est strictement bilingue.

- **L'anglais** constitue la langue par défaut (fichiers `.md`).
- Les traductions en **français** doivent être impérativement fournies pour chaque document et problème (fichiers `.fr.md`).

Lors de l'ajout ou de l'actualisation d'un problème, il convient de s'assurer que les versions dans les deux langues sont créées et maintenues synchronisées. La version française doit observer un ton mathématique académique d'une haute rigueur.

## 📂 Structure du Dépôt & Convention de Nommage

Le dépôt est structuré en trois répertoires principaux :

- `resolved/` : Destiné aux problèmes ayant été intégralement résolus.
- `inprogress/` : Destiné aux problèmes partiellement résolus ou faisant l'objet de recherches substantielles en cours.
- `todo/` : Destiné à l'ensemble des problèmes d'Erdős ouverts.

Lors de l'introduction d'un nouveau problème ou de la relocalisation d'un problème existant, la création d'un répertoire doit scrupuleusement respecter la convention de nommage suivante :
`[Numéro]-[Nom-du-Problème]`
*(par exemple, `01-Somme-des-Inverses-des-Nombres-Premiers`)*

Au sein de ce répertoire devront figurer l'ensemble des fichiers pertinents, tels que `README.md`, `README.fr.md`, ainsi que toute documentation ou démonstration annexe.

## 📐 Rigueur Mathématique et Autoformalisation

Ce dépôt se conforme à une rigueur mathématique stricte dans le but de faciliter une autoformalisation ultérieure vers Lean 4. Nous vous prions de respecter les directives suivantes :

1. **Définitions Axiomatiques Strictes :** Les propositions mathématiques doivent être traduites en définitions axiomatiques strictes. Toute variable et tout ensemble doivent faire l'objet d'un typage explicite.
2. **Absence de Raccourcis Logiques :** Il est proscrit d'employer des raccourcis logiques (souvent désignés sous le terme d'« ellipses nulles » ou « zéros points de suspension »). L'ensemble des étapes, changements d'indices, bornes et principes appliqués doivent être rédigés de manière explicite.
3. **Esquisse de Preuve (Proof Sketch) Lean 4 :** Les démonstrations doivent être structurées selon une architecture propice à l'autoformalisation. Elles doivent présenter une « Esquisse de Preuve » directement traduisible au sein de l'assistant de preuve formel Lean 4.
4. **Éléments Explicites :** Les Théorèmes, Lemmes, variables d'entrée et hypothèses doivent être clairement typés et structurés.

En vous conformant à ces directives, vous concourez à faire de ce dépôt un catalogue précis, éminemment formel et accessible des défis mathématiques posés par Paul Erdős. Nous attendons vos contributions avec grand intérêt !
