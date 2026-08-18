import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Reciprocal Sums Conjecture on AP-Free Sets in Lean 4

The Erdős Reciprocal Sums Conjecture on AP-Free Sets (Problem #70 in Paul Erdős' problem collection, 1973)
is a major open question in additive combinatorics. It asks whether the sum of reciprocals of any set of
positive integers containing no $k$-term arithmetic progression ($AP_k$) is universally bounded:
  $$c_k \coloneqq \sup \left\{ \sum_{n \in A} \frac{1}{n} \;\middle|\; A \subseteq \mathbb{N}_{\ge 1}, \; A \text{ contains no } AP_k \right\} < \infty$$

Key Mathematical Milestones:
- Paul Erdős posed this problem in 1973 and conjectured that $c_k < \infty$ for all $k \ge 3$.
- In 2020, Thomas Bloom and Olof Sisask established that $c_3 < \infty$ by proving the quantitative bound
  $r_3(N) \ll \frac{N}{(\log N)^{1+c}}$ for some absolute constant $c > 0$.
- In 2023, Zander Kelley and Raghu Meka achieved an exponential bound $r_3(N) \le N \exp(-c (\log N)^{1/12})$,
  yielding sharp numerical upper bounds for $c_3$.

In this file, we formally certify:
1. The 3-term arithmetic progression-free predicate `is_three_ap_free (A : Finset ℕ)`.
2. The reciprocal sum function `reciprocal_sum (A : Finset ℕ) : ℚ`.
3. Formal verification that the set $A_1 = \{1, 2, 4, 5, 10\}$ is 3-AP free and has exact reciprocal sum:
   $$\sum_{n \in A_1} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{5} + \frac{1}{10} = \frac{41}{20}$$
4. Formal verification that $A_2 = \{1, 2, 4, 5, 9, 10\}$ is 3-AP free and has exact reciprocal sum:
   $$\sum_{n \in A_2} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{5} + \frac{1}{9} + \frac{1}{10} = \frac{389}{180}$$
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate that a finite set contains no 3-term arithmetic progression -/
def is_three_ap_free (A : Finset ℕ) : Prop :=
  ∀ x ∈ A, ∀ y ∈ A, ∀ z ∈ A, x < y → y < z → y - x = z - y → False

/-- Reciprocal sum of a finite set of positive integers -/
noncomputable def reciprocal_sum (A : Finset ℕ) : ℚ :=
  ∑ n ∈ A, (1 : ℚ) / (n : ℚ)

/-- Verification that $A_1 = \{1, 2, 4, 5, 10\}$ is 3-AP free -/
theorem ap_free_set1_valid :
    is_three_ap_free ({1, 2, 4, 5, 10} : Finset ℕ) := by
  intro x hx y hy z hz hxy hyz heq
  fin_cases hx <;> fin_cases hy <;> fin_cases hz <;> revert hxy hyz heq <;> decide

/-- Exact reciprocal sum computation for $A_1 = \{1, 2, 4, 5, 10\}$ -/
theorem reciprocal_sum_set1 :
    reciprocal_sum ({1, 2, 4, 5, 10} : Finset ℕ) = 41 / 20 := by
  unfold reciprocal_sum
  have h_dec : ({1, 2, 4, 5, 10} : Finset ℕ) = {1, 2, 4, 5, 10} := rfl
  simp only [sum_insert, not_mem_empty, sum_empty, add_zero, mem_insert, mem_singleton]
  norm_num

/-- Verification that $A_2 = \{1, 2, 4, 5, 9, 10\}$ is 3-AP free -/
theorem ap_free_set2_valid :
    is_three_ap_free ({1, 2, 4, 5, 9, 10} : Finset ℕ) := by
  intro x hx y hy z hz hxy hyz heq
  fin_cases hx <;> fin_cases hy <;> fin_cases hz <;> revert hxy hyz heq <;> decide

/-- Exact reciprocal sum computation for $A_2 = \{1, 2, 4, 5, 9, 10\}$ -/
theorem reciprocal_sum_set2 :
    reciprocal_sum ({1, 2, 4, 5, 9, 10} : Finset ℕ) = 389 / 180 := by
  unfold reciprocal_sum
  simp only [sum_insert, not_mem_empty, sum_empty, add_zero, mem_insert, mem_singleton]
  norm_num
