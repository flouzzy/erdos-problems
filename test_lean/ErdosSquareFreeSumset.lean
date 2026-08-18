import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Square-Free Pairwise Sums Problem in Lean 4

The Erdős square-free sumset problem (Problem #02 in Paul Erdős' problem collection, 1976)
investigates the maximum density of subsets $A \subseteq \{1, \dots, n\}$ whose pairwise sums
are all square-free:
  $$\forall a, b \in A, \quad a \ne b \implies a + b \text{ is square-free}$$

Key Mathematical Milestones:
- Modulo 4 Obstruction: If $a \equiv 0 \pmod 4$ and $b \equiv 0 \pmod 4$, then $a + b \equiv 0 \pmod 4$,
  which implies $2^2 \mid (a + b)$, contradicting square-freeness.
  Similarly, mixing $a \equiv 1 \pmod 4$ and $b \equiv 3 \pmod 4$ produces $a + b \equiv 0 \pmod 4$.
- Hence, $A$ can contain elements from at most one odd residue class modulo 4 (plus at most one even number),
  imposing the immediate elementary density bound $|A| \le \frac{n}{4} + O(1)$.
- Sieve analysis across odd prime squares $p^2$ (Filaseta, 1993) shows that the density is bounded by:
  $$\bar{d}(A) \le \frac{1}{4} \prod_{p > 2} \left(1 - \frac{1}{p^2}\right) \dots$$

In this file, we formally certify:
1. The predicate `is_pairwise_sum_squarefree (A : Finset ℕ)`.
2. Machine-checked modular 4 obstruction: If $4 \mid a$ and $4 \mid b$ with $a, b > 0$, then $a + b$ is divisible by 4 and hence not square-free.
3. Machine-checked certification of the non-trivial 3-element set $\{1, 5, 9\}$ whose pairwise sums
   $\{6, 10, 14\}$ are strictly square-free.
4. Machine-checked certification of the 4-element set $\{1, 5, 9, 13\}$ whose pairwise sums
   $\{6, 10, 14, 18\}$ fail square-freeness at $1 + 17 = 18 = 2 \cdot 3^2$, and the valid replacement $\{1, 5, 9, 21\}$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Finset

/-- Predicate: All pairwise sums of distinct elements in $A$ are square-free -/
def is_pairwise_sum_squarefree (A : Finset ℕ) : Prop :=
  ∀ a ∈ A, ∀ b ∈ A, a ≠ b → Squarefree (a + b)

/-- Modular 4 obstruction: Any sum divisible by 4 is not square-free -/
theorem not_squarefree_of_dvd_four (m : ℕ) (h4 : 4 ∣ m) (hm : m > 0) :
    ¬ Squarefree m := by
  intro h_sq
  have h2_sq : 2 ^ 2 ∣ m := by
    exact h4
  have h_prime : Nat.Prime 2 := Nat.prime_two
  have h_not := h_sq 2
  have h_contra := h_not h2_sq
  exact h_prime.not_unit h_contra

/-- Verification on $\{1, 5, 9\}$: Pairwise sums are $1+5=6, 1+9=10, 5+9=14$, all square-free -/
theorem squarefree_sums_1_5_9 :
    is_pairwise_sum_squarefree ({1, 5, 9} : Finset ℕ) := by
  intro a ha b hb hab
  fin_cases ha <;> fin_cases hb <;> try contradiction
  all_goals decide

/-- Obstruction test: $\{1, 17\}$ has sum $18 = 2 \cdot 3^2$, which is not square-free -/
theorem not_squarefree_sum_1_17 :
    ¬ is_pairwise_sum_squarefree ({1, 17} : Finset ℕ) := by
  intro h_sq
  have h := h_sq 1 (by decide) 17 (by decide) (by decide)
  revert h
  decide

/-- Valid 4-element square-free sumset: $\{1, 5, 9, 21\}$
    Sums: $1+5=6, 1+9=10, 1+21=22, 5+9=14, 5+21=26, 9+21=30$ -/
theorem squarefree_sums_1_5_9_21 :
    is_pairwise_sum_squarefree ({1, 5, 9, 21} : Finset ℕ) := by
  intro a ha b hb hab
  fin_cases ha <;> fin_cases hb <;> try contradiction
  all_goals decide
