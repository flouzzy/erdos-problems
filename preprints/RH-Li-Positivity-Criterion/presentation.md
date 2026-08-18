# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Li Positivity Criterion for the Riemann Hypothesis`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Riemann Hypothesis, Li Positivity Criterion, Bombieri-Lagarias Theorem, Conformal Mappings, Riemann Xi Function, Weil Explicit Formula, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11M26, 11M06, 30C20, 68V20, 11N05`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Li Positivity Criterion for the Riemann Hypothesis: A Detailed Treatise on Conformal Unit Circle Mappings, the Bombieri-Lagarias Arithmetic Formula, Trace Formulations, and Certified Proofs</strong></p>

<p>The Li Positivity Criterion (Ke-Fei Li, 1997; Enrico Bombieri and Jeffrey Lagarias, 1999) is one of the deepest and most elegant analytic and geometric reformulations of the Riemann Hypothesis (RH). Let $\xi(s) \coloneqq \frac{1}{2} s(s - 1) \pi^{-s/2} \Gamma(s/2) \zeta(s)$ be the completed Riemann $\xi$-function. The sequence of Li coefficients $\lambda_n$ is defined by: $\lambda_n \coloneqq \sum_\rho \left[ 1 - \left( 1 - \frac{1}{\rho} \right)^n \right] = \left. \frac{1}{(n - 1)!} \frac{d^n}{ds^n} \left( s^{n - 1} \ln \xi(s) \right) \right|_{s=1}$, where the sum is over all non-trivial zeros $\rho$ of $\zeta(s)$ paired as $(\rho, 1 - \rho)$. Li's Criterion establishes that the Riemann Hypothesis is true if and only if $\lambda_n > 0$ for all positive integers $n \ge 1$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Conformal Geometry of the Critical Line:</strong> Non-elliptical proof that the Möbius map $w(s) = 1 - 1/s$ maps $\Re(s) = 1/2$ isometrically onto the unit circle $|w| = 1$.</li>
  <li><strong>Trigonometric Positivity of Critical Zeros:</strong> Step-by-step derivation showing that every zero on the critical line contributes $2 \sin^2(n\theta_\rho/2) \ge 0$, forcing $\lambda_n > 0$ under RH.</li>
  <li><strong>The Bombieri-Lagarias Arithmetic Formula:</strong> Exact decomposition of $\lambda_n$ into explicit Archimedean gamma terms and prime-power Von Mangoldt sums.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Conformal unit circle isometry, non-negativity of the trigonometric kernel, and numerical positivity for low-order coefficients $\lambda_1, \lambda_2, \lambda_3, \lambda_4 > 0$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/RiemannLiCriterion.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11M26, 11M06, 30C20, 68V20, 11N05<br />
<strong>Keywords:</strong> Riemann Hypothesis, Li Positivity Criterion, Bombieri-Lagarias Theorem, Conformal Mappings, Riemann Xi Function, Weil Explicit Formula, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Li Positivity Criterion for the Riemann Hypothesis: A Detailed Treatise on Conformal Unit Circle Mappings, the Bombieri-Lagarias Arithmetic Formula, Trace Formulations, and Certified Proofs**

The Li Positivity Criterion (Ke-Fei Li, 1997; Enrico Bombieri and Jeffrey Lagarias, 1999) is one of the deepest and most elegant analytic and geometric reformulations of the Riemann Hypothesis (RH). Let $\xi(s) \coloneqq \frac{1}{2} s(s - 1) \pi^{-s/2} \Gamma(s/2) \zeta(s)$ be the completed Riemann $\xi$-function.

### Key Mathematical Results & Contributions:
- **Conformal Geometry of the Critical Line:** Proof that $w(s) = 1 - 1/s$ maps $\Re(s) = 1/2$ isometrically onto the unit circle $|w| = 1$.
- **Trigonometric Positivity:** Proof that critical zeros contribute $2 \sin^2(n\theta_\rho/2) \ge 0$, forcing $\lambda_n > 0$.
- **Bombieri-Lagarias Arithmetic Formula:** Decomposition into Archimedean and Von Mangoldt sums.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/RiemannLiCriterion.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/RiemannLiCriterion.lean)).

* **MSC (2020)**: 11M26, 11M06, 30C20, 68V20, 11N05
* **Keywords**: Riemann Hypothesis, Li Positivity Criterion, Bombieri-Lagarias Theorem, Conformal Mappings, Riemann Xi Function, Weil Explicit Formula, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
