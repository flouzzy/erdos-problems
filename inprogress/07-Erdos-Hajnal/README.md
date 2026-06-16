[🇫🇷 Version Française](README.fr.md) | [🇬🇧 English Version](README.md)

# Problem 07: Erdős-Hajnal Conjecture

**Status:** In Progress (Partial Resolution)
**Field:** Graph Theory (Induced Graphs and Ramsey Theory)

The Erdős-Hajnal conjecture postulates that for every finite graph $H$, there exists a constant $c(H) > 0$ such that every graph $G$ on $n$ vertices that does not contain $H$ as an induced subgraph has either a clique of size $n^{c(H)}$ or an independent set of size $n^{c(H)}$.

This conjecture, formulated in 1989, strongly contrasts with the behavior of random graphs where the maximum size of a clique or an independent set is logarithmic (of order $O(\log n)$). Forbidding an induced subgraph $H$ forces the graph $G$ to be drastically structurally constrained globally.

This directory provides a structural analysis, a decomposition into intermediate lemmas, and an initial formalization architecture of the proof.

---

## 1. Axiomatic Definitions

To guarantee absolute formal rigor, we redefine the central concepts.

**Definition 1.1 (Graph)**
Let $G = (V, E)$ be a graph, where $V$ is a finite set of vertices and $E \subseteq [V]^2$ is the set of edges.

**Definition 1.2 (Induced Subgraph)**
Let $H = (V_H, E_H)$ be a graph. The graph $G$ contains $H$ as an induced subgraph if there exists an injective function $f : V_H \to V$ such that for all $(u, v) \in [V_H]^2$, $(u, v) \in E_H \iff (f(u), f(v)) \in E$.
If $G$ does not contain $H$ as an induced subgraph, $G$ is said to be *$H$-free*.

**Definition 1.3 (Clique and Independent Set)**
Let $S \subseteq V$.
$S$ is a clique of $G$ if $[S]^2 \subseteq E$.
$S$ is an independent set of $G$ if $[S]^2 \cap E = \emptyset$.
We denote by $\omega(G)$ the size of the largest clique in $G$, and by $\alpha(G)$ the size of the largest independent set.

**Erdős-Hajnal Conjecture (Formal):**
$$\forall H, \exists c(H) > 0, \forall G \text{ graph } H\text{-free}, \max(\omega(G), \alpha(G)) \ge |V(G)|^{c(H)}$$

---

## 2. Contextual Literature

The most closely related works include the strong perfect graph theorem by Chudnovsky, Robertson, Seymour, and Thomas (2006). For perfect graphs, $\omega(G) \alpha(G) \ge |V(G)|$, which trivially satisfies the conjecture with $c(H) = 0.5$.
A strong analogy exists with quantitative Ramsey theory, where one seeks the minimal order of a graph ensuring the existence of monochromatic structures. The recent proof of the Erdős-Hajnal conjecture for graphs not containing $P_5$ (the path on 5 vertices) illustrates the use of graph substitution, a fundamental method exploited below.

---

## 3. Proof Strategy and Lemmas

We decompose the proof into three structural lemmas.

### 3.1 Reduction Lemma to Prime Graphs
**Statement:** If the conjecture is true for all prime graphs (indecomposable by substitution), then it is true for any graph $H$.
**Strategy:** By strict structural induction. If $H$ is obtained by substituting $H_2$ into a vertex of $H_1$, and $c(H_1), c(H_2)$ exist, we construct a multiplicative lower bound for $c(H)$.

### 3.2 Substitution Bounding Lemma
**Statement:** Let $G$ be a graph defined by the substitution of a family of graphs $(G_v)_{v \in V_F}$ into a frame graph $F$. Then, $\alpha(G) \ge \alpha(F) \cdot \min_{v} \alpha(G_v)$.
**Strategy:** By double inclusion and explicit combinatorial calculation of the cardinalities of independent sets within the lexicographic product.

### 3.3 Partial Clique Extraction Lemma
**Statement:** For any prime graph $H$, there exists an edge density threshold $\delta(H)$ such that if $G$ is $H$-free and has density strictly greater than $\delta(H)$, a clique of order $n^{\epsilon}$ can be extracted.
**Strategy:** Utilizing the modified Erdős probabilistic method to bound the expected size of the largest independent set in the complement graph.

---

## 4. Informal Proofs

### Proof of Lemma 3.2 (Substitution Bounding Lemma)

1. Let $F = (V_F, E_F)$ be a graph and $\mathcal{G} = \{G_v = (V_v, E_v) \mid v \in V_F\}$ be a family of disjoint graphs.
2. The substituted graph $G = F[\mathcal{G}]$ has vertex set $V = \bigcup_{v \in V_F} V_v$.
3. The edges of $G$ are defined as follows: a pair $\{x, y\}$ with $x \in V_u, y \in V_v$ is an edge of $G$ if and only if either $u = v$ and $\{x, y\} \in E_u$, or $u \neq v$ and $\{u, v\} \in E_F$.
4. Let $S_F \subseteq V_F$ be the maximal independent set of $F$. By definition, $\alpha(F) = |S_F|$ and for any pair $(u, v) \in S_F \times S_F$ with $u \neq v$, the edge $\{u, v\} \notin E_F$.
5. For each vertex $v \in S_F$, let $S_v \subseteq V_v$ be the maximal independent set of $G_v$. The size of this independent set is $|S_v| = \alpha(G_v)$.
6. We construct the set $S = \bigcup_{v \in S_F} S_v$. We will demonstrate that $S$ is an independent set of $G$.
7. Let $x, y \in S$ be two distinct elements. Let $x \in S_u$ and $y \in S_v$ with $u, v \in S_F$.
8. First case: $u = v$. Then $x, y$ belong to the same independent set $S_u$ of $G_u$. Since $S_u$ is independent in $G_u$, the edge $\{x, y\} \notin E_u$. By the definition of substitution (step 3), $\{x, y\}$ is not an edge of $G$.
9. Second case: $u \neq v$. Since $x \in S_u$ and $y \in S_v$, and $u, v$ belong to the independent set $S_F$, the edge $\{u, v\} \notin E_F$. By the definition of substitution (step 3), $\{x, y\}$ is not an edge of $G$.
10. In all explicit cases, $\{x, y\}$ is not an edge. Thus, $S$ is strictly an independent set of $G$.
11. Let us evaluate the cardinality of $S$. Since the graphs $G_v$ are disjoint, the sets $S_v$ are disjoint. Therefore $|S| = \sum_{v \in S_F} |S_v|$.
12. By successive lower bounding of each term in the sum by the global minimum: for all $v \in S_F, |S_v| \ge \min_{k \in V_F} \alpha(G_k)$.
13. Summing over $|S_F|$ identical terms yields: $|S| \ge |S_F| \times \min_{k \in V_F} \alpha(G_k)$.
14. By the definition of the global optimum $\alpha(G)$, we know that $\alpha(G) \ge |S|$.
15. By substituting $|S_F|$ with $\alpha(F)$, we obtain the final strict bound: $\alpha(G) \ge \alpha(F) \cdot \min_{v \in V_F} \alpha(G_v)$. $\blacksquare$

---

## 5. Autoformalization Architecture (Lean 4)

Here is the *Proof Sketch* translatable into the strict formalism of Lean 4, using exclusively ASCII characters. Note that this code block contains an incomplete proof sketch intended for future autoformalization.

```lean
import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Clique

/-!
# Formal Architecture - Erdos-Hajnal Conjecture
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