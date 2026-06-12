[🇬🇧 English Version](README.md)

# 08 - Conjecture d'Erdős-Szekeres (Le Problème de la Fin Heureuse)

## 1. Introduction et Définitions Axiomatiques

La conjecture d'Erdős-Szekeres, issue de l'article fondateur de 1935, est un problème central de la géométrie discrète et de la théorie de Ramsey. Elle affirme que pour tout entier $n \ge 3$, il existe un entier minimal $ES(n)$ tel que tout ensemble de $ES(n)$ points dans le plan réel $\mathbb{R}^2$ en position générale (c'est-à-dire, sans trois points alignés) contient un sous-ensemble de $n$ points qui forment les sommets d'un polygone convexe à $n$ côtés.

**Définition 1.1 (Position Générale)**
Un ensemble fini de points $S \subset \mathbb{R}^2$ est en position générale si pour tous points distincts $p, q, r \in S$, les points $p, q, r$ ne sont pas colinéaires. Formellement, leur déterminant est non nul :
$\det \begin{pmatrix} p_x & q_x & r_x \\ p_y & q_y & r_y \\ 1 & 1 & 1 \end{pmatrix} \neq 0$

**Définition 1.2 (Ensemble Convexe de Points)**
Un sous-ensemble de points $P \subset S$ de taille $|P| = n$ forme un $n$-gone convexe si aucun des points de $P$ n'est contenu dans l'enveloppe convexe des $n-1$ autres points de $P$.

**Conjecture 1.3 (Erdős-Szekeres)**
Pour tout $n \ge 3$, le nombre minimum exact de points requis est donné par :
$ES(n) = 2^{n-2} + 1$

## 2. Littérature Contextuelle et Analogie

Le résultat fondateur d'Erdős et Szekeres a établi que $ES(n)$ est fini et a fourni la borne supérieure quantitative $\binom{2n-4}{n-2} + 1$. Les avancées ultérieures ont progressivement réduit l'écart entre les bornes supérieures et inférieures connues. La meilleure borne supérieure actuelle, due à Andrew Suk (2017), établit que $ES(n) \le 2^{n + o(n)}$, obtenue en traduisant le problème géométrique dans un cadre combinatoire abstrait utilisant des arrangements de pseudo-lignes et la théorie de Ramsey des hypergraphes.

Une analogie explicite peut être tracée avec le théorème de Dirichlet sur les nombres premiers dans les progressions arithmétiques, où l'existence de structures spécifiques est garantie globalement, mais où la limitation de leur distribution exacte nécessite des bornes analytiques profondes. Ici, la structure est géométriquement forcée à mesure que la cardinalité augmente. La méthode d'isolation des 'Cups' (Tasses) et 'Caps' (Casquettes) est structurellement analogue à l'isolation de séquences croissantes ou décroissantes dans le théorème d'Erdős-Szekeres sur les permutations.

## 3. Stratégie de Preuve et Isolation de Lemmes

La preuve de la borne supérieure générale procède en démontrant une structure combinatoire plus contrainte basée sur les orientations. Nous décomposons la stratégie en deux lemmes intermédiaires fondamentaux.

### Lemme 1 : L'Analogue de la Sous-séquence Monotone (Cups et Caps)
Nous définissons $f(k, l)$ comme le nombre minimum de points en position générale tel que tout ensemble de $f(k,l)$ points dont les abscisses sont distinctes contienne soit un $k$-cup (séquence convexe) soit un $l$-cap (séquence concave).
Nous prouvons la récurrence exacte $f(k, l) = f(k-1, l) + f(k, l-1) - 1$, qui établit une borne supérieure binomiale.

*Stratégie pour le Lemme 1 :* Nous utilisons une double induction sur $k$ et $l$. En supposant que l'énoncé est vrai pour des valeurs plus petites, nous partitionnons les configurations de points extrémaux et appliquons le Principe des Tiroirs pour forcer soit une extension de cup, soit une extension de cap, en écrivant strictement toutes les frontières de coordonnées sans sauts logiques.

### Lemme 2 : Convexité Géométrique à partir des Cups et Caps
Nous prouvons que si un ensemble de points contient un $n$-cup ou un $n$-cap, il contient nécessairement un $n$-gone convexe.

*Stratégie pour le Lemme 2 :* Il s'agit d'une équivalence géométrique directe cartographiant la définition fonctionnelle des cups/caps (basée sur les pentes) vers la propriété invariante affine de convexité, établie en analysant les angles intérieurs des polygones formés.

## 4. Architecture pour l'Autoformalisation (Lean 4 Proof Sketch)

Une architecture stricte et typée est établie pour la vérification formelle, garantissant que tous les indices, bornes et propriétés (comme la position générale) sont méticuleusement suivis sans hypothèses visuelles. La formalisation s'appuie fortement sur `Mathlib.Geometry.Euclidean.Basic` mais construit des prédicats personnalisés pour les cups et caps.
