# Conjecture d'Erdős-Turán sur les Bases Additives

Ce répertoire contient des ressources et des preuves en cours concernant la conjecture d'Erdős-Turán sur les bases additives.

## Statut

**Statut :** En cours. Ce problème demeure une question ouverte en mathématiques.

## Énoncé du Problème

Soit $\mathcal{A} \subseteq \mathbb{N}$ un ensemble d'entiers naturels. La fonction de représentation d'ordre 2, notée $r_{\mathcal{A}}(n)$, compte le nombre de façons d'exprimer un entier naturel $n$ comme la somme de deux éléments de $\mathcal{A}$.

L'ensemble $\mathcal{A}$ est appelé une **base additive d'ordre 2** s'il existe une constante $N_0 \ge 0$ telle que pour tout $n \ge N_0$, $r_{\mathcal{A}}(n) \ge 1$.

**Conjecture (Erdős-Turán) :** Si $\mathcal{A}$ est une base additive d'ordre 2, alors $\limsup_{n \to \infty} r_{\mathcal{A}}(n) = \infty$.

## Contenu

- `92-Erdos-Turan-Additive-Bases.fr.tex` & `.pdf` : Analyse mathématique formalisée et lemmes intermédiaires détaillant une approche partielle utilisant des séries génératrices.
