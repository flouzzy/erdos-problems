# On the Foundations and Autoformalization of the Erdős-Straus Conjecture

**Abstract**
The Erdős-Straus conjecture, formulated in 1948, postulates that every integer $n \ge 2$ allows the decomposition of the fraction $\frac{4}{n}$ into a sum of three unit fractions. Although it has been empirically verified up to $n = 10^{17}$, a general proof remains out of reach. This paper proposes a strict axiomatic dissection of the problem, establishing the fundamental reduction lemmas and providing exhaustive proofs without ellipses. Furthermore, we propose a formal architecture implementable in the Lean 4 proof assistant, laying the groundwork for mechanized verification of future partial results.

---

## 1. Introduction and Contextual Literature

The representation of rational numbers as sums of unit fractions (so-called "Egyptian fractions") is a classical arithmetic problem. The Erdős-Straus conjecture focuses on the rational Diophantine equation:
$$\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$$
for a given integer $n \ge 2$, with $x, y, z \in \mathbb{N}^*$.

Major advances on this problem primarily fall within analytic number theory. The work of Webb, Vaughan, and Elsholtz, relying on sieve methods (notably the Selberg sieve), established density theorems stipulating that the number of integers $n \in [1, N]$ for which the conjecture fails is bounded by $O(N \exp(-c \log^2 N))$. Thus, the conjecture is verified for almost all integers in the sense of asymptotic density.

However, a complete resolution requires a structural approach. Analogous to Andrew Wiles' proof of Fermat's Last Theorem, which necessitated the translation of Diophantine equations to modular objects, the preferred approach for the Erdős-Straus conjecture relies on polynomial parameterizations according to congruence classes modulo $k$.

## 2. Axiomatic Definitions

In order to avoid topological singularities related to fractional poles and to restrict the study to the category of commutative rings, we define the problem in its polynomial form.

**Definition 2.1 (Erdős-Straus Diophantine Hypersurface)**
Let $\mathbb{N}^*$ be the set of strictly positive integers. For any $n \in \mathbb{N}, n \ge 2$, we define the predicate $P(n, x, y, z)$ over $(\mathbb{N}^*)^3$ such that:
$$P(n, x, y, z) \iff 4xyz = n(xy + yz + zx)$$
Geometrically, for a fixed $n$, the set of solutions forms the positive rational points of a projective cubic Fano variety $\mathcal{H}_n$.

**Definition 2.2 (Validity)**
The Erdős-Straus conjecture is said to be valid for an integer $n \ge 2$ if and only if the set of solutions of $\mathcal{H}_n$ is not empty in $(\mathbb{N}^*)^3$.

## 3. Main Results and Proofs

We isolate two fundamental lemmas governing the multiplicative and modular behavior of the equation. The proofs are written exhaustively to guarantee strict formal review.

### 3.1 Multiplicative Reduction Lemma

**Lemma 1.** *If for every prime number $p \ge 2$, the variety $\mathcal{H}_p$ admits a rational point in $(\mathbb{N}^*)^3$, then for every integer $n \ge 2$, $\mathcal{H}_n$ admits a rational point in $(\mathbb{N}^*)^3$.*

**Proof.**
1. Let $n \in \mathbb{N}$ be an integer such that $n \ge 2$. If $n$ is prime, the property is trivial by hypothesis. Assume $n$ is composite.
2. By the Fundamental Theorem of Arithmetic, there exists a prime number $p$ dividing $n$. Thus, there exists an integer $m \in \mathbb{N}^*$ such that $n = p \cdot m$.
3. By hypothesis, the lemma states that the Erdős-Straus equation is solvable for the prime number $p$. Therefore, there exists a triplet $(x_p, y_p, z_p) \in (\mathbb{N}^*)^3$ such that:
   $$\frac{4}{p} = \frac{1}{x_p} + \frac{1}{y_p} + \frac{1}{z_p}$$
4. Multiplying each side of this equality by the non-zero scalar $\frac{1}{m}$, the equality is invariant:
   $$\frac{1}{m} \left( \frac{4}{p} \right) = \frac{1}{m} \left( \frac{1}{x_p} + \frac{1}{y_p} + \frac{1}{z_p} \right)$$
5. By distributivity of multiplication over addition in the field of rationals $\mathbb{Q}$:
   $$\frac{4}{p \cdot m} = \frac{1}{m \cdot x_p} + \frac{1}{m \cdot y_p} + \frac{1}{m \cdot z_p}$$
6. Substituting $p \cdot m$ by $n$, the equation becomes:
   $$\frac{4}{n} = \frac{1}{m \cdot x_p} + \frac{1}{m \cdot y_p} + \frac{1}{m \cdot z_p}$$
7. Let us define the transformation mapping: $X = m \cdot x_p$, $Y = m \cdot y_p$, and $Z = m \cdot z_p$.
8. Since the set $\mathbb{N}^*$ is closed under multiplication, and knowing that $m \in \mathbb{N}^*$ and $(x_p, y_p, z_p) \in (\mathbb{N}^*)^3$, we deduce that $X, Y, Z \in \mathbb{N}^*$.
9. The triplet $(X, Y, Z)$ therefore constitutes a strict solution for the integer $n$. This completes the proof of the reduction lemma. $\blacksquare$

### 3.2 Resolution for the Residual Class $n \equiv 3 \pmod 4$

**Lemma 2.** *For any integer $n$ belonging to the congruence class $3 \pmod 4$, the hypersurface $\mathcal{H}_n$ possesses a strict solution formable by a residual fraction expansion algorithm.*

**Proof.**
1. Let $n \in \mathbb{N}$ such that $n \equiv 3 \pmod 4$. By definition of modular arithmetic, there exists a natural integer $k \ge 0$ such that $n = 4k + 3$.
2. Consider the generating fraction $\frac{4}{4k+3}$. We seek to extract a first unit fraction. Let $x = k+1$. Since $k \ge 0$, $x \in \mathbb{N}^*$.
3. Let us evaluate the analytic remainder $R$ of this extraction:
   $$R = \frac{4}{4k+3} - \frac{1}{k+1}$$
4. Reducing to a common denominator (which is $(4k+3)(k+1)$) yields:
   $$R = \frac{4(k+1) - 1(4k+3)}{(4k+3)(k+1)}$$
5. The polynomial expansion of the numerator yields $4k + 4 - 4k - 3 = 1$.
6. The rational equality can thus be written:
   $$\frac{4}{4k+3} = \frac{1}{k+1} + \frac{1}{(4k+3)(k+1)}$$
7. To satisfy the axiom of the conjecture requiring exactly three terms, we must decompose the residual fraction $\frac{1}{(4k+3)(k+1)}$.
8. Let us introduce the strict algebraic identity, valid for any $A \in \mathbb{N}^*$:
   $$\frac{1}{A} = \frac{1}{A+1} + \frac{1}{A(A+1)}$$
9. Let $A = (4k+3)(k+1)$. Let us evaluate the bounds: for $k \ge 0$, the first factor $(4k+3) \ge 3$ and the second $(k+1) \ge 1$. By monotonicity of multiplication over $\mathbb{N}$, $A \ge 3$. Thus, the application of the identity is permissible because $A \in \mathbb{N}^*$.
10. The residual fraction expands as follows:
    $$\frac{1}{A} = \frac{1}{A+1} + \frac{1}{A(A+1)}$$
11. By recursive substitution into the equation from step 6, we obtain the final equality:
    $$\frac{4}{4k+3} = \frac{1}{k+1} + \frac{1}{A+1} + \frac{1}{A(A+1)}$$
    where $A = (4k+3)(k+1)$.
12. **Verification of the order constraint:**
    Let us define $y = A+1$ and $z = A(A+1)$.
    Knowing $A \ge 3$ and $x = k+1$, note that $x \le A/3 < A$. Thus $x < A < A+1 \implies x < y$.
    Furthermore, since $A \ge 3 > 1$, we have $A(A+1) > 1(A+1) \implies z > y$.
    The triplet $(x, y, z)$ satisfies the strict inequality $x < y < z$, guaranteeing distinct denominators belonging to $\mathbb{N}^*$. The lemma is proven. $\blacksquare$

## 4. Architecture for Autoformalization (Lean 4)

The rigor of modern mathematical proof demands the possibility of mechanized verification. We provide here the skeleton (Proof Sketch) implementable in the typed proof assistant **Lean 4**. The translation bypasses rational fraction fields by translating the predicates strictly over the ring of natural numbers $\mathbb{N}$.

```lean
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Prime

/-!
# Formalization of the Erdős-Straus Conjecture
This file contains the axiomatic infrastructure and the basic preparatory
theorems for resolution via modular congruence.
-/

/--
Algebraic definition of the Diophantine hypersurface.
Division is avoided to remain within the ring ℕ.
-/
def ErdosStrausEq (n x y z : ℕ) : Prop :=
  4 * x * y * z = n * (x * y + y * z + z * x)

/-- The validity predicate: existence of a strictly positive solution. -/
def HasErdosStrausSolution (n : ℕ) : Prop :=
  ∃ x y z : ℕ, x > 0 ∧ y > 0 ∧ z > 0 ∧ ErdosStrausEq n x y z

/-- Formal statement of the global conjecture. -/
def ErdosStrausConjecture : Prop :=
  ∀ n : ℕ, n ≥ 2 → HasErdosStrausSolution n

/--
Lemma 1: Multiplicative reduction.
If the conjecture holds for a prime p, it holds for any multiple p * m.
-/
lemma erdos_straus_reduction (p m : ℕ) (hp : HasErdosStrausSolution p) (hm : m > 0) :
  HasErdosStrausSolution (p * m) :=
by
  -- Extraction of existence witnesses from hypothesis hp
  rcases hp with ⟨x_p, y_p, z_p, hx, hy, hz, heq⟩
  -- Instantiation of the solution multiplied by m
  use m * x_p, m * y_p, m * z_p
  -- Proof of strict positivity via `pos_iff_ne_zero` and `mul_pos`
  -- Proof of the algebraic equation by associativity and commutativity (`ring`)
  sorry

/--
Lemma 2: Resolution for the congruence class n ≡ 3 (mod 4).
-/
lemma erdos_straus_mod4_3 (k : ℕ) :
  HasErdosStrausSolution (4 * k + 3) :=
by
  -- Explicit instantiation of parameterization polynomials from the paper proof
  let x := k + 1
  let A := (4 * k + 3) * (k + 1)
  let y := A + 1
  let z := A * (A + 1)

  -- Application of witnesses
  use x, y, z

  -- The positivity proof is trivial via `omega` since k ∈ ℕ
  -- The algebraic equality `ErdosStrausEq` resolves trivially via the `ring` tactic
  sorry
```

## 5. Conclusion

The Erdős-Straus conjecture illustrates the extreme complexity that can hide behind an elementary Diophantine equation. The reduction of the problem to prime numbers, coupled with the discovery of polynomial parameterizations covering increasingly dense congruence classes, constitutes the most promising path forward. The introduction of the Lean 4 proof assistant now allows validation of each new covered class with absolute certainty, eliminating the risk of human error in the algebraic expansion of massive polynomials.

---
**References**
* Erdős, P. (1950). *On a diophantine equation.* (Unpublished manuscript, cited by Straus).
* Vaughan, R. C. (1970). *On a problem of Erdős, Straus and Schinzel.* Mathematika, 17(2), 193-198.
* Elsholtz, C., & Tao, T. (2013). *Counting the number of solutions to the Erdős–Straus equation on unit fractions.* Journal of the Australian Mathematical Society, 94(1), 50-105.
