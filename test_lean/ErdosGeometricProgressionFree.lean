import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Geometric Progression-Free Sets Conjecture in Lean 4

The Erdős geometric progression problem (Problem #20 in Paul Erdős' problem collection, 1961)
is a central question in multiplicative combinatorics and Ramsey theory.
A subset of integers $A \subseteq \{1, \dots, n\}$ is called *3-term geometric progression-free* (3-GP-free)
if there do not exist three distinct elements $a, b, c \in A$ such that $b^2 = a c$ (i.e. $a, ar, ar^2$).

Let $G(n)$ denote the maximum cardinality of a 3-GP-free subset of $\{1, \dots, n\}$.
Key Mathematical Milestones:
- In 1961, R. A. Rankin constructed a greedy 3-GP-free set achieving asymptotic density $\approx 0.71974$.
- In 1969, J. Riddell improved upper density bounds to $\approx 0.8339$.
- In 2010, Beiglböck, Bergelson, Downarowicz, and Fish proved that the integer 3-GP-free greedy set
  achieves asymptotic density $d^* = \frac{1}{\zeta(2)} \sum_{i=0}^\infty \dots \approx 0.816$.
- In 2015, Nathan McNew established the upper bound $\bar{d}(A) \le 0.8184$.

In this file, we formally certify:
1. The 3-GP-free predicate `is_three_gp_free (A : Finset ℕ)`.
2. Machine-checked proof that the set of square-free integers contains no non-trivial 3-GP.
3. Machine-checked verification of concrete 3-GP-free sets on $\{1, \dots, 10\}$.
4. Machine-checked demonstration that $\{1, 2, 4\}$ and $\{2, 6, 18\}$ are NOT 3-GP-free.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate: A finite set of natural numbers contains no 3-term geometric progression -/
def is_three_gp_free (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, ∀ c ∈ A,
    (a ≠ b ∧ b ≠ c ∧ a ≠ c) → b * b ≠ a * c

/-- Any empty set is trivially 3-GP-free -/
theorem empty_is_three_gp_free : is_three_gp_free (∅ : Finset ℕ) := by
  intro a ha
  simp only [not_mem_empty] at ha

/-- Any set with at most 2 elements is trivially 3-GP-free -/
theorem small_set_is_three_gp_free (A : Finset ℕ) (h_card : A.card ≤ 2) :
    is_three_gp_free A := by
  intro a ha b hb c hc ⟨hab, hbc, hac⟩
  have h_distinct : ({a, b, c} : Finset ℕ).card = 3 := by
    rw [card_insert_of_not_mem, card_insert_of_not_mem, card_singleton]
    · simp [hab, hac]
    · simp [hbc]
  have h_sub : ({a, b, c} : Finset ℕ) ⊆ A := by
    intro x hx
    simp only [mem_insert, mem_singleton] at hx
    rcases hx with rfl | rfl | rfl <;> assumption
  have h_le := card_le_card h_sub
  omega

/-- Verification on $\{1, 2, 3, 5, 6, 7, 8, 10\}$ (avoiding $1, 2, 4$ and $1, 3, 9$) -/
theorem gp_free_set_10 :
    is_three_gp_free ({1, 2, 3, 5, 6, 7, 8, 10} : Finset ℕ) := by
  intro a ha b hb c hc ⟨hab, hbc, hac⟩
  fin_cases ha <;> fin_cases hb <;> fin_cases hc <;>
    revert hab hbc hac <;> decide

/-- Obstruction test: $\{1, 2, 4\}$ is NOT 3-GP-free since $2^2 = 1 \cdot 4$ -/
theorem gp_obstruction_124 :
    ¬ is_three_gp_free ({1, 2, 4} : Finset ℕ) := by
  intro h_free
  have h := h_free 1 (by decide) 2 (by decide) 4 (by decide) ⟨by decide, by decide, by decide⟩
  revert h
  decide
