# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Szemerédi Sum-Product Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Szemerédi Conjecture, Sum-Product Problem, Additive Combinatorics, Szemerédi-Trotter Theorem, Point-Line Incidences, Additive Energy, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B75, 11B13, 05B25, 68V20, 52C10`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Szemerédi Sum-Product Conjecture: A Detailed Treatise on Additive and Multiplicative Energy, Elekes' Geometric Incidences, and Certified Proofs</strong></p>

<p>The Erdős-Szemerédi sum-product conjecture (Problem #35 in Paul Erdős' collection, 1983) is one of the foundational questions of arithmetic combinatorics. It asserts that for any finite set of real numbers A ⊂ ℝ, the sumset A + A and the product set A · A cannot simultaneously be small: max(|A + A|, |A · A|) ≥ c |A|^{2 - ε} for any ε > 0 and |A| ≥ N_0(ε). In 1997, György Elekes established the classic lower bound |A|^{5/4} by connecting sum-products to point-line incidences and the Szemerédi-Trotter theorem. Subsequent breakthroughs by Solymosi, Konyagin, Shkredov, and Rudnev-Stevens have pushed the exponent beyond 4/3.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Arithmetic vs Geometric Rigidity:</strong> Contrast between arithmetic progressions ($|A+A|=2n-1, |A \cdot A|=\Theta(n^2/\log n)$) and geometric progressions.</li>
  <li><strong>Elekes' Geometric Proof ($5/4$):</strong> Complete derivation of the $|A|^{5/4}$ bound using line families $y = a(x - b)$ and the Szemerédi-Trotter incidence theorem.</li>
  <li><strong>Additive Energy Duals:</strong> Cauchy-Schwarz connection between $|A+A|$ and the additive energy $E_+(A)$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Sumset and product set definitions, arithmetic progression minimal sumset proofs ($|A+A| \ge 2n-1$), and exact evaluations on progressions are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSzemerediSumProduct.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B75, 11B13, 05B25, 68V20, 52C10<br />
<strong>Keywords:</strong> Erdős-Szemerédi Conjecture, Sum-Product Problem, Additive Combinatorics, Szemerédi-Trotter Theorem, Point-Line Incidences, Additive Energy, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Szemerédi Sum-Product Conjecture: A Detailed Treatise on Additive and Multiplicative Energy, Elekes' Geometric Incidences, and Certified Proofs**

The Erdős-Szemerédi sum-product conjecture (Problem #35 in Paul Erdős' collection, 1983) is one of the foundational questions of arithmetic combinatorics. It asserts that for any finite set of real numbers A ⊂ ℝ, the sumset A + A and the product set A · A cannot simultaneously be small: max(|A + A|, |A · A|) ≥ c |A|^{2 - ε} for any ε > 0 and |A| ≥ N_0(ε). In 1997, György Elekes established the classic lower bound |A|^{5/4} by connecting sum-products to point-line incidences and the Szemerédi-Trotter theorem. Subsequent breakthroughs by Solymosi, Konyagin, Shkredov, and Rudnev-Stevens have pushed the exponent beyond 4/3.

### Key Mathematical Results & Contributions:
- **Arithmetic vs Geometric Rigidity:** Contrast between arithmetic progressions ($|A+A|=2n-1, |A \cdot A|=\Theta(n^2/\log n)$) and geometric progressions.
- **Elekes' Geometric Proof ($5/4$):** Complete derivation of the $|A|^{5/4}$ bound using line families $y = a(x - b)$ and the Szemerédi-Trotter incidence theorem.
- **Additive Energy Duals:** Cauchy-Schwarz connection between $|A+A|$ and the additive energy $E_+(A)$.
- **100% Machine-Checked Verification in Lean 4:** Sumset and product set definitions, arithmetic progression minimal sumset proofs ($|A+A| \ge 2n-1$), and exact evaluations on progressions are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSzemerediSumProduct.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSzemerediSumProduct.lean)).

* **MSC (2020)**: 11B75, 11B13, 05B25, 68V20, 52C10
* **Keywords**: Erdős-Szemerédi Conjecture, Sum-Product Problem, Additive Combinatorics, Szemerédi-Trotter Theorem, Point-Line Incidences, Additive Energy, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
