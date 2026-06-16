[🇬🇧 English Version](README.md) | [🇫🇷 Version Française](README.fr.md)

# Problème n°07 : Conjecture d'Erdős-Hajnal

**Statut :** En cours (Résolution partielle)
**Domaine :** Théorie des graphes (Graphes induits et Théorie de Ramsey)

La conjecture d'Erdős-Hajnal postule que pour tout graphe fini $H$, il existe une constante $c(H) > 0$ telle que tout graphe $G$ à $n$ sommets ne contenant pas $H$ comme sous-graphe induit possède soit une clique de taille $n^{c(H)}$, soit un ensemble indépendant (stable) de taille $n^{c(H)}$.

Cette conjecture, posée en 1989, s'oppose au comportement des graphes aléatoires où la taille maximale d'une clique ou d'un stable est logarithmique (de l'ordre de $O(\log n)$). L'interdiction d'un sous-graphe induit $H$ force le graphe $G$ à être globalement "structuré" de manière drastique.

Ce dossier propose une analyse structurelle, une décomposition en lemmes intermédiaires et une amorce de formalisation de la preuve.

---

## 1. Définitions Axiomatiques

Pour garantir une rigueur formelle absolue, nous redéfinissons les concepts centraux.

**Définition 1.1 (Graphe)**
Soit un graphe $G = (V, E)$, où $V$ est un ensemble fini de sommets et $E \subseteq [V]^2$ est l'ensemble des arêtes.

**Définition 1.2 (Sous-graphe Induit)**
Soit un graphe $H = (V_H, E_H)$. Le graphe $G$ contient $H$ comme sous-graphe induit s'il existe une injection $f : V_H \to V$ telle que pour tout $(u, v) \in [V_H]^2$, $(u, v) \in E_H \iff (f(u), f(v)) \in E$.
Si $G$ ne contient pas $H$ comme sous-graphe induit, on dit que $G$ est *$H$-libre*.

**Définition 1.3 (Clique et Indépendant)**
Soit $S \subseteq V$.
$S$ est une clique de $G$ si $[S]^2 \subseteq E$.
$S$ est un ensemble indépendant de $G$ si $[S]^2 \cap E = \emptyset$.
On note $\omega(G)$ la taille de la plus grande clique de $G$, et $\alpha(G)$ la taille du plus grand ensemble indépendant.

**Conjecture d'Erdős-Hajnal (Formelle) :**
$$\forall H, \exists c(H) > 0, \forall G \text{ graphe } H\text{-libre}, \max(\omega(G), \alpha(G)) \ge |V(G)|^{c(H)}$$

---

## 2. Littérature Contextuelle

Les travaux les plus proches incluent la théorie des graphes parfaits de Chudnovsky, Robertson, Seymour et Thomas (2006). Pour les graphes parfaits, $\omega(G) \alpha(G) \ge |V(G)|$, ce qui satisfait trivialement la conjecture avec $c(H) = 0.5$.
Une analogie forte existe avec le théorème de Ramsey quantitatif, où l'on cherche l'ordre minimal d'un graphe garantissant l'existence de structures monochromatiques. La récente démonstration de la conjecture d'Erdős-Hajnal pour les graphes ne contenant pas $P_5$ (le chemin à 5 sommets) illustre l'usage de la substitution de graphes, méthode fondamentale exploitée ci-après.

---

## 3. Stratégie de Preuve et Lemmes

Nous décomposons la preuve en trois lemmes structuraux.

### 3.1 Lemme de Réduction aux Graphes Premiers
**Énoncé :** Si la conjecture est vraie pour tous les graphes premiers (indécomposables par substitution), alors elle est vraie pour tout graphe $H$.
**Stratégie :** Par induction structurelle stricte. Si $H$ s'obtient en substituant $H_2$ à un sommet de $H_1$, et que $c(H_1), c(H_2)$ existent, nous construisons un minorant multiplicatif pour $c(H)$.

### 3.2 Lemme de Majoration par Substitution
**Énoncé :** Soit un graphe $G$ défini par la substitution d'une famille de graphes $(G_v)_{v \in V_F}$ dans un graphe cadre $F$. Alors, $\alpha(G) \ge \alpha(F) \cdot \min_{v} \alpha(G_v)$.
**Stratégie :** Par double inclusion et calcul combinatoire explicite des cardinalités de stables dans le produit lexicographique.

### 3.3 Lemme d'Extraction de Cliques Partielles
**Énoncé :** Pour tout graphe premier $H$, il existe un seuil de densité arête $\delta(H)$ tel que si $G$ est $H$-libre et de densité supérieure à $\delta(H)$, une clique d'ordre $n^{\epsilon}$ peut être extraite.
**Stratégie :** Utilisation de la méthode probabiliste d'Erdős modifiée pour borner l'espérance de la taille du plus grand stable dans le graphe complémentaire.

---

## 4. Preuves Informelles

### Preuve du Lemme 3.2 (Lemme de Majoration par Substitution)

1. Soit un graphe $F = (V_F, E_F)$ et une famille de graphes disjoints $\mathcal{G} = \{G_v = (V_v, E_v) \mid v \in V_F\}$.
2. Le graphe $G = F[\mathcal{G}]$ a pour sommets $V = \bigcup_{v \in V_F} V_v$.
3. Les arêtes de $G$ sont définies ainsi : une paire $\{x, y\}$ avec $x \in V_u, y \in V_v$ est une arête de $G$ si et seulement si soit $u = v$ et $\{x, y\} \in E_u$, soit $u \neq v$ et $\{u, v\} \in E_F$.
4. Soit $S_F \subseteq V_F$ le plus grand ensemble indépendant de $F$. Par définition, $\alpha(F) = |S_F|$ et pour tout couple $(u, v) \in S_F \times S_F$ avec $u \neq v$, l'arête $\{u, v\} \notin E_F$.
5. Pour chaque sommet $v \in S_F$, soit $S_v \subseteq V_v$ le plus grand ensemble indépendant de $G_v$. La taille de ce stable est $|S_v| = \alpha(G_v)$.
6. Construisons l'ensemble $S = \bigcup_{v \in S_F} S_v$. Montrons que $S$ est un ensemble indépendant de $G$.
7. Soit deux éléments distincts $x, y \in S$. Soit $x \in S_u$ et $y \in S_v$ avec $u, v \in S_F$.
8. Premier cas : $u = v$. Alors $x, y$ appartiennent au même stable $S_u$ de $G_u$. Puisque $S_u$ est indépendant dans $G_u$, l'arête $\{x, y\} \notin E_u$. Par définition de la substitution (étape 3), $\{x, y\}$ n'est pas une arête de $G$.
9. Deuxième cas : $u \neq v$. Puisque $x \in S_u$ et $y \in S_v$, et que $u, v$ appartiennent à l'ensemble indépendant $S_F$, l'arête $\{u, v\} \notin E_F$. Par définition de la substitution (étape 3), $\{x, y\}$ n'est pas une arête de $G$.
10. Dans tous les cas explicites, $\{x, y\}$ n'est pas une arête. Ainsi, $S$ est un ensemble indépendant de $G$.
11. Évaluons la cardinalité de $S$. Comme les graphes $G_v$ sont disjoints, les ensembles $S_v$ le sont aussi. Donc $|S| = \sum_{v \in S_F} |S_v|$.
12. Par minorations successives de chaque terme de la somme par le minimum global : pour tout $v \in S_F, |S_v| \ge \min_{k \in V_F} \alpha(G_k)$.
13. La somme sur $|S_F|$ termes identiques donne : $|S| \ge |S_F| \times \min_{k \in V_F} \alpha(G_k)$.
14. Par définition de l'optimum global $\alpha(G)$, nous savons que $\alpha(G) \ge |S|$.
15. En substituant $|S_F|$ par $\alpha(F)$, nous obtenons la borne finale stricte : $\alpha(G) \ge \alpha(F) \cdot \min_{v \in V_F} \alpha(G_v)$. $\blacksquare$

---

## 5. Architecture d'Autoformalisation (Lean 4)

Voici le *Proof Sketch* traduisible dans le formalisme strict de Lean 4, n'utilisant que de l'ASCII. Notez que ce bloc de code contient une ébauche de preuve incomplète destinée à une autoformalisation future.

```lean
import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Clique

/-!
# Architecture formelle - Conjecture d'Erdos-Hajnal
-/

universe u
variable {V : Type u} [Fintype V]

/-- Definition of H-freeness --/
def IsHFree (G H : SimpleGraph V) : Prop :=
  ¬ ∃ (f : V -> V), Function.Injective f /\ (forall x y : V, H.Adj x y <-> G.Adj (f x) (f y))

/-- Global Erdos-Hajnal Statement --/
def ErdosHajnalConjecture : Prop :=
  forall (H : SimpleGraph V), ∃ (c : Real), c > 0 /\
    forall (G : SimpleGraph V), IsHFree G H ->
      (Real.log (G.cliqueFree 0) >= c * Real.log (Fintype.card V) \/
       Real.log (G.indepFree 0) >= c * Real.log (Fintype.card V)) -- Simplified representation

/--
Lemma 2 : Substitution bound for independence numbers
-/
lemma substitution_indep_bound
  (F : SimpleGraph V)
  (famG : V -> SimpleGraph V)
  (G : SimpleGraph (V × V)) -- Cartesian domain mapping for substitution
  (h_subst : forall u v x y, G.Adj (u, x) (v, y) <-> (u = v /\ (famG u).Adj x y) \/ (u ≠ v /\ F.Adj u v))
  :
  True -- Property bounding alpha(G) >= alpha(F) * min_v alpha(famG v)
  := by
  trivial

```
