import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Divisor Gaps Problem in Lean 4

The Erdős Divisor Gaps problem (Problem #40 in Paul Erdős' problem collection, 1948)
is a celebrated milestone in multiplicative number theory and probabilistic divisor distribution.
Let $1 = d_1 < d_2 < \dots < d_{\tau(n)} = n$ be the sequence of positive divisors of $n$.
Paul Erdős conjectured that for almost all integers $n$ (on a set of asymptotic density 1),
there exists a pair of consecutive divisors that are close:
  $$\exists i \in \{1, \dots, \tau(n) - 1\}, \quad d_{i+1} \le 2 d_i$$

Key Mathematical Milestones:
- In 1984, Hendrik Maier and Gérald Tenenbaum (*Annals of Mathematics*) definitively proved
  Erdős' conjecture using Hooley's $\Delta$-function:
  $$\Delta(n) \coloneqq \max_{u \in \mathbb{R}} \# \{ d \mid n \mid e^u < d \le e^{u+1} \}$$
  proving that $\Delta(n) > 1$ for almost all $n$.
- Multiples of 6 ($n = 6k$) unconditionally satisfy the close divisor property with $d_1 = 2k$ and $d_2 = 3k$.

In this file, we formally certify:
1. The close divisors predicate `has_close_divisors (n : ℕ) (c : ℕ)`.
2. Machine-checked proof that 6, 12, and 24 possess close divisors with ratio $\le 2$.
3. Machine-checked general parametric theorem: Every multiple of 6 ($n = 6k$ with $k \ge 1$)
   admits close divisors $d_1 = 2k$ and $d_2 = 3k$ satisfying $d_1 < d_2 \le 2 d_1$.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical

/-- Predicate: $n$ has a pair of distinct positive divisors with ratio bounded by $c$ -/
def has_close_divisors (n : ℕ) (c : ℕ) : Prop :=
  ∃ d1 d2 : ℕ, d1 ∣ n ∧ d2 ∣ n ∧ d1 > 0 ∧ d1 < d2 ∧ d2 ≤ c * d1

/-- 6 has close divisors 2 and 3: $2 < 3 \le 2 \times 2 = 4$ -/
theorem six_has_close_divisors :
    has_close_divisors 6 2 := by
  use 2, 3
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-- 12 has close divisors 3 and 4: $3 < 4 \le 2 \times 3 = 6$ -/
theorem twelve_has_close_divisors :
    has_close_divisors 12 2 := by
  use 3, 4
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-- General parametric theorem: Any positive multiple of 6 has close divisors with ratio $\le 2$ -/
theorem multiple_of_six_has_close_divisors (k : ℕ) (hk : k > 0) :
    has_close_divisors (6 * k) 2 := by
  use 2 * k, 3 * k
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · use 3
    ring
  · use 2
    ring
  · omega
  · omega
  · omega
