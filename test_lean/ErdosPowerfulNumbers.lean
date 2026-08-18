import Mathlib

/-!
# Erdős Problem #27: Consecutive Powerful Numbers in Lean 4

A natural number $n$ is *powerful* (or 2-full / square-full) if for every prime $p$,
$p \mid n \implies p^2 \mid n$.

Paul Erdős studied consecutive powerful numbers:
1. Are there pairs of consecutive powerful numbers $(n, n+1)$?
   Yes: $(8, 9)$ since $8 = 2^3$ and $9 = 3^2$.
2. Can there be four consecutive powerful numbers $(n, n+1, n+2, n+3)$?
   No: Among any four consecutive integers, exactly one is $\equiv 2 \pmod 4$, which cannot be powerful.
3. Can there be three consecutive powerful numbers $(n, n+1, n+2)$?
   Only possibly if $n \equiv 3 \pmod 4$, since for all $n \not\equiv 3 \pmod 4$, one of them is $\equiv 2 \pmod 4$.

In this file, we formally prove in Lean 4 (with 0 `sorry`):
- 8 and 9 are powerful numbers.
- There exists a consecutive pair of powerful numbers $(8, 9)$.
- Every integer $m \equiv 2 \pmod 4$ is divisible by 2 but not by 4, hence is NOT powerful.
- **Four Consecutive Impossibility Theorem:** There do NOT exist four consecutive powerful numbers $(n, n+1, n+2, n+3)$.
- **Three Consecutive Modulo 4 Constraint:** Any triplet of consecutive powerful numbers must have $n \equiv 3 \pmod 4$.
-/

set_option linter.unusedVariables false

open Nat

/-- A natural number n is powerful if every prime divisor divides it to at least the second power -/
def is_powerful (n : ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → p ∣ n → p^2 ∣ n

/-- 8 is powerful since 8 = 2^3 -/
theorem eight_is_powerful : is_powerful 8 := by
  intro p hp hdiv
  have hp_le : p ≤ 8 := Nat.le_of_dvd (by decide) hdiv
  interval_cases p
  · exfalso; revert hp; decide
  · exfalso; revert hp; decide
  · -- p = 2: 4 | 8
    decide
  · -- p = 3: 3 does not divide 8
    exfalso; revert hdiv; decide
  · exfalso; revert hp; decide
  · -- p = 5: 5 does not divide 8
    exfalso; revert hdiv; decide
  · exfalso; revert hp; decide
  · -- p = 7: 7 does not divide 8
    exfalso; revert hdiv; decide
  · exfalso; revert hp; decide

/-- 9 is powerful since 9 = 3^2 -/
theorem nine_is_powerful : is_powerful 9 := by
  intro p hp hdiv
  have hp_le : p ≤ 9 := Nat.le_of_dvd (by decide) hdiv
  interval_cases p
  · exfalso; revert hp; decide
  · exfalso; revert hp; decide
  · -- p = 2: 2 does not divide 9
    exfalso; revert hdiv; decide
  · -- p = 3: 9 | 9
    decide
  · exfalso; revert hp; decide
  · -- p = 5: 5 does not divide 9
    exfalso; revert hdiv; decide
  · exfalso; revert hp; decide
  · -- p = 7: 7 does not divide 9
    exfalso; revert hdiv; decide
  · exfalso; revert hp; decide
  · exfalso; revert hp; decide

/-- Theorem: There exists a pair of consecutive powerful numbers: (8, 9) -/
theorem consecutive_powerful_pair_exists : ∃ n : ℕ, is_powerful n ∧ is_powerful (n + 1) := by
  use 8
  exact ⟨eight_is_powerful, nine_is_powerful⟩

/-- Lemma: Any integer m ≡ 2 [mod 4] is not powerful -/
theorem mod4_two_not_powerful (m : ℕ) (h_mod : m % 4 = 2) : ¬ is_powerful m := by
  intro h_pow
  have h_two_dvd : 2 ∣ m := by
    have : 2 ∣ 4 := by decide
    have h_mod2 : m % 2 = (m % 4) % 2 := by rw [Nat.mod_mod_of_dvd _ this]
    rw [h_mod] at h_mod2
    exact Nat.dvd_of_mod_eq_zero h_mod2
  have h_two_prime : Nat.Prime 2 := Nat.prime_two
  have h_four_dvd : 2^2 ∣ m := h_pow 2 h_two_prime h_two_dvd
  have h_mod4_zero : m % 4 = 0 := Nat.mod_eq_zero_of_dvd h_four_dvd
  omega

/--
Theorem (Erdős Four Consecutive Powerful Numbers Impossibility):
There do NOT exist four consecutive powerful numbers (n, n+1, n+2, n+3).
-/
theorem no_four_consecutive_powerful (n : ℕ) :
    ¬ (is_powerful n ∧ is_powerful (n + 1) ∧ is_powerful (n + 2) ∧ is_powerful (n + 3)) := by
  rintro ⟨h0_pow, h1_pow, h2_pow, h3_pow⟩
  have h_mod : n % 4 = 0 ∨ n % 4 = 1 ∨ n % 4 = 2 ∨ n % 4 = 3 := by omega
  rcases h_mod with h0 | h1 | h2 | h3
  · -- If n % 4 = 0, then (n + 2) % 4 = 2
    have h : (n + 2) % 4 = 2 := by omega
    exact mod4_two_not_powerful (n + 2) h h2_pow
  · -- If n % 4 = 1, then (n + 1) % 4 = 2
    have h : (n + 1) % 4 = 2 := by omega
    exact mod4_two_not_powerful (n + 1) h h1_pow
  · -- If n % 4 = 2, then n % 4 = 2
    exact mod4_two_not_powerful n h2 h0_pow
  · -- If n % 4 = 3, then (n + 3) % 4 = 2
    have h : (n + 3) % 4 = 2 := by omega
    exact mod4_two_not_powerful (n + 3) h h3_pow

/--
Theorem: If three consecutive integers (n, n+1, n+2) are powerful, then necessarily n ≡ 3 [mod 4].
-/
theorem three_consecutive_powerful_mod4 (n : ℕ)
    (h_three : is_powerful n ∧ is_powerful (n + 1) ∧ is_powerful (n + 2)) :
    n % 4 = 3 := by
  obtain ⟨h0_pow, h1_pow, h2_pow⟩ := h_three
  by_contra h_ne
  have h_mod : n % 4 = 0 ∨ n % 4 = 1 ∨ n % 4 = 2 := by omega
  rcases h_mod with h0 | h1 | h2
  · have h : (n + 2) % 4 = 2 := by omega
    exact mod4_two_not_powerful (n + 2) h h2_pow
  · have h : (n + 1) % 4 = 2 := by omega
    exact mod4_two_not_powerful (n + 1) h h1_pow
  · exact mod4_two_not_powerful n h2 h0_pow
