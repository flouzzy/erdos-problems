[🇬🇧 English Version](README.md)

# La Conjecture d'Erdős-Turán sur les Bases Additives

**Statut : En cours (Solutions partielles et fondations)**

## 1. Introduction
La conjecture d'Erdős-Turán sur les bases additives est un problème ouvert central de la théorie additive des nombres. Formulée par Paul Erdős et Pál Turán en 1941, elle propose une propriété structurelle profonde concernant la densité et le chevauchement des représentations des sous-ensembles d'entiers naturels qui forment des bases additives.

Intuitivement, si un ensemble de nombres est suffisamment "riche" pour que tout grand nombre puisse être écrit comme la somme de deux éléments de l'ensemble, alors certains nombres doivent inévitablement pouvoir être représentés de nombreuses manières différentes. Il ne peut exister de base additive d'ordre 2 parfaitement efficace.

## 2. Définitions Axiomatiques

Afin d'étudier cette conjecture avec une rigueur absolue, nous fournissons la formalisation stricte suivante.

**Définition 2.1 (Sous-ensembles et Typage)**
Soit $\mathbb{N}$ l'ensemble des entiers naturels.
Soit $B$ un sous-ensemble d'entiers naturels, formellement $B \subseteq \mathbb{N}$ ou $B \in \mathcal{P}(\mathbb{N})$.

**Définition 2.2 (Fonction de Représentation)**
Nous définissons la fonction de représentation $r_B: \mathbb{N} \to \mathbb{N} \cup \{\infty\}$ qui compte le nombre de façons dont un entier $n$ peut être exprimé comme la somme de deux éléments de $B$.
Strictement :
$$r_B(n) = \text{card}(\{(a, b) \in B^2 \mid a + b = n\})$$
où $a, b \in B$ et l'ordre a de l'importance (c'est-à-dire que $(a,b)$ et $(b,a)$ sont comptés comme distincts si $a \neq b$).

**Définition 2.3 (Base Additive Asymptotique d'Ordre 2)**
L'ensemble $B$ est défini comme une base additive asymptotique d'ordre 2 si tout entier suffisamment grand peut être représenté comme la somme de deux éléments de $B$. Formellement :
$$\exists N \in \mathbb{N}, \forall n \in \mathbb{N}, n \ge N \implies r_B(n) > 0$$

## 3. Énoncé Formel de la Conjecture

**Conjecture d'Erdős-Turán :**
Pour toute base additive asymptotique $B$ d'ordre 2, la suite des représentations $(r_B(n))_{n \in \mathbb{N}}$ ne peut pas être bornée. Formellement :
$$\limsup_{n \to \infty} r_B(n) = \infty$$
Ou de manière équivalente :
$$\forall M \in \mathbb{N}, \exists n \in \mathbb{N} \text{ tel que } r_B(n) > M$$

## 4. Approche et Travaux en Cours

Ce dossier contient une analyse mathématique détaillée et une réduction structurelle du problème, proposant une preuve rigoureuse étape par étape de théorèmes de densité partiels liés à cette conjecture.
Nous fournissons également une architecture pour l'autoformalisation, structurant les lemmes pour qu'ils soient facilement vérifiables dans l'assistant de preuve formelle **Lean 4**.

Un document PDF détaillé contenant les démonstrations exhaustives est maintenu à la racine de ce dossier.
