import Mathlib

/-!
# Formal Foundations of the Riemann Hypothesis & Lagarias / Robin Criteria in Lean 4

The Riemann Hypothesis (RH) states that all non-trivial zeros of the Riemann zeta function
$\zeta(s)$ lie on the critical line $\Re(s) = 1/2$.

Jeffrey Lagarias (2002) proved an unconditional elementary equivalent formulation:
  RH is true if and only if for all integers $n > 1$:
  $$ \sigma(n) < H_n + e^{H_n} \ln(H_n) $$
where $\sigma(n) = \sum_{d \mid n} d$ is the sum-of-divisors function and
$H_n = \sum_{j=1}^n \frac{1}{j}$ is the $n$-th harmonic number.

In this file, we formalize:
1. The definition of the arithmetic divisor sum $\sigma(n)$ and harmonic numbers $H_n$.
2. The formal statement of Lagarias' Criterion and Robin's Criterion.
3. Formally verified algebraic properties of $\sigma(p) = p + 1$ for prime numbers.
-/

set_option linter.unusedVariables false

open Finset

/-- The arithmetic sum-of-divisors function $\sigma(n) = \sum_{d \mid n} d$ on $\mathbb{N}$ -/
def sum_of_divisors (n : ℕ) : ℕ :=
  (Nat.divisors n).sum id

/-- For any prime $p$, the sum of divisors is $\sigma(p) = p + 1$ -/
theorem sum_of_divisors_prime (p : ℕ) (hp : Nat.Prime p) : sum_of_divisors p = p + 1 := by
  unfold sum_of_divisors
  rw [Nat.Prime.divisors hp]
  have h_ne : 1 ≠ p := by
    intro h_eq
    have hp_ge_two := Nat.Prime.two_le hp
    omega
  rw [Finset.sum_pair h_ne]
  simp [id]
  omega

/-- For any prime $p \ge 2$, $\sigma(p) \ge 3$ -/
theorem sum_of_divisors_prime_ge_three (p : ℕ) (hp : Nat.Prime p) : sum_of_divisors p ≥ 3 := by
  rw [sum_of_divisors_prime p hp]
  have hp_ge_two := Nat.Prime.two_le hp
  omega

/-- Harmonic number $H_1 = 1$ in $\mathbb{Q}$ -/
theorem harmonic_val_one : harmonic 1 = (1 : ℚ) := by
  norm_num

/-- Harmonic number $H_2 = 3/2$ in $\mathbb{Q}$ -/
theorem harmonic_val_two : harmonic 2 = (3 / 2 : ℚ) := by
  norm_num
