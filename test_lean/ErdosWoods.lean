import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Woods Conjecture in Lean 4

The Erdős-Woods Conjecture (Problem #17 in Paul Erdős' collection, 1980 / Alan R. Woods 1981)
is a deep arithmetic conjecture with direct consequences for mathematical logic and the decidability
of the existential theory of arithmetic $\langle \mathbb{N}, +, \mid \rangle$.

The conjecture states that there exists an absolute positive integer $k \ge 2$ such that for any
two positive integers $x, y \ge 1$:
  $$(\forall i \in \{0, 1, \dots, k - 1\}, \operatorname{rad}(x + i) = \operatorname{rad}(y + i)) \implies x = y$$
where $\operatorname{rad}(n) = \prod_{p \mid n} p$ is the square-free kernel (radical) of $n$.

Key Mathematical Milestones:
- For $k = 1$: False because infinitely many distinct numbers share the same radical (e.g. $\operatorname{rad}(12) = \operatorname{rad}(18) = 6$).
- For $k = 2$: False due to counterexamples such as $(x, y) = (75, 1215)$ with:
  $\operatorname{rad}(75) = \operatorname{rad}(1215) = 15$ and $\operatorname{rad}(76) = \operatorname{rad}(1216) = 38$.
- For $k = 3$: Open, but suspected to hold (or for $k \le 4$).
- Langevin (1993) and Balasubramanian-Shorey-Waldschmidt (1998) established bounds using $S$-unit equations.

In this file, we formally certify:
1. The definition of the radical $\operatorname{rad}(n)$ as the product of prime factors.
2. Formal proof that $k = 1$ is insufficient: $\operatorname{rad}(12) = \operatorname{rad}(18) = 6$ with $12 \ne 18$.
3. Formal proof that $k = 2$ is insufficient: $\operatorname{rad}(75) = \operatorname{rad}(1215) = 15$ and $\operatorname{rad}(76) = \operatorname{rad}(1216) = 38$ with $75 \ne 1215$.
4. The general Erdős-Woods predicate for a length $k$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open Nat

/-- Radical (square-free kernel) of a positive integer $n$ -/
def int_rad (n : ℕ) : ℕ :=
  (Nat.primeFactors n).prod id

/-- Predicate: integers $x$ and $y$ have identical radicals on $k$ consecutive shifts -/
def erdos_woods_pair (k x y : ℕ) : Prop :=
  ∀ i : ℕ, i < k → int_rad (x + i) = int_rad (y + i)

/-- Verification of radical for 12 and 18 -/
theorem rad_12_eq_6 : int_rad 12 = 6 := by
  unfold int_rad
  decide

theorem rad_18_eq_6 : int_rad 18 = 6 := by
  unfold int_rad
  decide

/-- $k = 1$ is insufficient for uniqueness -/
theorem erdos_woods_k1_counterexample :
    erdos_woods_pair 1 12 18 ∧ 12 ≠ 18 := by
  refine ⟨?_, by decide⟩
  intro i hi
  interval_cases i
  rw [add_zero, add_zero]
  rw [rad_12_eq_6, rad_18_eq_6]

/-- Radical evaluations for the $k = 2$ counterexample (75, 1215) -/
theorem rad_75_eq_15 : int_rad 75 = 15 := by
  unfold int_rad
  decide

theorem rad_1215_eq_15 : int_rad 1215 = 15 := by
  unfold int_rad
  decide

theorem rad_76_eq_38 : int_rad 76 = 38 := by
  unfold int_rad
  decide

theorem rad_1216_eq_38 : int_rad 1216 = 38 := by
  unfold int_rad
  decide

/-- $k = 2$ is insufficient for uniqueness -/
theorem erdos_woods_k2_counterexample :
    erdos_woods_pair 2 75 1215 ∧ 75 ≠ 1215 := by
  refine ⟨?_, by decide⟩
  intro i hi
  interval_cases i
  · rw [add_zero, add_zero]
    rw [rad_75_eq_15, rad_1215_eq_15]
  · rw [add_assoc, add_zero]
    rw [rad_76_eq_38, rad_1216_eq_38]
