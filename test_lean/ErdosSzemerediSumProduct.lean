import Mathlib

/-!
# Erdős-Szemerédi Sum-Product Phenomenon (Problem #35) in Lean 4

Let $A \subset \mathbb{N}$ be a finite non-empty set of $n$ natural numbers.
We define the sumset $A + A = \{a + b \mid a, b \in A\}$.

Paul Erdős and Endre Szemerédi (1983) conjectured that for every $\epsilon > 0$,
  $$ \max(|A + A|, |A \cdot A|) \ge c_\epsilon |A|^{2 - \epsilon} $$

In this file, we formally establish the fundamental sumset lower bounds:
1. $|A + A| \ge 1$ for any singleton set $A = \{a\}$ ($|A+A| = 2|A| - 1$).
2. $|A + A| \ge 3$ for any doubleton set $A = \{a, b\}$ with $a \ne b$ ($|A+A| \ge 2|A| - 1$).
-/

set_option linter.unusedVariables false

open Finset

/-- The sumset A + B of two finite sets of natural numbers -/
def sumset (A B : Finset ℕ) : Finset ℕ :=
  (A ×ˢ B).image (fun p => p.1 + p.2)

/-- Theorem: For any singleton {a}, |{a} + {a}| = 1 = 2(1) - 1 -/
theorem sumset_singleton (a : ℕ) : (sumset {a} {a}).card = 2 * ({a} : Finset ℕ).card - 1 := by
  have h_ss : sumset {a} {a} = {a + a} := by
    ext x
    simp [sumset]
  rw [h_ss, card_singleton, card_singleton]

/-- Theorem: For any pair {a, b} with a < b, |{a, b} + {a, b}| ≥ 3 = 2(2) - 1 -/
theorem sumset_pair (a b : ℕ) (hab : a < b) : (sumset {a, b} {a, b}).card ≥ 2 * ({a, b} : Finset ℕ).card - 1 := by
  have h_ne : a ≠ b := by omega
  have h_card_ab : ({a, b} : Finset ℕ).card = 2 := card_pair h_ne
  have h_in1 : a + a ∈ sumset {a, b} {a, b} := by
    unfold sumset; rw [mem_image]; use (a, a); simp
  have h_in2 : a + b ∈ sumset {a, b} {a, b} := by
    unfold sumset; rw [mem_image]; use (a, b); simp
  have h_in3 : b + b ∈ sumset {a, b} {a, b} := by
    unfold sumset; rw [mem_image]; use (b, b); simp
  have h_sub : {a + a, a + b, b + b} ⊆ sumset {a, b} {a, b} := by
    intro x hx
    simp only [mem_insert, mem_singleton] at hx
    rcases hx with rfl | rfl | rfl
    · exact h_in1
    · exact h_in2
    · exact h_in3
  have h_card_three : ({a + a, a + b, b + b} : Finset ℕ).card = 3 := by
    rw [card_insert_of_notMem]
    · rw [card_insert_of_notMem]
      · rw [card_singleton]
      · intro h_mem; simp only [mem_singleton] at h_mem; omega
    · intro h_mem; simp only [mem_insert, mem_singleton] at h_mem; omega
  have h_card_le := card_le_card h_sub
  omega
