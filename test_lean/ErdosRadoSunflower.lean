import Mathlib

/-!
# Erdős-Rado Sunflower Lemma & Shadow Theorem (Problem #68) in Lean 4

A *sunflower* (or $\Delta$-system) with $r$ petals and core $Y$ is a collection of sets
$S_1, S_2, \dots, S_r$ such that for all $i \ne j$, $S_i \cap S_j = Y$.
(When $Y = \emptyset$, the sets are pairwise disjoint).

Paul Erdős and Richard Rado (1960) proved the Sunflower Lemma:
Any family $\mathcal{F}$ of sets each of size $k$ with $|\mathcal{F}| > k!(r-1)^k$
contains a sunflower with $r$ petals.

In this file, we formally establish in Lean 4 (with 0 `sorry`):
1. **Base Case $k = 1$:** Any family of singletons with $|\mathcal{F}| \ge r$ forms
   a sunflower with empty core.
2. **Shadow & Extension Definition:** The shadow $\partial \mathcal{F}$ and the
   extension family $\mathcal{F}_E = \{F \in \mathcal{F} \mid E \subset F\}$.
3. **Sunflower Structure of Extensions:** For any $E$ of size $k-1$, the family of
   all $k$-element extensions $\mathcal{F}_E$ forms a sunflower with core $E$.
-/

set_option linter.unusedVariables false

open Finset

/-- A collection of sets F forms a sunflower with core Y if all pairwise intersections equal Y -/
def is_sunflower (F : Finset (Finset ℕ)) (Y : Finset ℕ) : Prop :=
  ∀ A B, A ∈ F → B ∈ F → A ≠ B → A ∩ B = Y

/-- A family of sets is k-uniform if every member has cardinality k -/
def is_uniform (F : Finset (Finset ℕ)) (k : ℕ) : Prop :=
  ∀ A ∈ F, A.card = k

/-- The shadow ∂F of a k-uniform family: all subsets of size k-1 contained in some F ∈ ℱ -/
def shadow (F : Finset (Finset ℕ)) (k : ℕ) : Finset (Finset ℕ) :=
  F.biUnion (fun A => A.powersetCard (k - 1))

/-- The extensions of a subset E in F: all sets in F that contain E -/
def extensions (F : Finset (Finset ℕ)) (E : Finset ℕ) : Finset (Finset ℕ) :=
  F.filter (fun A => E ⊆ A)

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

/--
Theorem (Extension Sunflower Theorem):
For any (k-1)-element set E and any k-uniform family F,
the family of extensions {A ∈ F | E ⊆ A} forms a sunflower with core E.
-/
theorem extensions_form_sunflower (F : Finset (Finset ℕ)) (k : ℕ) (E : Finset ℕ)
    (h_uni : is_uniform F k) (hE : E.card = k - 1) (hk : k ≥ 1) :
    is_sunflower (extensions F E) E := by
  intro A B hA hB h_ne
  simp only [extensions, mem_filter] at hA hB
  obtain ⟨hA_F, hE_A⟩ := hA
  obtain ⟨hB_F, hE_B⟩ := hB
  have hA_card : A.card = k := h_uni A hA_F
  have hB_card : B.card = k := h_uni B hB_F
  have h_sub : E ⊆ A ∩ B := subset_inter hE_A hE_B
  -- Since A ≠ B and |A| = |B| = k, |A ∩ B| < k
  have h_inter_ss : A ∩ B ⊂ A := by
    rw [ssubset_iff_subset_ne]
    refine ⟨inter_subset_left, ?_⟩
    intro h_eq
    have h_sub_BA : A ⊆ B := by
      rw [← h_eq]
      exact inter_subset_right
    have h_card_BA : B.card ≤ A.card := by rw [hA_card, hB_card]
    have h_eq_AB : A = B := eq_of_subset_of_card_le h_sub_BA h_card_BA
    exact h_ne h_eq_AB
  have h_inter_lt : (A ∩ B).card < k := by
    have h_card_lt := card_lt_card h_inter_ss
    omega
  have h_inter_le : (A ∩ B).card ≤ k - 1 := by omega
  have h_card_inter_le_E : (A ∩ B).card ≤ E.card := by omega
  have h_E_eq_inter : E = A ∩ B := eq_of_subset_of_card_le h_sub h_card_inter_le_E
  exact h_E_eq_inter.symm
