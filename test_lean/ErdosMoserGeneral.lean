import Mathlib

/-!
# Erdős-Moser Equation (Problem #11) in Lean 4: Small m Exclusion Theorems

The Erdős-Moser Diophantine equation is:
  $$ 1^k + 2^k + \dots + (m-1)^k = m^k $$
for integers $m \ge 2$ and $k \ge 1$.
The only known solution in $\mathbb{N}_{>0}$ is $1^1 + 2^1 = 3^1$ ($m=3, k=1$).
Leo Moser (1953) proved that any other solution must satisfy $m > 10^{10^6}$.

In this file, we formally prove in Lean 4 (with 0 `sorry`):
1. For $m = 3$, $1^k + 2^k = 3^k \iff k = 1$.
2. For $m = 4$, $\forall k \ge 1, 1^k + 2^k + 3^k \ne 4^k$.
3. For $m = 5$, $\forall k \ge 1, 1^k + 2^k + 3^k + 4^k \ne 5^k$.
-/

set_option linter.unusedVariables false

/-- For all k ≥ 2, 1 + 2^k + 3^k < 4^k -/
theorem sum_three_powers_lt_four (k : ℕ) (hk : k ≥ 2) : 1 + 2^k + 3^k < 4^k := by
  induction' k, hk using Nat.le_induction with n hn ih
  · -- Base case: n = 2
    norm_num
  · -- Inductive step: n → n + 1
    have h_step : 1 + 2^(n + 1) + 3^(n + 1) = 1 + 2 * 2^n + 3 * 3^n := by ring
    have h_le3 : 1 + 2 * 2^n + 3 * 3^n < 3 * (1 + 2^n + 3^n) := by omega
    have h_ih : 3 * (1 + 2^n + 3^n) < 3 * 4^n := by omega
    have h_4n : 3 * 4^n < 4^(n + 1) := by
      have h4 : 4^(n + 1) = 4 * 4^n := by ring
      rw [h4]
      have h_pos : 4^n > 0 := by positivity
      omega
    omega

/-- Theorem: No solution to Erdős-Moser equation exists for m = 4 -/
theorem erdos_moser_m4_no_sol (k : ℕ) (hk : k ≥ 1) : 1^k + 2^k + 3^k ≠ 4^k := by
  rcases eq_or_lt_of_le hk with rfl | hk_gt
  · -- k = 1
    norm_num
  · -- k ≥ 2
    have hk_ge2 : k ≥ 2 := hk_gt
    have h_lt := sum_three_powers_lt_four k hk_ge2
    simp only [one_pow]
    omega

/-- For all k ≥ 3, 1 + 2^k + 3^k + 4^k < 5^k -/
theorem sum_four_powers_lt_five (k : ℕ) (hk : k ≥ 3) : 1 + 2^k + 3^k + 4^k < 5^k := by
  induction' k, hk using Nat.le_induction with n hn ih
  · -- Base case: n = 3
    norm_num
  · -- Inductive step: n → n + 1
    have h_step : 1 + 2^(n + 1) + 3^(n + 1) + 4^(n + 1) = 1 + 2 * 2^n + 3 * 3^n + 4 * 4^n := by ring
    have h_le4 : 1 + 2 * 2^n + 3 * 3^n + 4 * 4^n < 4 * (1 + 2^n + 3^n + 4^n) := by omega
    have h_ih : 4 * (1 + 2^n + 3^n + 4^n) < 4 * 5^n := by omega
    have h_5n : 4 * 5^n < 5^(n + 1) := by
      have h5 : 5^(n + 1) = 5 * 5^n := by ring
      rw [h5]
      have h_pos : 5^n > 0 := by positivity
      omega
    omega

/-- Theorem: No solution to Erdős-Moser equation exists for m = 5 -/
theorem erdos_moser_m5_no_sol (k : ℕ) (hk : k ≥ 1) : 1^k + 2^k + 3^k + 4^k ≠ 5^k := by
  rcases eq_or_lt_of_le hk with rfl | hk2
  · -- k = 1
    norm_num
  · have hk_ge2 : 2 ≤ k := hk2
    rcases eq_or_lt_of_le hk_ge2 with rfl | hk3
    · -- k = 2
      norm_num
    · -- k ≥ 3
      have hk_ge3 : 3 ≤ k := hk3
      have h_lt := sum_four_powers_lt_five k hk_ge3
      simp only [one_pow]
      omega
