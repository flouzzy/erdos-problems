# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Nyman-Beurling and Báez-Duarte Criteria for the Riemann Hypothesis`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Riemann Hypothesis, Nyman-Beurling Criterion, Báez-Duarte Theorem, Hilbert Space L^2(0, 1), Fractional Part Functions, Even Zeta Values, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11M26, 46E20, 11M06, 68V20, 30H10`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Nyman-Beurling and Báez-Duarte Criteria for the Riemann Hypothesis: A Detailed Treatise on Hilbert Space Density, Fractional Part Approximations, Even Zeta Reciprocals, and Certified Proofs</strong></p>

<p>The Nyman-Beurling Criterion (Bertil Nyman, 1950; Arne Beurling, 1955) and its discrete reformulation by Luis Báez-Duarte (2003) establish a profound equivalence between the Riemann Hypothesis (RH) and density in the Hilbert space $L^2(0, 1)$. Let $\rho_\alpha(x) \coloneqq \{\alpha / x\} - \alpha \{1 / x\}$ for $\alpha \in (0, 1)$, where $\{y\} = y - \lfloor y \rfloor$ denotes the fractional part. The Nyman-Beurling Theorem asserts that RH holds if and only if the constant function $\mathbf{1}(x) \equiv 1$ lies in the $L^2(0, 1)$-closure of $\operatorname{span}\{\rho_\alpha \mid \alpha \in (0, 1)\}$. In 2003, Báez-Duarte established the discrete equivalent: $\text{RH is true} \iff c_k \coloneqq \sum_{j=0}^k (-1)^j \binom{k}{j} \frac{1}{\zeta(2j + 2)} = O_\varepsilon(k^{-3/4 + \varepsilon})$ for every $\varepsilon > 0$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Nyman-Beurling Density Theorem:</strong> Rigorous exposition of the Hilbert space density problem in $L^2(0, 1)$ approximating the constant function $\mathbf{1}$ by fractional-part linear combinations.</li>
  <li><strong>The Báez-Duarte Discrete Formulation (2003):</strong> Exact derivation linking RH to the power-law decay of binomial alternating sums over reciprocal even zeta values $1/\zeta(2j+2)$.</li>
  <li><strong>Explicit Euler Zeta Evaluations:</strong> Full calculation of $c_0 = 6/\pi^2$, $c_1 = 6/\pi^2 - 90/\pi^4$, and $c_2 = 6/\pi^2 - 180/\pi^4 + 945/\pi^6$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Fractional part bounds $0 \le \{x\} < 1$, exact binomial coefficient identities, and verified positivity of reciprocal zeta approximations are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/RiemannNymanBeurling.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11M26, 46E20, 11M06, 68V20, 30H10<br />
<strong>Keywords:</strong> Riemann Hypothesis, Nyman-Beurling Criterion, Báez-Duarte Theorem, Hilbert Space L^2(0, 1), Fractional Part Functions, Even Zeta Values, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Nyman-Beurling and Báez-Duarte Criteria for the Riemann Hypothesis: A Detailed Treatise on Hilbert Space Density, Fractional Part Approximations, Even Zeta Reciprocals, and Certified Proofs**

The Nyman-Beurling Criterion (Bertil Nyman, 1950; Arne Beurling, 1955) and its discrete reformulation by Luis Báez-Duarte (2003) establish a profound equivalence between the Riemann Hypothesis (RH) and density in the Hilbert space $L^2(0, 1)$.

### Key Mathematical Results & Contributions:
- **The Nyman-Beurling Density Theorem:** Equivalence between RH and density of fractional parts in $L^2(0, 1)$.
- **The Báez-Duarte Discrete Formulation (2003):** Power-law decay of $c_k = \sum (-1)^j \binom{k}{j} \frac{1}{\zeta(2j+2)}$.
- **Explicit Euler Zeta Evaluations:** Full calculation of $c_0, c_1, c_2$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/RiemannNymanBeurling.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/RiemannNymanBeurling.lean)).

* **MSC (2020)**: 11M26, 46E20, 11M06, 68V20, 30H10
* **Keywords**: Riemann Hypothesis, Nyman-Beurling Criterion, Báez-Duarte Theorem, Hilbert Space L^2(0, 1), Fractional Part Functions, Even Zeta Values, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
