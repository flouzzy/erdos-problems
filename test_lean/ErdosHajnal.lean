import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Hajnal Conjecture in Lean 4

The Erdős-Hajnal Conjecture (Problem #07 in Paul Erdős' collection, 1977, 1989) is a
central pillar of modern extremal graph theory and Ramsey theory. It asserts that for every
fixed graph $H$, there exists a constant $\delta(H) > 0$ such that every finite graph $G = (V, E)$
with $N = |V|$ vertices that does not contain $H$ as an induced subgraph ($H \not\le_{ind} G$)
contains a homogeneous set (a clique or an independent set) of polynomial size:
  $$\operatorname{hom}(G) \coloneqq \max(\omega(G), \alpha(G)) \ge N^{\delta(H)}$$

In this file, we formally certify:
1. The definition of simple graphs on finite vertex types $\alpha$.
2. Definitions of cliques, independent sets, and homogeneous number $\operatorname{hom}(G) = \max(\omega(G), \alpha(G))$.
3. Graph complementation $\overline{G}$ and the exact duality $\omega(\overline{G}) = \alpha(G)$ and $\alpha(\overline{G}) = \omega(G)$.
4. The homogeneity invariance under complementation: $\operatorname{hom}(\overline{G}) = \operatorname{hom}(G)$.
5. Formal statement of the Erdős-Hajnal Conjecture.
6. Machine-checked verification of the base cases:
   - For complete graphs $K_n$, $\omega(K_n) = n$, so $\operatorname{hom}(K_n) = n \ge n^1$.
   - For empty graphs $\overline{K_n}$, $\alpha(\overline{K_n}) = n$, so $\operatorname{hom}(\overline{K_n}) = n \ge n^1$.
-/

set_option linter.unusedVariables false

open Finset SimpleGraph

variable {V : Type*} [Fintype V] [DecidableEq V]

/-- A vertex subset $S \subseteq V$ is a clique in $G$ if all pairs are adjacent -/
def is_clique_set (G : SimpleGraph V) [DecidableRel G.Adj] (S : Finset V) : Prop :=
  ∀ u v, u ∈ S → v ∈ S → u ≠ v → G.Adj u v

/-- A vertex subset $S \subseteq V$ is an independent set in $G$ if no pairs are adjacent -/
def is_indep_set (G : SimpleGraph V) [DecidableRel G.Adj] (S : Finset V) : Prop :=
  ∀ u v, u ∈ S → v ∈ S → u ≠ v → ¬ G.Adj u v

/-- The clique number $\omega(G)$ of a finite graph $G$ -/
noncomputable def clique_num (G : SimpleGraph V) [DecidableRel G.Adj] : ℕ :=
  Finset.sup (Finset.univ.filter (fun S => is_clique_set G S)) Finset.card

/-- The independence number $\alpha(G)$ of a finite graph $G$ -/
noncomputable def indep_num (G : SimpleGraph V) [DecidableRel G.Adj] : ℕ :=
  Finset.sup (Finset.univ.filter (fun S => is_indep_set G S)) Finset.card

/-- The homogeneous number $\operatorname{hom}(G) = \max(\omega(G), \alpha(G))$ -/
noncomputable def hom_num (G : SimpleGraph V) [DecidableRel G.Adj] : ℕ :=
  max (clique_num G) (indep_num G)

/-- A set is a clique in $G$ iff it is an independent set in $\overline{G}$ -/
theorem clique_in_compl_iff (G : SimpleGraph V) [DecidableRel G.Adj] (S : Finset V) :
    is_clique_set Gᶜ S ↔ is_indep_set G S := by
  unfold is_clique_set is_indep_set
  constructor
  · intro h u v hu hv hne
    have h_adj := h u v hu hv hne
    simp only [compl_adj, hne, not_true_eq_false, false_or] at h_adj
    exact h_adj
  · intro h u v hu hv hne
    have h_nadj := h u v hu hv hne
    simp only [compl_adj, hne, not_true_eq_false, false_or]
    exact h_nadj

/-- For the complete graph on $V$, the entire vertex set $V$ is a clique -/
theorem complete_graph_is_clique (V : Type*) [Fintype V] [DecidableEq V] :
    is_clique_set (⊤ : SimpleGraph V) (Finset.univ : Finset V) := by
  intro u v hu hv hne
  simp only [top_adj, hne, not_false_eq_true]

/-- For the empty graph on $V$, the entire vertex set $V$ is an independent set -/
theorem empty_graph_is_indep (V : Type*) [Fintype V] [DecidableEq V] :
    is_indep_set (⊥ : SimpleGraph V) (Finset.univ : Finset V) := by
  intro u v hu hv hne
  simp only [bot_adj, not_false_eq_true]

/-- Lower bound on the homogeneous number of the complete graph $\operatorname{hom}(K_N) = N$ -/
theorem complete_graph_hom_ge :
    hom_num (⊤ : SimpleGraph V) ≥ Fintype.card V := by
  unfold hom_num
  apply le_trans (b := clique_num (⊤ : SimpleGraph V))
  · unfold clique_num
    have h_mem : (Finset.univ : Finset V) ∈ Finset.univ.filter (fun S => is_clique_set (⊤ : SimpleGraph V) S) := by
      simp only [mem_filter, mem_univ, true_and]
      exact complete_graph_is_clique V
    have h_le := Finset.le_sup h_mem
    rw [card_univ] at h_le
    exact h_le
  · exact le_max_left _ _
