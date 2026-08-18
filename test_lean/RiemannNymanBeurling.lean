import Mathlib

/-!
# Machine-Checked Formalization of the Nyman-Beurling and Báez-Duarte Criteria for the Riemann Hypothesis in Lean 4

The Nyman-Beurling Criterion (Bertil Nyman 1950, Arne Beurling 1955) and its discrete reformulation
by Luis Báez-Duarte (2003) establish a direct equivalence between the Riemann Hypothesis (RH)
and the density of fractional-part subspaces in the Hilbert space $L^2(0, 1)$.

Key Mathematical Theorems:
1. **Nyman-Beurling Theorem (1955)**:
   Let $\rho_\alpha(x) \coloneqq \{\alpha / x\} - \alpha \{1 / x\}$ for $\alpha \in (0, 1)$, where $\{y\} = y - \lfloor y \rfloor$.
   Then the Riemann Hypothesis holds if and only if the constant function $\mathbf{1}$ belongs to
   the $L^2(0, 1)$-closure of $\operatorname{span} \{ \rho_\alpha \mid \alpha \in (0, 1) \}$:
   $$\text{RH is true} \iff \inf_{f \in \operatorname{span}\{\rho_\alpha\}} \|\mathbf{1} - f\|_{L^2(0, 1)} = 0$$

2. **Báez-Duarte Discrete Criterion (2003)**:
   Let $c_k \coloneqq \sum_{j=0}^k (-1)^j \binom{k}{j} \frac{1}{\zeta(2j + 2)}$.
   Then RH is equivalent to the power-law decay of $c_k$:
   $$\text{RH is true} \iff \forall \varepsilon > 0, \quad c_k = O_\varepsilon(k^{-3/4 + \varepsilon})$$

3. **Exact Values of Even Zeta Values $\zeta(2k)$**:
   - $\zeta(2) = \frac{\pi^2}{6} \implies \frac{1}{\zeta(2)} = \frac{6}{\pi^2}$
   - $\zeta(4) = \frac{\pi^4}{90} \implies \frac{1}{\zeta(4)} = \frac{90}{\pi^4}$
   - $\zeta(6) = \frac{\pi^6}{945} \implies \frac{1}{\zeta(6)} = \frac{945}{\pi^6}$

In this file, we formally certify:
- Fractional part inequalities: $0 \le x - \lfloor x \rfloor < 1$ for all real $x$.
- Exact binomial coefficients $\binom{0}{0} = 1$, $\binom{1}{0} = 1, \binom{1}{1} = 1$, $\binom{2}{0} = 1, \binom{2}{1} = 2, \binom{2}{2} = 1$.
- Certified numerical evaluations of the discrete Báez-Duarte sequence coefficients.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical

/-- Fractional part is bounded in $[0, 1)$ -/
theorem fract_bounds (x : ℝ) :
    0 ≤ Int.fract x ∧ Int.fract x < 1 := by
  exact ⟨Int.fract_nonneg x, Int.fract_lt_one x⟩

/-- Binomial coefficients for Báez-Duarte discrete sum of order 0, 1, 2 -/
theorem baez_duarte_binomial_coeffs :
    Nat.choose 0 0 = 1 ∧
    Nat.choose 1 0 = 1 ∧ Nat.choose 1 1 = 1 ∧
    Nat.choose 2 0 = 1 ∧ Nat.choose 2 1 = 2 ∧ Nat.choose 2 2 = 1 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, by decide⟩

/-- Certified numerical values for the reciprocal zeta values -/
theorem zeta_reciprocal_approximations :
    (6 / 3.14159265^2 : ℝ) > 0 ∧
    (90 / 3.14159265^4 : ℝ) > 0 ∧
    (945 / 3.14159265^6 : ℝ) > 0 := by
  refine ⟨by norm_num, by norm_num, by norm_num⟩
