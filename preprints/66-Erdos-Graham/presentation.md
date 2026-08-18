# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Graham Egyptian Fraction Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Graham Conjecture, Egyptian Fractions, Monochromatic Subsets, Unit Fractions, Croot's Theorem, Smooth Numbers, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D68, 11B75, 05D10, 68V20, 11N25`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Graham Egyptian Fraction Conjecture: A Detailed Treatise on Monochromatic Unit Fractions, Smooth Number Densities, Croot's Theorem, and Certified Proofs</strong></p>

<p>The Erdős-Graham conjecture on Egyptian fractions (Problem #66 in Paul Erdős' problem collection, 1980) was a prominent open problem in combinatorial number theory carrying a $500 monetary reward. The conjecture asserts that for every r-coloring of the positive integers ℕ_{≥ 2} = C_1 ∪ ... ∪ C_r, there exists at least one monochromatic color class C_i containing a finite subset S ⊆ C_i whose reciprocals sum to exactly one: ∑_{s ∈ S} 1/s = 1. In 2003, Ernie Croot completely resolved the conjecture in his landmark Annals of Mathematics paper by establishing a general density theorem on subsets of smooth integers.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Egyptian Representation Identities:</strong> Full derivation of classical identity families such as $1 = 1/2 + 1/3 + 1/6$ and greedy unit decompositions.</li>
  <li><strong>Croot's Density Theorem (Annals 2003):</strong> Detailed exposition of Ernie Croot's proof showing that any set of integers with positive upper density contains a subset summing to 1.</li>
  <li><strong>Smooth Numbers &amp; Saddle-Point Methods:</strong> The role of $y$-smooth integers and exponential sum bounds in constructing unit fractions.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Exact rational Egyptian fractions, unit sum predicates, and non-empty disjoint subset sum certifications are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosGraham.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D68, 11B75, 05D10, 68V20, 11N25<br />
<strong>Keywords:</strong> Erdős-Graham Conjecture, Egyptian Fractions, Monochromatic Subsets, Unit Fractions, Croot's Theorem, Smooth Numbers, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Graham Egyptian Fraction Conjecture: A Detailed Treatise on Monochromatic Unit Fractions, Smooth Number Densities, Croot's Theorem, and Certified Proofs**

The Erdős-Graham conjecture on Egyptian fractions (Problem #66 in Paul Erdős' problem collection, 1980) was a prominent open problem in combinatorial number theory carrying a $500 monetary reward. The conjecture asserts that for every r-coloring of the positive integers ℕ_{≥ 2} = C_1 ∪ ... ∪ C_r, there exists at least one monochromatic color class C_i containing a finite subset S ⊆ C_i whose reciprocals sum to exactly one: ∑_{s ∈ S} 1/s = 1. In 2003, Ernie Croot completely resolved the conjecture in his landmark Annals of Mathematics paper by establishing a general density theorem on subsets of smooth integers.

### Key Mathematical Results & Contributions:
- **Egyptian Representation Identities:** Full derivation of classical identity families such as $1 = 1/2 + 1/3 + 1/6$ and greedy unit decompositions.
- **Croot's Density Theorem (Annals 2003):** Detailed exposition of Ernie Croot's proof showing that any set of integers with positive upper density contains a subset summing to 1.
- **Smooth Numbers & Saddle-Point Methods:** The role of $y$-smooth integers and exponential sum bounds in constructing unit fractions.
- **100% Machine-Checked Verification in Lean 4:** Exact rational Egyptian fractions, unit sum predicates, and non-empty disjoint subset sum certifications are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosGraham.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosGraham.lean)).

* **MSC (2020)**: 11D68, 11B75, 05D10, 68V20, 11N25
* **Keywords**: Erdős-Graham Conjecture, Egyptian Fractions, Monochromatic Subsets, Unit Fractions, Croot's Theorem, Smooth Numbers, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
