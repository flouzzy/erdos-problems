# 142 - Conjecture d'Erdős–Turán sur les bases additives

[English](README.md)

## Énoncé
La conjecture d'Erdős-Turán sur les bases additives (1941) stipule que si $B$ est une base additive asymptotique d'ordre 2, alors la fonction de représentation $r_{B,2}(n)$ ne peut pas être bornée. En d'autres termes, si chaque entier $n$ suffisamment grand peut être exprimé comme la somme de deux éléments de $B$, alors le nombre de telles représentations doit être non borné :
$$ \limsup_{n \to \infty} r_{B,2}(n) = \infty $$

## Statut Actuel
Ce problème est actuellement **en cours**.

Une architecture de preuve partielle et rigoureuse ciblant les systèmes de vérification formelle comme Lean 4 a été structurée. Le document établit des types axiomatiques stricts, explore les limites probabilistes, et prouve définitivement la contrainte structurelle de densité fondamentale sans ellipses logiques.

[Voir l'Architecture de Preuve (PDF)](142-Erdos-Turan-Additive-Bases.fr.pdf)
