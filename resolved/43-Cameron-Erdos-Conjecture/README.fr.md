# 43 - Conjecture de Cameron-Erdos

## Énoncé du Problème

La conjecture de Cameron-Erdős stipule que le nombre de sous-ensembles sans somme de $\{1, 2, \dots, N\}$ est $O(2^{N/2})$. Un sous-ensemble $A$ est sans somme s'il n'existe pas d'éléments $x, y, z \in A$ tels que $x + y = z$.

Cette conjecture a été proposée par Peter Cameron et Paul Erdős en 1990. Elle a été prouvée indépendamment par Ben Green (2004) et Alexander Sapozhenko (2003).

## Formalisation et Stratégie de Preuve

Notre stratégie pour prouver cette conjecture comprend :
1. La définition formelle des ensembles sans somme et l'énoncé de la conjecture.
2. Une revue de la littérature contextuelle, notamment les méthodes de Green et Sapozhenko.
3. L'établissement de lemmes bornant le nombre de sous-ensembles sans somme dominés par des entiers impairs et pairs, en utilisant des bornes combinatoires et des conteneurs d'hypergraphes.
4. L'architecture de la feuille de route d'auto-formalisation à l'aide de l'assistant de preuve Lean 4.
