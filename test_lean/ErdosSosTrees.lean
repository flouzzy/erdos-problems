import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Sós Tree Conjecture in Lean 4

The Erdős-Sós Conjecture (Problem #09 in Paul Erdős' collection, 1963) asserts that
every simple graph $G = (V, E)$ with average degree strictly exceeding $k - 1$:
  $$\bar{d}(G) = \frac{2 |E|}{|V|} > k - 1 \iff |E| > \frac{k - 1}{2} |V|$$
contains every tree $T$ on $k$ edges ($k + 1$ vertices) as a subgraph ($T \subseteq G$).

Key Mathematical Milestones:
- Tightness: Disjoint unions of cliques $K_k$ have average degree $k - 1$ and cannot contain any tree on $k + 1$ vertices.
- For stars $T = S_k = K_{1, k}$, the conjecture holds trivially because $\Delta(G) \ge \bar{d}(G) > k - 1 \implies \Delta(G) \ge k$.
- For paths $T = P_{k+1}$, the conjecture was established by Erdős and Gallai (1959).
- For large graphs ($|V| \ge N_0(k)$), the conjecture was established by Ajtai, Komlós, Simonovits, and Szemerédi via the Regularity Lemma.

In this file, we formally certify:
1. The average degree inequality and edge count predicate.
2. The Handshaking Lemma relation: $\sum_{v \in V} \deg(v) = 2 |E|$.
3. Formal proof that $\bar{d}(G) > k - 1$ implies the existence of a vertex of degree at least $k$: $\exists v \in V, \deg(v) \ge k$.
4. Formal certification of the Erdős-Sós conjecture for all star trees $S_k = K_{1, k}$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset SimpleGraph

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- The total number of edges in a simple graph $G$ -/
noncomputable def num_edges (G : SimpleGraph V) : ℕ :=
  G.edgeFinset.card

/-- The average degree of $G$ multiplied by $|V|$ (i.e. $2 |E|$) -/
noncomputable def sum_degrees (G : SimpleGraph V) : ℕ :=
  ∑ v : V, G.degree v

/-- Handshaking Lemma: $\sum_{v \in V} \deg(v) = 2 |E|$ -/
theorem handshaking_identity (G : SimpleGraph V) :
    sum_degrees G = 2 * num_edges G := by
  unfold sum_degrees num_edges
  exact G.sum_degrees_eq_twice_card_edges

/-- If $2 |E| > (k - 1) |V|$, then there exists a vertex with degree $\ge k$ -/
theorem exists_vertex_degree_ge (G : SimpleGraph V) (k : ℕ) [Nonempty V]
    (h_dense : 2 * num_edges G > (k - 1) * Fintype.card V) :
    ∃ v : V, G.degree v ≥ k := by
  by_contra h_contra
  push_neg at h_contra
  have h_sum_lt : sum_degrees G ≤ (k - 1) * Fintype.card V := by
    unfold sum_degrees
    have h_each : ∀ v : V, G.degree v ≤ k - 1 := by
      intro v
      have hv := h_contra v
      omega
    have h_le := Finset.sum_le_card_nsmul (Finset.univ : Finset V) (k - 1) (fun v _ => h_each v)
    rw [card_univ] at h_le
    exact h_le
  rw [handshaking_identity] at h_sum_lt
  omega

/-- For star trees $S_k = K_{1, k}$, a graph with $2|E| > (k-1)|V|$ contains a vertex of degree $\ge k$, embedding $S_k$ -/
theorem erdos_sos_star_tree (G : SimpleGraph V) (k : ℕ) [Nonempty V]
    (h_dense : 2 * num_edges G > (k - 1) * Fintype.card V) :
    ∃ (center : V) (leaves : Finset V), leaves.card = k ∧ (∀ u ∈ leaves, G.Adj center u) := by
  obtain ⟨v, hv⟩ := exists_vertex_degree_ge G k h_dense
  have h_card_ge : (G.neighborFinset v).card ≥ k := hv
  obtain ⟨leaves, h_sub, h_card⟩ := Finset.exists_smaller_set (G.neighborFinset v) k h_card_ge
  use v, leaves
  refine ⟨h_card, ?_⟩
  intro u hu
  have hu_neigh : u ∈ G.neighborFinset v := h_sub hu
  simp only [mem_neighborFinset] at hu_neigh
  exact hu_neigh
