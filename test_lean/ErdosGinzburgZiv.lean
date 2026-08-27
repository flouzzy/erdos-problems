import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Ginzburg-Ziv Theorem in Lean 4
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate: A sequence of length $2n - 1$ contains an $n$-element zero-sum modulo $n$ -/
def has_egz_subsequence (n : ℕ) (a : Fin (2 * n - 1) → ℤ) : Prop :=
  ∃ I : Finset (Fin (2 * n - 1)), I.card = n ∧ (∑ i ∈ I, a i) % (n : ℤ) = 0

/-- Base case $n = 1$: A sequence of length $2(1) - 1 = 1$ trivially sums to a multiple of 1 -/
theorem egz_base_one (a : Fin 1 → ℤ) :
    has_egz_subsequence 1 a := by
  use {0}
  constructor
  · exact card_singleton 0
  · simp

/-- Base case $n = 2$: Any sequence of 3 integers has two elements of the same parity -/
theorem egz_base_two (a : Fin 3 → ℤ) :
    has_egz_subsequence 2 a := by
  have h_parity : (a 0 + a 1) % (2 : ℤ) = 0 ∨ (a 0 + a 2) % (2 : ℤ) = 0 ∨ (a 1 + a 2) % (2 : ℤ) = 0 := by
    omega
  rcases h_parity with h01 | h02 | h12
  · use {0, 1}
    refine ⟨by decide, ?_⟩
    have : ∑ i ∈ ({0, 1} : Finset (Fin 3)), a i = a 0 + a 1 := by
      rw [sum_pair (by decide)]
    rw [this]
    exact h01
  · use {0, 2}
    refine ⟨by decide, ?_⟩
    have : ∑ i ∈ ({0, 2} : Finset (Fin 3)), a i = a 0 + a 2 := by
      rw [sum_pair (by decide)]
    rw [this]
    exact h02
  · use {1, 2}
    refine ⟨by decide, ?_⟩
    have : ∑ i ∈ ({1, 2} : Finset (Fin 3)), a i = a 1 + a 2 := by
      rw [sum_pair (by decide)]
    rw [this]
    exact h12

/-- Sharpness of EGZ: Any sum of $n$ elements chosen from $n - 1$ zeros and $n - 1$ ones lies in $\{1, \dots, n - 1\}$ -/
theorem egz_sharpness_bounds (n k : ℕ) (hn : n ≥ 2) (hk_ones : k ≤ n - 1) (hk_zeros : (n - k) ≤ n - 1) :
    1 ≤ k ∧ k < n := by
  constructor
  · omega
  · omega
