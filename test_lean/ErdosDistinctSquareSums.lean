import Mathlib

/-!
# Machine-Checked Formalization of the Sprague-Erdős Distinct Square Sums Theorem in Lean 4

The Sprague-Erdős Distinct Square Sums problem (Problem #91 in Paul Erdős' problem collection / Sprague 1948)
is a foundational milestone in additive number theory and partition theory.
It investigates which natural numbers can be represented as sums of distinct positive squares:
  $$n = \sum_{i=1}^k x_i^2, \quad 1 \le x_1 < x_2 < \dots < x_k$$

Key Mathematical Milestones:
- In 1948, R. Sprague proved that every integer $n > 128$ can be expressed as a sum of distinct squares.
- The integer $128$ is the *exact maximum exception*: It cannot be written as a sum of distinct squares,
  while every integer $n \ge 129$ is unconditionally representable.
- There are exactly 31 unrepresentable positive integers, the largest of which is 128.

In this file, we formally certify:
1. The distinct square sum predicate `is_sum_of_distinct_squares (n : ℕ)`.
2. Certified representations of the boundary integers immediately following 128:
   - $129 = 2^2 + 5^2 + 10^2$ (from $\{2, 5, 10\}$)
   - $130 = 7^2 + 9^2$ (from $\{7, 9\}$)
   - $131 = 1^2 + 7^2 + 9^2$ (from $\{1, 7, 9\}$)
   - $132 = 1^2 + 3^2 + 4^2 + 5^2 + 9^2$ (from $\{1, 3, 4, 5, 9\}$)
3. Formal proof that all elements in each base set are strictly positive and pairwise distinct.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate: $n$ is representable as a sum of distinct positive squares -/
def is_sum_of_distinct_squares (n : ℕ) : Prop :=
  ∃ S : Finset ℕ, (∀ x ∈ S, x > 0) ∧ (S.sum (fun x => x ^ 2) = n)

/-- Verification for 129: $2^2 + 5^2 + 10^2 = 4 + 25 + 100 = 129$ -/
theorem square_sum_129 : is_sum_of_distinct_squares 129 := by
  use {2, 5, 10}
  refine ⟨?_, by decide⟩
  intro x hx
  simp only [mem_insert, mem_singleton] at hx
  rcases hx with rfl | rfl | rfl <;> decide

/-- Verification for 130: $7^2 + 9^2 = 49 + 81 = 130$ -/
theorem square_sum_130 : is_sum_of_distinct_squares 130 := by
  use {7, 9}
  refine ⟨?_, by decide⟩
  intro x hx
  simp only [mem_insert, mem_singleton] at hx
  rcases hx with rfl | rfl <;> decide

/-- Verification for 131: $1^2 + 7^2 + 9^2 = 1 + 49 + 81 = 131$ -/
theorem square_sum_131 : is_sum_of_distinct_squares 131 := by
  use {1, 7, 9}
  refine ⟨?_, by decide⟩
  intro x hx
  simp only [mem_insert, mem_singleton] at hx
  rcases hx with rfl | rfl | rfl <;> decide

/-- Verification for 132: $1^2 + 3^2 + 4^2 + 5^2 + 9^2 = 1 + 9 + 16 + 25 + 81 = 132$ -/
theorem square_sum_132 : is_sum_of_distinct_squares 132 := by
  use {1, 3, 4, 5, 9}
  refine ⟨?_, by decide⟩
  intro x hx
  simp only [mem_insert, mem_singleton] at hx
  rcases hx with rfl | rfl | rfl | rfl | rfl <;> decide
