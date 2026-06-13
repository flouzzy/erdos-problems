[🇬🇧 English Version](README.md)

# Problème 08 - Conjecture d'Erdős-Szekeres (Le Happy Ending Problem)

## Introduction et Énoncé du Problème
La conjecture d'Erdős-Szekeres, également connue sous le nom de "Happy Ending Problem", est un problème fondamental en géométrie discrète et en théorie de Ramsey. Elle affirme que pour tout entier $n \ge 3$, il existe un entier minimal $N(n)$ tel que tout ensemble de $N(n)$ points dans le plan, en position générale (aucun triplet de points n'est aligné), contienne au moins un sous-ensemble de $n$ points formant un polygone convexe.

Paul Erdős et George Szekeres ont initialement prouvé l'existence de $N(n)$ en 1935. La conjecture centrale postule que la borne exacte est :
$$N(n) = 2^{n-2} + 1$$

## État Actuel et Littérature Contextuelle
Les bornes de $N(n)$ font l'objet de recherches intenses. Pour de petites valeurs, il est connu que $N(3)=3$, $N(4)=5$, $N(5)=9$, et $N(6)=17$. La valeur exacte pour $n \ge 7$ reste un problème ouvert, bien que la borne inférieure $N(n) \ge 2^{n-2} + 1$ soit établie.

Le problème partage des connexions profondes avec la théorie de Ramsey et les ensembles partiellement ordonnés. La preuve séminale repose sur le théorème de Dilworth et le théorème de la tasse et de la casquette (Cup-Cap theorem), qui analyse les séquences monotones de pentes. Récemment, Andrew Suk (2017) a réalisé une percée en prouvant que $N(n) \le 2^{n + o(n)}$, rapprochant considérablement la borne supérieure de la borne inférieure conjecturée. Cette approche utilise des outils probabilistes modernes analogues à ceux utilisés pour résoudre les bornes de certains nombres de Ramsey géométriques.

## Définitions Formelles

**Définition 1 (Position Générale)**
Un sous-ensemble de points $S \subset \mathbb{R}^2$ est dit en position générale si et seulement si pour tout triplet de points distincts $(p_i, p_j, p_k) \in S^3$, le déterminant de la matrice de leurs coordonnées affines est non nul :
$$ \det \begin{pmatrix} x_i & x_j & x_k \\ y_i & y_j & y_k \\ 1 & 1 & 1 \end{pmatrix} \neq 0 $$

**Définition 2 (Polygone Convexe)**
Un sous-ensemble ordonné de $n$ points $\{p_1, \dots, p_n\} \subset \mathbb{R}^2$ forme un polygone convexe si tous les points sont situés strictement du même côté de chaque droite passant par deux points consécutifs $p_i$ et $p_{i+1}$ (avec $p_{n+1} = p_1$).

## Approche et Stratégie de Preuve
Dans la documentation jointe (`08-proof.pdf`), nous fournissons une dérivation stricte, sans aucune ellipse, des bornes inférieures. Notre stratégie implique :
1. **Le Théorème de la Tasse et de la Casquette (Cup-Cap) :** Une preuve rigoureuse démontrant que tout ensemble suffisamment grand de points doit contenir soit une "tasse" (une séquence formant une enveloppe convexe par le bas) soit une "casquette" (par le haut).
2. **Borne Inférieure Constructive pour n=5 :** Nous générons algorithmiquement et analysons une configuration de 8 points, en évaluant l'intégralité des 56 sous-ensembles de taille 5 via des produits vectoriels pour prouver l'absence de tout pentagone convexe, établissant ainsi que $N(5) > 8$.
3. **Architecture Lean 4 :** Un squelette de preuve (*Proof Sketch*) est fourni pour traduire ces définitions géométriques dans l'assistant de preuve Lean 4 en vue d'une vérification mécanisée.

Voir `08-proof.pdf` pour la dérivation mathématique rigoureuse complète.
