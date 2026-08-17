import Mathlib

/-!
# Erdős-Straus Conjecture: Formally Verified Universal Parameterizations in Lean 4

The Erdős-Straus conjecture asserts that for all integers $n \ge 2$,
the Diophantine equation
  $$ \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} $$
admits a solution in positive integers $(x, y, z) \in \mathbb{N}_{>0}^3$.
Equivalently, cleared of denominators:
  $$ 4 x y z = n (x y + y z + x z) $$

In this file, we prove:
1. The **Universal 3-Parameter Schinzel-Mordell Theorem**:
   For any parameters $(a, b, c) \in (\mathbb{N}_{>0})^3$, if $4abc = c \cdot n + a + b$,
   then $(x, y, z) = (ab, acn, bcn)$ is an exact positive integer solution.
2. The **Master Modulo 24 Reduction Theorem**:
   Every integer $n \ge 2$ with $n \not\equiv 1 \pmod{24}$ admits a solution in $(\mathbb{N}_{>0})^3$.
   This covers $23/24 = 95.83\%$ of all residue classes.
-/

set_option linter.unusedVariables false

def is_erdos_straus_sol (n x y z : ℕ) : Prop :=
  x > 0 ∧ y > 0 ∧ z > 0 ∧ 4 * x * y * z = n * (x * y + y * z + x * z)

/--
Universal 3-Parameter Schinzel-Mordell Theorem:
For any positive parameters a, b, c, if 4 * a * b * c = c * n + a + b,
then (ab, acn, bcn) is an exact solution to the Erdős-Straus equation.
-/
theorem erdos_straus_universal_identity (a b c n : ℕ)
    (ha : a > 0) (hb : b > 0) (hc : c > 0) (hn_pos : n > 0)
    (h_eq : 4 * a * b * c = c * n + a + b) :
    is_erdos_straus_sol n (a * b) (a * c * n) (b * c * n) := by
  have hx : a * b > 0 := by positivity
  have hy : a * c * n > 0 := by positivity
  have hz : b * c * n > 0 := by positivity
  refine ⟨hx, hy, hz, ?_⟩
  have h_lhs : 4 * (a * b) * (a * c * n) * (b * c * n) = (4 * a * b * c) * a * b * c * n^2 := by ring
  have h_rhs : n * (a * b * (a * c * n) + a * c * n * (b * c * n) + a * b * (b * c * n)) =
      (c * n + a + b) * a * b * c * n^2 := by ring
  rw [h_lhs, h_rhs, h_eq]

/-- Case n ≡ 0 mod 2, i.e., n = 2k (k ≥ 1) : 4/(2k) = 1/k + 1/(2k) + 1/(2k) -/
theorem erdos_straus_even (k : ℕ) (hk : k ≥ 1) :
    ∃ x y z : ℕ, is_erdos_straus_sol (2 * k) x y z := by
  use k, 2 * k, 2 * k
  refine ⟨by omega, by omega, by omega, ?_⟩
  ring

/-- Case n ≡ 0 mod 3, i.e., n = 3k (k ≥ 1) : 4/(3k) = 1/k + 1/(6k) + 1/(6k) -/
theorem erdos_straus_mod3_eq0 (k : ℕ) (hk : k ≥ 1) :
    ∃ x y z : ℕ, is_erdos_straus_sol (3 * k) x y z := by
  have hx : k > 0 := by omega
  have hy : 6 * k > 0 := by omega
  use k, 6 * k, 6 * k
  refine ⟨hx, hy, hy, ?_⟩
  ring

/-- Case n ≡ 2 mod 3, i.e., n = 3k + 2 (k ≥ 0) : 4/n = 1/(k+1) + 1/n + 1/((k+1)n) -/
theorem erdos_straus_mod3_eq2 (k : ℕ) :
    ∃ x y z : ℕ, is_erdos_straus_sol (3 * k + 2) x y z := by
  have hx : k + 1 > 0 := by omega
  have hy : 3 * k + 2 > 0 := by omega
  have hz : (k + 1) * (3 * k + 2) > 0 := by positivity
  use k + 1, 3 * k + 2, (k + 1) * (3 * k + 2)
  refine ⟨hx, hy, hz, ?_⟩
  ring

/-- Case n ≡ 3 mod 4, i.e., n = 4k + 3 (k ≥ 0) : 4/n = 1/(k+1) + 1/(2(k+1)n) + 1/(2(k+1)n) -/
theorem erdos_straus_mod4_eq3 (k : ℕ) :
    ∃ x y z : ℕ, is_erdos_straus_sol (4 * k + 3) x y z := by
  have hx : k + 1 > 0 := by omega
  have hy : 2 * (k + 1) * (4 * k + 3) > 0 := by positivity
  use k + 1, 2 * (k + 1) * (4 * k + 3), 2 * (k + 1) * (4 * k + 3)
  refine ⟨hx, hy, hy, ?_⟩
  ring

/-- Case n ≡ 5 mod 8, i.e., n = 8k + 5 (k ≥ 0) : 4/n = 1/(2(k+1)) + 1/((k+1)n) + 1/(2(k+1)n) -/
theorem erdos_straus_mod8_eq5 (k : ℕ) :
    ∃ x y z : ℕ, is_erdos_straus_sol (8 * k + 5) x y z := by
  have hx : 2 * (k + 1) > 0 := by omega
  have hy : (k + 1) * (8 * k + 5) > 0 := by positivity
  have hz : 2 * (k + 1) * (8 * k + 5) > 0 := by positivity
  use 2 * (k + 1), (k + 1) * (8 * k + 5), 2 * (k + 1) * (8 * k + 5)
  refine ⟨hx, hy, hz, ?_⟩
  ring

/--
Master Reduction Theorem for Erdős-Straus:
For every integer $n \ge 2$, if $n \not\equiv 1 \pmod{24}$, then there exists
a solution $(x, y, z) \in \mathbb{N}_{>0}^3$ to the Erdős-Straus equation.
-/
theorem erdos_straus_not_mod24_one (n : ℕ) (hn : n ≥ 2) (h24 : n % 24 ≠ 1) :
    ∃ x y z : ℕ, is_erdos_straus_sol n x y z := by
  have h_cases :
    n % 2 = 0 ∨
    n % 3 = 0 ∨
    n % 3 = 2 ∨
    n % 4 = 3 ∨
    n % 8 = 5 := by
      omega
  rcases h_cases with h_even | h_mod3_0 | h_mod3_2 | h_mod4_3 | h_mod8_5
  · obtain ⟨k, hk⟩ : ∃ k, n = 2 * k := ⟨n / 2, by omega⟩
    have hk_pos : k ≥ 1 := by omega
    subst hk
    exact erdos_straus_even k hk_pos
  · obtain ⟨k, hk⟩ : ∃ k, n = 3 * k := ⟨n / 3, by omega⟩
    have hk_pos : k ≥ 1 := by omega
    subst hk
    exact erdos_straus_mod3_eq0 k hk_pos
  · obtain ⟨k, hk⟩ : ∃ k, n = 3 * k + 2 := ⟨n / 3, by omega⟩
    subst hk
    exact erdos_straus_mod3_eq2 k
  · obtain ⟨k, hk⟩ : ∃ k, n = 4 * k + 3 := ⟨n / 4, by omega⟩
    subst hk
    exact erdos_straus_mod4_eq3 k
  · obtain ⟨k, hk⟩ : ∃ k, n = 8 * k + 5 := ⟨n / 8, by omega⟩
    subst hk
    exact erdos_straus_mod8_eq5 k
