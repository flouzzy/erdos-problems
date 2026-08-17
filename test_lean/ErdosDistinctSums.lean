import Mathlib

/-!
# Erdős Distinct Subset Sums Problem (Problem #14) in Lean 4

Let $S \subset \mathbb{N}_{>0}$ be a finite set of $n$ positive integers.
We say that $S$ has *distinct subset sums* if for any two distinct subsets
$A, B \subseteq S$, $\sum_{x \in A} x \neq \sum_{x \in B} x$.

Paul Erdős (1931, 1955) conjectured that $\max(S) \ge c \cdot 2^n$ for some constant $c > 0$.
The powers of two $\{1, 2, 4, \dots, 2^{n-1}\}$ satisfy $\max(S) = 2^{n-1}$.

In this file, we formally prove (with 0 `sorry`):
1. If $S$ has distinct subset sums and $|S| = n$, then $\sum_{x \in S} x \ge 2^n - 1$.
2. For any positive integer $M$ bounding all elements of $S$ ($\forall x \in S, x \le M$),
   we have $n \cdot M \ge 2^n - 1$, which implies $M \ge (2^n - 1) / n$.
-/

set_option linter.unusedVariables false

open Finset

/-- A finite set S of natural numbers has distinct subset sums -/
def has_distinct_subset_sums (S : Finset ℕ) : Prop :=
  ∀ A B : Finset ℕ, A ⊆ S → B ⊆ S → A.sum id = B.sum id → A = B

/--
Theorem (Information-Theoretic Sum Bound):
If a set S of natural numbers has distinct subset sums,
then the total sum of elements in S is at least 2^(|S|) - 1.
-/
theorem distinct_subset_sums_total_bound (S : Finset ℕ) (h_dist : has_distinct_subset_sums S) :
    S.sum id + 1 ≥ 2^(S.card) := by
  have h_pow_card : (powerset S).card = 2^(S.card) := card_powerset S
  have h_inj : Set.InjOn (fun A : Finset ℕ => A.sum id) (powerset S : Set (Finset ℕ)) := by
    intro A hA B hB heq
    rw [Finset.mem_coe, Finset.mem_powerset] at hA hB
    exact h_dist A B hA hB heq
  have h_img_sub : (powerset S).image (fun A => A.sum id) ⊆ range (S.sum id + 1) := by
    intro s hs
    rw [mem_image] at hs
    obtain ⟨A, hA, rfl⟩ := hs
    rw [mem_powerset] at hA
    rw [mem_range]
    have h_le : A.sum id ≤ S.sum id := Finset.sum_le_sum_of_subset hA
    omega
  have h_card_img : ((powerset S).image (fun A => A.sum id)).card = 2^(S.card) := by
    rw [card_image_of_injOn h_inj, h_pow_card]
  have h_le_range : ((powerset S).image (fun A => A.sum id)).card ≤ (range (S.sum id + 1)).card :=
    card_le_card h_img_sub
  rw [card_range, h_card_img] at h_le_range
  exact h_le_range

/--
Corollary (Erdős Lower Bound on Maximum Element):
If S has distinct subset sums and every element is bounded by M,
then n * M ≥ 2^n - 1.
-/
theorem erdos_distinct_sums_max_bound (S : Finset ℕ) (M : ℕ)
    (h_dist : has_distinct_subset_sums S)
    (h_bound : ∀ x ∈ S, x ≤ M) :
    S.card * M + 1 ≥ 2^(S.card) := by
  have h_sum_le : S.sum id ≤ S.card * M := by
    have h1 : S.sum id ≤ S.sum (fun _ => M) := sum_le_sum h_bound
    rw [sum_const, nsmul_eq_mul] at h1
    exact h1
  have h_total := distinct_subset_sums_total_bound S h_dist
  omega
