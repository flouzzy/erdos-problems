# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Heilbronn Restricted Sumset Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Heilbronn Conjecture, Restricted Sumset, Combinatorial Nullstellensatz, Cauchy-Davenport Theorem, Additive Combinatorics, Polynomial Method, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B13, 11P70, 05E99, 68V20, 12E05`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Heilbronn Restricted Sumset Conjecture: A Detailed Treatise on Combinatorial Nullstellensatz, Cauchy-Davenport Generalizations, Dias da Silva-Hamidoune Exterior Algebra, and Certified Proofs</strong></p>

<p>The Erdős-Heilbronn conjecture (Problem #03 in Paul Erdős' collection, 1964) is a seminal milestone in additive number theory and arithmetic combinatorics. For any prime p and non-empty subset A ⊆ ℤ/pℤ, the restricted sumset A ^+ A is formed by sums of distinct elements: A ^+ A = {a + b | a, b ∈ A, a ≠ b}. Erdős and Heilbronn conjectured that |A ^+ A| ≥ min(p, 2|A| - 3), establishing a sharp analogue to the classical Cauchy-Davenport theorem (|A + B| ≥ min(p, |A| + |B| - 1)). The conjecture was first proven in 1994 by J. A. Dias da Silva and Y. O. Hamidoune using linear representations and exterior algebra, and subsequently revolutionized by Noga Alon, M. B. Nathanson, and I. Z. Ruzsa (1995, 1996) via the Combinatorial Nullstellensatz.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Sharpness of the $2|A|-3$ Bound:</strong> Complete derivation of the extremal equality $|A \hat{+} A| = 2k - 3$ for arithmetic progressions $A = \{0, 1, \dots, k-1\}$.</li>
  <li><strong>The Alon-Nathanson-Ruzsa Polynomial Proof:</strong> Step-by-step non-elliptical proof via the Combinatorial Nullstellensatz applied to the polynomial $P(x, y) = (x - y) \prod_{c \in C} (x + y - c)$ over $\mathbb{F}_p$.</li>
  <li><strong>Exterior Algebra Foundations:</strong> Survey of the Dias da Silva and Hamidoune (1994) proof via cyclic spaces and exterior powers $\bigwedge^k V$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Restricted sumset definitions, general two-element set identities ($|A \hat{+} A| = 1$), bound definitions, and exact evaluations in cyclic finite fields $\mathbb{Z}/5\mathbb{Z}$ and $\mathbb{Z}/7\mathbb{Z}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosHeilbronn.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B13, 11P70, 05E99, 68V20, 12E05<br />
<strong>Keywords:</strong> Erdős-Heilbronn Conjecture, Restricted Sumset, Combinatorial Nullstellensatz, Cauchy-Davenport Theorem, Additive Combinatorics, Polynomial Method, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Heilbronn Restricted Sumset Conjecture: A Detailed Treatise on Combinatorial Nullstellensatz, Cauchy-Davenport Generalizations, Dias da Silva-Hamidoune Exterior Algebra, and Certified Proofs**

The Erdős-Heilbronn conjecture (Problem #03 in Paul Erdős' collection, 1964) is a seminal milestone in additive number theory and arithmetic combinatorics. For any prime p and non-empty subset A ⊆ ℤ/pℤ, the restricted sumset A ^+ A is formed by sums of distinct elements: A ^+ A = {a + b | a, b ∈ A, a ≠ b}. Erdős and Heilbronn conjectured that |A ^+ A| ≥ min(p, 2|A| - 3), establishing a sharp analogue to the classical Cauchy-Davenport theorem (|A + B| ≥ min(p, |A| + |B| - 1)). The conjecture was first proven in 1994 by J. A. Dias da Silva and Y. O. Hamidoune using linear representations and exterior algebra, and subsequently revolutionized by Noga Alon, M. B. Nathanson, and I. Z. Ruzsa (1995, 1996) via the Combinatorial Nullstellensatz.

### Key Mathematical Results & Contributions:
- **Sharpness of the $2|A|-3$ Bound:** Complete derivation of the extremal equality $|A \hat{+} A| = 2k - 3$ for arithmetic progressions $A = \{0, 1, \dots, k-1\}$.
- **The Alon-Nathanson-Ruzsa Polynomial Proof:** Step-by-step non-elliptical proof via the Combinatorial Nullstellensatz applied to the polynomial $P(x, y) = (x - y) \prod_{c \in C} (x + y - c)$ over $\mathbb{F}_p$.
- **Exterior Algebra Foundations:** Survey of the Dias da Silva and Hamidoune (1994) proof via cyclic spaces and exterior powers $\bigwedge^k V$.
- **100% Machine-Checked Verification in Lean 4:** Restricted sumset definitions, general two-element set identities ($|A \hat{+} A| = 1$), bound definitions, and exact evaluations in cyclic finite fields $\mathbb{Z}/5\mathbb{Z}$ and $\mathbb{Z}/7\mathbb{Z}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosHeilbronn.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosHeilbronn.lean)).

* **MSC (2020)**: 11B13, 11P70, 05E99, 68V20, 12E05
* **Keywords**: Erdős-Heilbronn Conjecture, Restricted Sumset, Combinatorial Nullstellensatz, Cauchy-Davenport Theorem, Additive Combinatorics, Polynomial Method, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
