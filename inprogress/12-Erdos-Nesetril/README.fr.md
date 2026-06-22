[🇬🇧 English Version](README.md)

# 12 - Conjecture d'Erdos-Nesetril

## Énoncé
La conjecture d'Erdős-Nešetřil (1985) stipule que pour tout graphe simple $G$ de degré maximum $\Delta$, l'indice chromatique fort de $G$, noté $sq(G)$, est borné par :
- $sq(G) \le \frac{5}{4}\Delta^2$ si $\Delta$ est pair.
- $sq(G) \le \frac{1}{4}(5\Delta^2 - 2\Delta + 1)$ si $\Delta$ est impair.

L'indice chromatique fort est le nombre minimum de couleurs nécessaires pour colorer les arêtes d'un graphe de sorte qu'aucune arête ne partage un sommet ou ne soit adjacente à une arête commune avec une arête de la même couleur. Ce problème trouve des applications très concrètes dans l'allocation de fréquences pour les réseaux sans fil, où l'évitement des interférences correspond exactement à la coloration forte des arêtes.

## Statut Actuel
Ce problème est actuellement **en cours**.

Nous avons formulé une esquisse de preuve partielle robuste établissant des bornes supérieures pour les chemins, les arbres et les cycles de longueur paire. Une analyse combinatoire exhaustive a été réalisée sur des centaines de topologies de graphes distinctes pour satisfaire strictement aux exigences d'inégalité.

Un document mathématique détaillé contenant des définitions axiomatiques strictes, le contexte et des preuves sans ellipse pour les lemmes clés a été préparé.

[Voir la Preuve et l'Analyse (PDF)](12-proof.pdf)