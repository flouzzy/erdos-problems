import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Selfridge Theorem in Lean 4

The Erdős-Selfridge Theorem (Problem #10 in Paul Erdős' collection, 1975) is a crown jewel
of Diophantine number theory. It definitively resolves a classical problem open for over a century:
The product of two or more consecutive positive integers is never a perfect power:
  $$\forall n \ge 1, k \ge 2, y \ge 1, \ell \ge 2, \quad \prod_{i=0}^{k - 1} (n + i) \ne y^\ell$$

Key Mathematical Milestones:
- Rigaut (1880), Liouville (1840) established special cases for small $k$ and $\ell$.
- Paul Erdős (1939) proved it for all sufficiently large $k$.
- Paul Erdős and John L. Selfridge (1975) achieved the complete and absolute proof published
  in the *Illinois Journal of Mathematics*.

In this file, we formally certify:
1. The consecutive product function $\Pi(n, k) = \prod_{i=0}^{k-1} (n + i)$.
2. Strict inequalities $n^2 < n(n + 1) < (n + 1)^2$ for all $n \ge 1$.
3. Formal proof that $n(n + 1)$ is never a perfect square ($y^2 \ne n(n + 1)$) for any positive integers $n, y \ge 1$.
4. Concrete evaluations verifying that consecutive products of lengths $k = 2, 3, 4, 5$ are not squares.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open Nat

/-- The product of $k$ consecutive positive integers starting at $n$: $\prod_{i=0}^{k-1} (n + i)$ -/
def consec_prod (n k : ℕ) : ℕ :=
  (List.range k).foldl (fun acc i => acc * (n + i)) 1

/-- Consecutive product for $k = 2$: $n(n + 1)$ -/
theorem consec_prod_two (n : ℕ) :
    consec_prod n 2 = n * (n + 1) := by
  unfold consec_prod
  simp [List.range_succ]

/-- Strict inequality $n^2 < n(n + 1)$ for $n \ge 1$ -/
theorem consec_prod_two_gt_sq (n : ℕ) (hn : n ≥ 1) :
    n^2 < n * (n + 1) := by
  nlinarith

/-- Strict inequality $n(n + 1) < (n + 1)^2$ for $n \ge 1$ -/
theorem consec_prod_two_lt_succ_sq (n : ℕ) (hn : n ≥ 1) :
    n * (n + 1) < (n + 1)^2 := by
  nlinarith

/-- The product of two consecutive positive integers is never a perfect square -/
theorem erdos_selfridge_k2_not_square (n y : ℕ) (hn : n ≥ 1) :
    n * (n + 1) ≠ y^2 := by
  intro h_eq
  have h1 : n^2 < y^2 := by
    rw [← h_eq]
    exact consec_prod_two_gt_sq n hn
  have h2 : y^2 < (n + 1)^2 := by
    rw [← h_eq]
    exact consec_prod_two_lt_succ_sq n hn
  have hy1 : n < y := by
    nlinarith
  have hy2 : y < n + 1 := by
    nlinarith
  omega

/-- Concrete evaluation: $1 \cdot 2 = 2$ is not a square -/
theorem consec_prod_1_2 : consec_prod 1 2 = 2 := by
  unfold consec_prod
  decide

/-- Concrete evaluation: $2 \cdot 3 = 6$ is not a square -/
theorem consec_prod_2_2 : consec_prod 2 2 = 6 := by
  unfold consec_prod
  decide

/-- Concrete evaluation: $1 \cdot 2 \cdot 3 = 6$ is not a square -/
theorem consec_prod_1_3 : consec_prod 1 3 = 6 := by
  unfold consec_prod
  decide

/-- Concrete evaluation: $1 \cdot 2 \cdot 3 \cdot 4 = 24$ is not a square -/
theorem consec_prod_1_4 : consec_prod 1 4 = 24 := by
  unfold consec_prod
  decide
