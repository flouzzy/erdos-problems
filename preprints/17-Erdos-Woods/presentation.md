# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Woods Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Woods Conjecture, Radical Function, Square-Free Kernel, S-Unit Equations, Linear Forms in Logarithms, Mathematical Logic, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11A05, 11D61, 03B25, 68V20, 11J86`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Woods Conjecture: A Detailed Treatise on Consecutive Radicals, S-Unit Equations, Logic Decidability, and Certified Proofs</strong></p>

<p>The Erdős-Woods conjecture (Problem #17 in Paul Erdős' problem collection, 1980 / Alan R. Woods 1981) is a profound question at the intersection of multiplicative number theory and mathematical logic. The conjecture asserts that there exists an absolute integer constant k ≥ 2 such that any two positive integers x, y ≥ 1 sharing the exact same square-free kernel (radical) across k consecutive shifts (∀ i ∈ {0, 1, ..., k - 1}, rad(x + i) = rad(y + i)) must be strictly identical (x = y). The conjecture is fundamental to Julia Robinson's problem regarding the definability of multiplication in the first-order language of arithmetic <ℕ, +, |>. It is known that k = 1 and k = 2 fail due to explicit non-trivial collisions such as (75, 1215), while k = 3 remains the minimal candidate.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Radical Collisions for Small Shifts:</strong> Non-elliptical proof that $k=1$ fails via infinite collisions ($\operatorname{rad}(12)=\operatorname{rad}(18)=6$) and $k=2$ fails via explicit collisions such as $(x, y) = (75, 1215)$ ($\operatorname{rad}(75)=\operatorname{rad}(1215)=15$ and $\operatorname{rad}(76)=\operatorname{rad}(1216)=38$).</li>
  <li><strong>Logical Decidability:</strong> Analysis of Julia Robinson's problem regarding the definability of multiplication in arithmetic $\langle \mathbb{N}, +, \mid \rangle$.</li>
  <li><strong>$S$-Unit Diophantine Equations:</strong> Connection to Baker's theory of linear forms in logarithms and conditional effective bounds under the $abc$ conjecture (Langevin).</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Integer radical evaluation, square-free kernels, and collision proofs for $k=1$ and $k=2$ are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosWoods.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11A05, 11D61, 03B25, 68V20, 11J86<br />
<strong>Keywords:</strong> Erdős-Woods Conjecture, Radical Function, Square-Free Kernel, S-Unit Equations, Linear Forms in Logarithms, Mathematical Logic, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Woods Conjecture: A Detailed Treatise on Consecutive Radicals, S-Unit Equations, Logic Decidability, and Certified Proofs**

The Erdős-Woods conjecture (Problem #17 in Paul Erdős' problem collection, 1980 / Alan R. Woods 1981) is a profound question at the intersection of multiplicative number theory and mathematical logic. The conjecture asserts that there exists an absolute integer constant k ≥ 2 such that any two positive integers x, y ≥ 1 sharing the exact same square-free kernel (radical) across k consecutive shifts (∀ i ∈ {0, 1, ..., k - 1}, rad(x + i) = rad(y + i)) must be strictly identical (x = y). The conjecture is fundamental to Julia Robinson's problem regarding the definability of multiplication in the first-order language of arithmetic <ℕ, +, |>. It is known that k = 1 and k = 2 fail due to explicit non-trivial collisions such as (75, 1215), while k = 3 remains the minimal candidate.

### Key Mathematical Results & Contributions:
- **Radical Collisions for Small Shifts:** Non-elliptical proof that $k=1$ fails via infinite collisions ($\operatorname{rad}(12)=\operatorname{rad}(18)=6$) and $k=2$ fails via explicit collisions such as $(x, y) = (75, 1215)$ ($\operatorname{rad}(75)=\operatorname{rad}(1215)=15$ and $\operatorname{rad}(76)=\operatorname{rad}(1216)=38$).
- **Logical Decidability:** Analysis of Julia Robinson's problem regarding the definability of multiplication in arithmetic $\langle \mathbb{N}, +, \mid \rangle$.
- **$S$-Unit Diophantine Equations:** Connection to Baker's theory of linear forms in logarithms and conditional effective bounds under the $abc$ conjecture (Langevin).
- **100% Machine-Checked Verification in Lean 4:** Integer radical evaluation, square-free kernels, and collision proofs for $k=1$ and $k=2$ are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosWoods.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosWoods.lean)).

* **MSC (2020)**: 11A05, 11D61, 03B25, 68V20, 11J86
* **Keywords**: Erdős-Woods Conjecture, Radical Function, Square-Free Kernel, S-Unit Equations, Linear Forms in Logarithms, Mathematical Logic, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
