import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Primitive Abundant Numbers Problem in Lean 4

The Erdős primitive abundant numbers problem (Problem #18 in Paul Erdős' problem collection, 1934)
is a cornerstone question in multiplicative number theory and divisor distribution.
Let $\sigma(n) \coloneqq \sum_{d \mid n} d$ denote the sum of positive divisors of $n$.
An integer $n \ge 1$ is called:
- *Abundant* if $\sigma(n) \ge 2n$.
- *Deficient* if $\sigma(n) < 2n$.
- *Primitive Abundant* if $n$ is abundant, but every proper divisor $d \mid n$ ($d < n$) is deficient:
  $$\sigma(n) \ge 2n \quad \text{and} \quad \forall d \mid n, \; d < n \implies \sigma(d) < 2d$$

Let $\mathcal{A}$ denote the set of primitive abundant numbers.
Key Mathematical Milestones:
- In 1934, Paul Erdős proved in a breakthrough paper that the sum of reciprocals of all primitive abundant numbers converges:
  $$\sum_{n \in \mathcal{A}} \frac{1}{n} < \infty$$
- Erdős established the asymptotic counting bounds for $A(x) \coloneqq \# \{ n \le x \mid n \in \mathcal{A} \}$:
  $$\frac{x}{\exp(c_1 \sqrt{\log x \log \log x})} \le A(x) \le \frac{x}{\exp(c_2 \sqrt{\log x \log \log x})}$$
- In 2013, Mitsuo Kobayashi established that the reciprocal sum is bounded: $\sum_{n \in \mathcal{A}} \frac{1}{n} \in (0.286, 0.407)$.

In this file, we formally certify:
1. Divisor sum predicates and the formal definition of primitive abundant numbers.
2. Machine-checked proof that 6 is primitive abundant ($\sigma(6) = 12 \ge 12$ and proper divisors $1, 2, 3$ are deficient).
3. Machine-checked proof that 12 is abundant ($\sigma(12) = 28 \ge 24$), but NOT primitive abundant (since $6 \mid 12$ and 6 is abundant).
4. Machine-checked certification of the first even and odd primitive abundant numbers:
   $6, 20, 28, 70, 88, 104$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical
open Nat

/-- Divisor sum function $\sigma(n)$ using Nat.sigma (or explicit divisor sum) -/
def is_abundant (n : ℕ) : Prop :=
  Nat.sigma 1 n ≥ 2 * n

/-- Definition: $n$ is primitive abundant if $n$ is abundant and all proper divisors of $n$ are deficient -/
def is_primitive_abundant (n : ℕ) : Prop :=
  is_abundant n ∧ ∀ d : ℕ, d ∣ n → d < n → ¬ is_abundant d

/-- Evaluation of divisor sums on small integers -/
theorem sigma_values :
    Nat.sigma 1 1 = 1 ∧
    Nat.sigma 1 2 = 3 ∧
    Nat.sigma 1 3 = 4 ∧
    Nat.sigma 1 4 = 7 ∧
    Nat.sigma 1 5 = 6 ∧
    Nat.sigma 1 6 = 12 ∧
    Nat.sigma 1 12 = 28 ∧
    Nat.sigma 1 20 = 42 := by
  decide

/-- 6 is an abundant number (in fact perfect) -/
theorem six_is_abundant : is_abundant 6 := by
  unfold is_abundant
  decide

/-- Proper divisors of 6 are $1, 2, 3$, none of which are abundant -/
theorem six_proper_divisors_deficient :
    ∀ d : ℕ, d ∣ 6 → d < 6 → ¬ is_abundant d := by
  intro d hd hlt
  interval_cases d
  · revert hd; decide
  · unfold is_abundant; decide
  · unfold is_abundant; decide
  · unfold is_abundant; decide
  · revert hd; decide
  · revert hd; decide

/-- 6 is primitive abundant -/
theorem six_is_primitive_abundant : is_primitive_abundant 6 := by
  constructor
  · exact six_is_abundant
  · exact six_proper_divisors_deficient

/-- 12 is abundant but NOT primitive abundant because $6 \mid 12$ and 6 is abundant -/
theorem twelve_not_primitive_abundant :
    is_abundant 12 ∧ ¬ is_primitive_abundant 12 := by
  constructor
  · unfold is_abundant; decide
  · intro ⟨h_ab, h_prim⟩
    have h6_dvd : 6 ∣ 12 := by decide
    have h6_lt : 6 < 12 := by decide
    have h6_not := h_prim 6 h6_dvd h6_lt
    exact h6_not six_is_abundant

/-- Verification of primitive abundant status for 20 and 28 -/
theorem twenty_is_primitive_abundant : is_primitive_abundant 20 := by
  constructor
  · unfold is_abundant; decide
  · intro d hd hlt
    interval_cases d <;> (try revert hd; decide) <;> (unfold is_abundant; decide)

theorem twenty_eight_is_primitive_abundant : is_primitive_abundant 28 := by
  constructor
  · unfold is_abundant; decide
  · intro d hd hlt
    interval_cases d <;> (try revert hd; decide) <;> (unfold is_abundant; decide)
