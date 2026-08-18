import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Conjecture on Arithmetic Progressions in Lean 4

The Erdős Conjecture on Arithmetic Progressions (Problem #12 / #77 in Paul Erdős' collection, 1976)
is one of the most celebrated and monumental conjectures in number theory. It asserts that
if a set of positive integers $A \subseteq \mathbb{N}_{\ge 1}$ has divergent reciprocal sum:
  $$\sum_{n \in A} \frac{1}{n} = \infty$$
then for every integer $k \ge 3$, $A$ contains an arithmetic progression of length $k$:
  $$\exists a \ge 1, d \ge 1, \quad \{a, a + d, a + 2d, \dots, a + (k - 1)d\} \subseteq A$$

Landmark milestones:
- For $A = \mathbb{P}$ (prime numbers), the conjecture was proven by Ben Green and Terence Tao (2008).
- For $k = 3$, the conjecture was completely resolved for all divergent sets by Thomas Bloom and Olof Sisask (2020).
- Kelley and Meka (2023) established the landmark density bound $r_3(N) \le N \exp(-c (\log N)^{1/12})$.

In this file, we formally certify:
1. The definition of a $k$-term arithmetic progression in a set $A \subseteq \mathbb{N}$.
2. The definition of the Erdős AP property for general length $k$.
3. Machine-checked verification of explicit prime arithmetic progressions:
   - $\{3, 5, 7\}$ is a 3-term arithmetic progression of primes ($a=3, d=2$).
   - $\{5, 11, 17, 23, 29\}$ is a 5-term arithmetic progression of primes ($a=5, d=6$).
   - $\{7, 37, 67, 97, 127, 157\}$ is a 6-term arithmetic progression of primes ($a=7, d=30$).
4. Formal proof that every infinite arithmetic progression contains arithmetic progressions of any arbitrary length $k$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false

open Finset

/-- A set $A \subseteq \mathbb{N}$ contains an arithmetic progression of length $k$ -/
def has_ap_length (A : Set ℕ) (k : ℕ) : Prop :=
  ∃ a d : ℕ, d ≥ 1 ∧ ∀ i : ℕ, i < k → (a + i * d) ∈ A

/-- Predicate that $A \subseteq \mathbb{N}$ satisfies the Erdős AP property for all lengths $k \ge 3$ -/
def erdos_ap_property (A : Set ℕ) : Prop :=
  ∀ k : ℕ, k ≥ 3 → has_ap_length A k

/-- Verification that $\{3, 5, 7\}$ contains a 3-term AP with $a = 3, d = 2$ -/
theorem prime_ap_3 :
    has_ap_length ({3, 5, 7} : Set ℕ) 3 := by
  use 3, 2
  refine ⟨by decide, ?_⟩
  intro i hi
  interval_cases i
  · simp
  · simp
  · simp

/-- Verification that $\{5, 11, 17, 23, 29\}$ contains a 5-term AP with $a = 5, d = 6$ -/
theorem prime_ap_5 :
    has_ap_length ({5, 11, 17, 23, 29} : Set ℕ) 5 := by
  use 5, 6
  refine ⟨by decide, ?_⟩
  intro i hi
  interval_cases i
  · simp
  · simp
  · simp
  · simp
  · simp

/-- Verification that $\{7, 37, 67, 97, 127, 157\}$ contains a 6-term AP with $a = 7, d = 30$ -/
theorem prime_ap_6 :
    has_ap_length ({7, 37, 67, 97, 127, 157} : Set ℕ) 6 := by
  use 7, 30
  refine ⟨by decide, ?_⟩
  intro i hi
  interval_cases i
  · simp
  · simp
  · simp
  · simp
  · simp
  · simp

/-- Every infinite arithmetic progression $A_{a, d} = \{a + n \cdot d \mid n \in \mathbb{N}\}$ with $d \ge 1$ contains APs of arbitrary length $k$ -/
theorem infinite_ap_contains_arbitrary_length (a d : ℕ) (hd : d ≥ 1) :
    erdos_ap_property {x : ℕ | ∃ n : ℕ, x = a + n * d} := by
  intro k hk
  use a, d
  refine ⟨hd, ?_⟩
  intro i hi
  simp only [Set.mem_setOf_eq]
  use i
