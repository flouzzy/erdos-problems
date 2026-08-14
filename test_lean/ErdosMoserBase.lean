import Mathlib

/-!
# Erdős-Moser Equation: Base Cases and Uniqueness for m=3 in Lean 4

The Erdős-Moser Diophantine equation is:
  $$ 1^k + 2^k + \dots + (m-1)^k = m^k $$
The only known positive integer solution is $m=3, k=1$ ($1^1 + 2^1 = 3^1$).
Leo Moser (1953) conjectured there are no other solutions and proved $m > 10^{10^6}$.

Here we formally prove (with 0 `sorry`):
1. For any $k \ge 2$, $1 + 2^k < 3^k$ strictly.
2. Consequently, for $m=3$, the only possible power is $k=1$.
-/

set_option linter.unusedVariables false

def erdos_moser_sum (m k : ℕ) : ℕ :=
  (Finset.range m).sum (fun i => i^k)

def is_erdos_moser_sol (m k : ℕ) : Prop :=
  m > 0 ∧ k > 0 ∧ erdos_moser_sum m k = m^k

/-- For all k ≥ 2, 1 + 2^k < 3^k -/
theorem pow_ineq_two_three (k : ℕ) (hk : k ≥ 2) : 1 + 2^k < 3^k := by
  induction' k, hk using Nat.le_induction with n hn ih
  · -- base case n = 2: 1 + 4 < 9
    decide
  · -- induction step
    have h_pow3_pos : 3^n > 0 := by positivity
    calc
      1 + 2^(n + 1) = 1 + 2 * 2^n := by ring
      _ ≤ 2 * (1 + 2^n) := by omega
      _ < 2 * 3^n := Nat.mul_lt_mul_of_pos_left ih (by decide)
      _ < 3 * 3^n := Nat.mul_lt_mul_of_pos_right (by decide) h_pow3_pos
      _ = 3^(n + 1) := by ring

/-- For m = 3, erdos_moser_sum 3 k simplifies to 1 + 2^k -/
theorem erdos_moser_sum_three (k : ℕ) (hk : k > 0) :
    erdos_moser_sum 3 k = 1 + 2^k := by
  unfold erdos_moser_sum
  rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_zero]
  have h0 : 0^k = 0 := by
    cases k
    · contradiction
    · rfl
  have h1 : 1^k = 1 := Nat.one_pow k
  omega

/-- For m = 3, k cannot be ≥ 2 -/
theorem erdos_moser_m_three_no_sol_ge_two (k : ℕ) (hk : k ≥ 2) :
    ¬ is_erdos_moser_sol 3 k := by
  intro ⟨_, hk_pos, heq⟩
  have h_sum := erdos_moser_sum_three k hk_pos
  rw [h_sum] at heq
  have h_lt := pow_ineq_two_three k hk
  omega
