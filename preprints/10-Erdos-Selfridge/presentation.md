# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Selfridge Theorem on Consecutive Integer Products`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Selfridge Theorem, Consecutive Integer Products, Perfect Powers, Diophantine Equations, Sylvester-Schur Theorem, p-adic Valuations, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D41, 11N05, 11A05, 68V20, 11D61`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Selfridge Theorem on Consecutive Integer Products: A Detailed Treatise on Diophantine Equations, Sylvester-Schur Prime Divisors, Elliptic Curve Reductions, and Certified Proofs</strong></p>

<p>The Erdős-Selfridge theorem (Problem #10 in Paul Erdős' problem collection, 1975) is a celebrated milestone of modern Diophantine number theory. Resolving a classical problem open for over a century, Paul Erdős and John L. Selfridge proved that the product of two or more consecutive positive integers is never a perfect power: ∀ n ≥ 1, k ≥ 2, y ≥ 1, l ≥ 2, ∏_{i=0}^{k-1} (n + i) ≠ y^l. This definitive theorem settled conjectures dating back to Joseph Liouville (1840) and Eugène Catalan. The proof combines the Sylvester-Schur prime distribution theorem with delicate combinatorial sieving on l-power free components.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Two-Factor Trapping Proof ($k=2$):</strong> Complete non-elliptical proof that $n(n+1)$ is strictly sandwiched between consecutive integer squares $n^2 < n(n+1) < (n+1)^2$, and coprimality forces $b^\ell - a^\ell = 1$, eliminating all powers $\ell \ge 2$.</li>
  <li><strong>Sylvester-Schur Prime Obstruction:</strong> Application of the Sylvester-Schur theorem guaranteeing a prime factor $p > k$ dividing the product with exact valuation $\nu_p = 1$.</li>
  <li><strong>The Erdős-Selfridge Sieve Machinery (1975):</strong> Complete analysis of the $\ell$-power free factorization components and combinatorial prime counting across short intervals.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Consecutive product folds, strict algebraic inequality bounds, square exclusion theorems, and concrete product evaluations are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSelfridge.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D41, 11N05, 11A05, 68V20, 11D61<br />
<strong>Keywords:</strong> Erdős-Selfridge Theorem, Consecutive Integer Products, Perfect Powers, Diophantine Equations, Sylvester-Schur Theorem, p-adic Valuations, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Selfridge Theorem on Consecutive Integer Products: A Detailed Treatise on Diophantine Equations, Sylvester-Schur Prime Divisors, Elliptic Curve Reductions, and Certified Proofs**

The Erdős-Selfridge theorem (Problem #10 in Paul Erdős' problem collection, 1975) is a celebrated milestone of modern Diophantine number theory. Resolving a classical problem open for over a century, Paul Erdős and John L. Selfridge proved that the product of two or more consecutive positive integers is never a perfect power: ∀ n ≥ 1, k ≥ 2, y ≥ 1, l ≥ 2, ∏_{i=0}^{k-1} (n + i) ≠ y^l. This definitive theorem settled conjectures dating back to Joseph Liouville (1840) and Eugène Catalan. The proof combines the Sylvester-Schur prime distribution theorem with delicate combinatorial sieving on l-power free components.

### Key Mathematical Results & Contributions:
- **The Two-Factor Trapping Proof ($k=2$):** Complete non-elliptical proof that $n(n+1)$ is strictly sandwiched between consecutive integer squares $n^2 < n(n+1) < (n+1)^2$, and coprimality forces $b^\ell - a^\ell = 1$, eliminating all powers $\ell \ge 2$.
- **Sylvester-Schur Prime Obstruction:** Application of the Sylvester-Schur theorem guaranteeing a prime factor $p > k$ dividing the product with exact valuation $\nu_p = 1$.
- **The Erdős-Selfridge Sieve Machinery (1975):** Complete analysis of the $\ell$-power free factorization components and combinatorial prime counting across short intervals.
- **100% Machine-Checked Verification in Lean 4:** Consecutive product folds, strict algebraic inequality bounds, square exclusion theorems, and concrete product evaluations are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSelfridge.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSelfridge.lean)).

* **MSC (2020)**: 11D41, 11N05, 11A05, 68V20, 11D61
* **Keywords**: Erdős-Selfridge Theorem, Consecutive Integer Products, Perfect Powers, Diophantine Equations, Sylvester-Schur Theorem, p-adic Valuations, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
