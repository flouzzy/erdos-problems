import Mathlib

/-!
# Erdős-Rado Sunflower Lemma (Problem #68) in Lean 4

A *sunflower* (or $\Delta$-system) with $r$ petals and core $Y$ is a collection of sets
$S_1, S_2, \dots, S_r$ such that for all $i \ne j$, $S_i \cap S_j = Y$.
(When $Y = \emptyset$, the sets are pairwise disjoint).

Paul Erdős and Richard Rado (1960) proved the Sunflower Lemma:
Any family $\mathcal{F}$ of sets each of size $k$ with $|\mathcal{F}| > k!(r-1)^k$
contains a sunflower with $r$ petals.

In this file, we formally prove in Lean 4 (with 0 `sorry`):
1. The base case $k = 1$: Any family of singletons with $|\mathcal{F}| \ge r$ forms
   a sunflower with empty core (pairwise disjoint).
2. The threshold cardinality bounds for $k = 1$.
-/

set_option linter.unusedVariables false

open Finset

/-- A collection of sets F forms a sunflower with core Y if all pairwise intersections equal Y -/
def is_sunflower (F : Finset (Finset ℕ)) (Y : Finset ℕ) : Prop :=
  ∀ A B, A ∈ F → B ∈ F → A ≠ B → A ∩ B = Y

/-- A family of sets is k-uniform if every member has cardinality k -/
def is_uniform (F : Finset (Finset ℕ)) (k : ℕ) : Prop :=
  ∀ A ∈ F, A.card = k

/--
Base Case k = 1 of the Erdős-Rado Sunflower Lemma:
Any family F of 1-element sets (singletons) forms a sunflower
with empty core (pairwise disjoint).
-/
theorem sunflower_base_k_one (F : Finset (Finset ℕ))
    (h_uni : is_uniform F 1) :
    is_sunflower F ∅ := by
  intro A B hA hB h_ne
  have hA_card : A.card = 1 := h_uni A hA
  have hB_card : B.card = 1 := h_uni B hB
  obtain ⟨a, rfl⟩ := card_eq_one.mp hA_card
  obtain ⟨b, rfl⟩ := card_eq_one.mp hB_card
  have hab_ne : a ≠ b := by
    intro h_eq
    subst h_eq
    exact h_ne rfl
  ext x
  simp only [mem_inter, mem_singleton]
  constructor
  · rintro ⟨rfl, rfl⟩
    exact (hab_ne rfl).elim
  · intro h_emp
    exact (Finset.notMem_empty x h_emp).elim

/--
Erdős-Rado Bound Threshold for k = 1:
k! * (r - 1)^k = 1! * (r - 1)^1 = r - 1.
If |F| > r - 1, then |F| ≥ r and F is a sunflower.
-/
theorem erdos_rado_threshold_k1 (F : Finset (Finset ℕ)) (r : ℕ) (hr : r ≥ 1)
    (h_card : F.card > r - 1) (h_uni : is_uniform F 1) :
    F.card ≥ r ∧ is_sunflower F ∅ := by
  have h_ge : F.card ≥ r := by omega
  refine ⟨h_ge, sunflower_base_k_one F h_uni⟩
