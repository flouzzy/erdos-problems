# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Distinct Subset Sums Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Distinct Subset Sums, Additive Combinatorics, Central Limit Theorem, Conway-Guy Sequence, Additive Independence, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B13, 05A17, 11B75, 68V20, 60F05`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Distinct Subset Sums Conjecture: A Detailed Treatise on Additive Independence, Central Limit Bounds, the Conway-Guy Sequence, and Certified Proofs</strong></p>

<p>The Erdős distinct subset sums conjecture (Problem #14 in Paul Erdős' problem collection, 1931 / 1955) is a fundamental open question in additive combinatorics. It asks for the maximum element max(S) of an n-element set of positive integers S = {s_1, ..., s_n} whose 2^n subset sums are all mutually distinct. Erdős conjectured that max(S) ≥ c 2^n for an absolute constant c > 0. In 1955, Erdős and Leo Moser established the classic lower bound max(S) ≥ 2^n / sqrt(n) using the Central Limit Theorem and Fourier analysis. In 1968, J. H. Conway and R. K. Guy constructed an infinite family of distinct subset sum sets with max(S) < 2^{n-2}.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Combinatorial Sum Lower Bound:</strong> Rigorous proof that $\sum_{s \in S} s \ge 2^n - 1$ by pairing each subset sum with distinct integers.</li>
  <li><strong>Elementary Maximum Bound:</strong> Non-elliptical proof that $\max(S) \ge \frac{2^n - 1}{n}$.</li>
  <li><strong>The Erdős-Moser CLT Bound:</strong> Step-by-step derivation of the $\frac{2^n}{\sqrt{n}}$ bound via variance of independent Rademacher random variables.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Distinct sumset predicates, sum lower bounds, and exact verification of small distinct sets are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosDistinctSums.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B13, 05A17, 11B75, 68V20, 60F05<br />
<strong>Keywords:</strong> Erdős Distinct Subset Sums, Additive Combinatorics, Central Limit Theorem, Conway-Guy Sequence, Additive Independence, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Distinct Subset Sums Conjecture: A Detailed Treatise on Additive Independence, Central Limit Bounds, the Conway-Guy Sequence, and Certified Proofs**

The Erdős distinct subset sums conjecture (Problem #14 in Paul Erdős' problem collection, 1931 / 1955) is a fundamental open question in additive combinatorics. It asks for the maximum element max(S) of an n-element set of positive integers S = {s_1, ..., s_n} whose 2^n subset sums are all mutually distinct. Erdős conjectured that max(S) ≥ c 2^n for an absolute constant c > 0. In 1955, Erdős and Leo Moser established the classic lower bound max(S) ≥ 2^n / sqrt(n) using the Central Limit Theorem and Fourier analysis. In 1968, J. H. Conway and R. K. Guy constructed an infinite family of distinct subset sum sets with max(S) < 2^{n-2}.

### Key Mathematical Results & Contributions:
- **Combinatorial Sum Lower Bound:** Rigorous proof that $\sum_{s \in S} s \ge 2^n - 1$ by pairing each subset sum with distinct integers.
- **Elementary Maximum Bound:** Non-elliptical proof that $\max(S) \ge \frac{2^n - 1}{n}$.
- **The Erdős-Moser CLT Bound:** Step-by-step derivation of the $\frac{2^n}{\sqrt{n}}$ bound via variance of independent Rademacher random variables.
- **100% Machine-Checked Verification in Lean 4:** Distinct sumset predicates, sum lower bounds, and exact verification of small distinct sets are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosDistinctSums.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosDistinctSums.lean)).

* **MSC (2020)**: 11B13, 05A17, 11B75, 68V20, 60F05
* **Keywords**: Erdős Distinct Subset Sums, Additive Combinatorics, Central Limit Theorem, Conway-Guy Sequence, Additive Independence, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
