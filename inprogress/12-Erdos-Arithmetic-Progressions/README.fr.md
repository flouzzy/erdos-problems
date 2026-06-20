[🇬🇧 English Version](README.md)

# 12 - Conjecture d'Erdős sur les progressions arithmétiques

## Énoncé
La conjecture d'Erdős sur les progressions arithmétiques, souvent appelée conjecture d'Erdős-Turán, stipule que si la somme des inverses des membres d'un ensemble $A$ d'entiers strictement positifs diverge, alors $A$ contient des progressions arithmétiques de longueur arbitraire. Soit $A \subset \mathbb{N}$ tel que $\sum_{n \in A} \frac{1}{n} = \infty$. Alors, pour tout entier $k \ge 3$, il existe une progression arithmétique de longueur $k$ entièrement contenue dans $A$.

## Statut Actuel
Ce problème est actuellement **en cours** de résolution.

Nous présentons une esquisse de preuve structurelle s'appuyant sur l'analyse de Fourier discrète et les normes d'uniformité de Gowers. La conjecture globale est décomposée en lemmes intermédiaires établissant des bornes de densité et des conditions de pseudo-aléatoire, avec un accent particulier sur la traduction de ces propriétés en Lean 4 pour une autoformalisation future.

[Voir l'esquisse de preuve partielle (PDF)](12-proof.pdf)
