[🇬🇧 English Version](README.md)

# 18 - Conjecture d'Erdős-Turán sur les Bases Additives

## Énoncé
La conjecture d'Erdős-Turán sur les bases additives, formulée en 1941, stipule que si un ensemble d'entiers naturels $B$ est une base asymptotique d'ordre 2, alors le nombre de représentations d'un entier $n$ comme somme $a + b$ (avec $a, b \in B$) ne peut pas être borné. Formellement, si $r(n) > 0$ pour tout $n$ suffisamment grand, alors $\limsup r(n) = \infty$.

## Statut Actuel
Ce problème est actuellement **en cours** (in progress).

Nous présentons une esquisse de preuve analytique exploitant l'analyse de Fourier discrète et la méthode du cercle de Hardy-Littlewood. La preuve établit une identité de Parseval rigoureuse pour la fonction de représentation et démontre que borner uniformément $r(n)$ conduit à une contradiction analytique concernant les propriétés Lipschitziennes du polynôme associé sur le cercle unité.

[Voir l'Esquisse de Preuve (PDF)](18-proof.pdf)
