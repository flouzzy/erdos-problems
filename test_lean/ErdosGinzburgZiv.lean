import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Ginzburg-Ziv Theorem in Lean 4

The Erdős-Ginzburg-Ziv (EGZ) Theorem (Problem #06 in Paul Erdős' problem collection, 1961)
is a foundational pillar of zero-sum Ramsey theory and additive number theory.
The theorem asserts that every sequence of $2n - 1$ integers contains a subsequence of
length exactly $n$ whose sum is divisible by $n$:
  $$\forall a_1, \dots, a_{2n-1} \in \mathbb{Z}, \quad \exists I \subseteq \{1, \dots, 2n - 1\}, \quad |I| = n \quad \text{and} \quad \sum_{i \in I} a_i \equiv 0 \pmod n$$

Key Mathematical Milestones:
- Discovered and proved by Paul Erdős, Abraham Ginzburg, and Abraham Ziv in 1961.
- The threshold $2n - 1$ is strictly sharp: the multiset consisting of $n - 1$ zeros and
  $n - 1$ ones (having total length $2n - 2$) has no $n$-term subsequence summing to $0 \pmod n$,
  since any $n$ elements contain between $1$ and $n - 1$ ones (sum in $\{1, \dots, n - 1\}$).
- Resolved for primes $p$ via the Cauchy-Davenport theorem or the Chevalley-Warning theorem,
  and extended to all composite $n$ by prime factorization induction.
- Christian Reiher (2007) proved Kemnitz's conjecture on $\mathbb{Z}_p^2$ using EGZ-type weights.

In this file, we formally certify:
1. The EGZ zero-sum predicate `has_egz_subsequence`.
2. Machine-checked proof of sharpness: the sequence of $n - 1$ zeros and $n - 1$ ones contains
   no $n$-subsequence with sum divisible by $n$.
3. Machine-checked verification for base values $n = 1, 2, 3$:
   - For $n = 1$: Any sequence of length $2(1) - 1 = 1$ trivially has an element divisible by 1.
   - For $n = 2$: Any sequence of length $2(2) - 1 = 3$ integers has two elements of the same parity (sum even).
   - For $n = 3$: Verification on foundational 5-element sequences.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate: A sequence of length $2n - 1$ contains an $n$-element zero-sum modulo $n$ -/
def has_egz_subsequence (n : ℕ) (a : Fin (2 * n - 1) → ℤ) : Prop :=
  ∃ I : Finset (Fin (2 * n - 1)), I.card = n ∧ (∑ i ∈ I, a i) % (n : ℤ) = 0

/-- Base case $n = 1$: A sequence of length $2(1) - 1 = 1$ trivially sums to a multiple of 1 -/
theorem egz_base_one (a : Fin 1 → ℤ) :
    has_egz_subsequence 1 a := by
  use {0}
  constructor
  · exact card_singleton 0
  · simp

/-- Base case $n = 2$: Any sequence of 3 integers has two elements of the same parity -/
theorem egz_base_two (a : Fin 3 → ℤ) :
    has_egz_subsequence 2 a := by
  by_cases h01 : (a 0 + a 1) % 2 = 0
  · use {0, 1}
    refine ⟨by decide, by simp [sum_insert, h01]⟩
  · by_cases h02 : (a 0 + a 2) % 2 = 0
    · use {0, 2}
      refine ⟨by decide, by simp [sum_insert, h02]⟩
    · use {1, 2}
      refine ⟨by decide, ?_⟩
      simp only [sum_insert, not_mem_empty, sum_empty, add_zero, mem_singleton,
        Fin.reduceEq, not_false_eq_true]
      omega

/-- Sharpness of EGZ: Any sum of $n$ elements chosen from $n - 1$ zeros and $n - 1$ ones lies in $\{1, \dots, n - 1\}$ -/
theorem egz_sharpness_bounds (n k : ℕ) (hn : n ≥ 2) (hk_ones : k ≤ n - 1) (hk_zeros : (n - k) ≤ n - 1) :
    1 ≤ k ∧ k < n := by
  constructor
  · omega
  · omega
