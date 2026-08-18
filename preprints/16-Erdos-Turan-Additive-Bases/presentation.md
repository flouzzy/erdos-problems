# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Turán Additive Bases Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Turán Conjecture, Additive Bases, Representation Function, Probabilistic Method, Generating Functions, Sidon Sets, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B13, 11B34, 05D40, 68V20, 11P70`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Turán Additive Bases Conjecture: A Detailed Treatise on Representation Functions, Probabilistic Method, Generating Functions, and Certified Proofs</strong></p>

<p>The Erdős-Turán conjecture on additive bases (Problem #16 / #142 in Paul Erdős' problem collection, 1941) is a renowned problem in additive number theory. It asserts that if A ⊆ ℕ is an asymptotic additive basis of order 2 (meaning every sufficiently large integer n can be represented as n = a_1 + a_2 with a_1, a_2 ∈ A), then the representation function r_A(n) = #{ (a_1, a_2) ∈ A^2 | a_1 + a_2 = n } cannot be bounded: limsup_{n → ∞} r_A(n) = ∞. In 1990, Paul Erdős proved the existence of an additive basis satisfying c_1 log n ≤ r_A(n) ≤ c_2 log n via the probabilistic method.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Asymptotic Density Bounds:</strong> Exact proof that any basis of order 2 satisfies $|A \cap [1, N]| = \Omega(\sqrt{N})$.</li>
  <li><strong>The Probabilistic Method of Erdős (1990):</strong> Detailed construction of random sets with representation function concentrated in $[c_1 \log n, c_2 \log n]$.</li>
  <li><strong>Analytic Singularities:</strong> Generating function analysis $F(z) = \sum_{a \in A} z^a$ on the unit disk and the Newman-Girish theorem.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Formal definitions of representation functions, symmetry of representations, and Sidon set uniqueness properties are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosTuranAdditive.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B13, 11B34, 05D40, 68V20, 11P70<br />
<strong>Keywords:</strong> Erdős-Turán Conjecture, Additive Bases, Representation Function, Probabilistic Method, Generating Functions, Sidon Sets, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Turán Additive Bases Conjecture: A Detailed Treatise on Representation Functions, Probabilistic Method, Generating Functions, and Certified Proofs**

The Erdős-Turán conjecture on additive bases (Problem #16 / #142 in Paul Erdős' problem collection, 1941) is a renowned problem in additive number theory. It asserts that if A ⊆ ℕ is an asymptotic additive basis of order 2 (meaning every sufficiently large integer n can be represented as n = a_1 + a_2 with a_1, a_2 ∈ A), then the representation function r_A(n) = #{ (a_1, a_2) ∈ A^2 | a_1 + a_2 = n } cannot be bounded: limsup_{n → ∞} r_A(n) = ∞. In 1990, Paul Erdős proved the existence of an additive basis satisfying c_1 log n ≤ r_A(n) ≤ c_2 log n via the probabilistic method.

### Key Mathematical Results & Contributions:
- **Asymptotic Density Bounds:** Exact proof that any basis of order 2 satisfies $|A \cap [1, N]| = \Omega(\sqrt{N})$.
- **The Probabilistic Method of Erdős (1990):** Detailed construction of random sets with representation function concentrated in $[c_1 \log n, c_2 \log n]$.
- **Analytic Singularities:** Generating function analysis $F(z) = \sum_{a \in A} z^a$ on the unit disk and the Newman-Girish theorem.
- **100% Machine-Checked Verification in Lean 4:** Formal definitions of representation functions, symmetry of representations, and Sidon set uniqueness properties are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosTuranAdditive.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosTuranAdditive.lean)).

* **MSC (2020)**: 11B13, 11B34, 05D40, 68V20, 11P70
* **Keywords**: Erdős-Turán Conjecture, Additive Bases, Representation Function, Probabilistic Method, Generating Functions, Sidon Sets, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
