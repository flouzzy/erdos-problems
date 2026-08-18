# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Unit Distance Problem`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Unit Distance Problem, Combinatorial Geometry, Incidence Bounds, Crossing Number Inequality, Spencer-Szemerédi-Trotter, Guth-Katz Method, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `52C10, 05C10, 68V20, 52A10, 05C62`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Unit Distance Problem: A Detailed Treatise on Incidence Geometry, Spencer-Szemerédi-Trotter $n^{4/3}$ Bounds, Guth-Katz Polynomial Methods, and Certified Proofs</strong></p>

<p>The Erdős unit distance problem (Problem #33 in Paul Erdős' problem collection, 1946) is a foundational open question in combinatorial geometry. It asks for the maximum number of unit distance pairs u(n) that can be formed by n points in the Euclidean plane ℝ^2. Erdős conjectured that u(n) ≤ n^{1 + o(1)} = n^{1 + c / log log n}, matching the lower bound produced by a sqrt(n) × sqrt(n) section of the triangular lattice. In 1984, Joel Spencer, Endre Szemerédi, and William T. Trotter established the landmark upper bound u(n) ≤ C n^{4/3} via point-circle incidences and graph crossing numbers, which remains the best known upper bound to date.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Lattice Constructions &amp; Gaussian Sums:</strong> Non-elliptical derivation of Erdős' $\Omega(n^{1 + c/\log \log n})$ lower bound via the divisor function on sums of two squares $r_2(R^2)$.</li>
  <li><strong>The Crossing Number Inequality &amp; SST Bound:</strong> Step-by-step proof of the Spencer-Szemerédi-Trotter (1984) landmark bound $u(n) \le C n^{4/3}$ via point-circle incidence graphs and the crossing number inequality $\operatorname{cr}(G) \ge \frac{e^3}{29 v^2}$.</li>
  <li><strong>The Elekes-Sharir and Guth-Katz Framework:</strong> Survey of the 3D rigid motion Lie group $\mathrm{SE}(2) \cong \mathbb{R}^3$ representation, polynomial partitioning, and its impact on combinatorial incidence geometry.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> 2D rational geometry structures, squared Euclidean distance predicates, collinear chain invariants, and exact unit distance evaluations on unit square grids are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosUnitDistance.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 52C10, 05C10, 68V20, 52A10, 05C62<br />
<strong>Keywords:</strong> Erdős Unit Distance Problem, Combinatorial Geometry, Incidence Bounds, Crossing Number Inequality, Spencer-Szemerédi-Trotter, Guth-Katz Method, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Unit Distance Problem: A Detailed Treatise on Incidence Geometry, Spencer-Szemerédi-Trotter $n^{4/3}$ Bounds, Guth-Katz Polynomial Methods, and Certified Proofs**

The Erdős unit distance problem (Problem #33 in Paul Erdős' problem collection, 1946) is a foundational open question in combinatorial geometry. It asks for the maximum number of unit distance pairs u(n) that can be formed by n points in the Euclidean plane ℝ^2. Erdős conjectured that u(n) ≤ n^{1 + o(1)} = n^{1 + c / log log n}, matching the lower bound produced by a sqrt(n) × sqrt(n) section of the triangular lattice. In 1984, Joel Spencer, Endre Szemerédi, and William T. Trotter established the landmark upper bound u(n) ≤ C n^{4/3} via point-circle incidences and graph crossing numbers, which remains the best known upper bound to date.

### Key Mathematical Results & Contributions:
- **Lattice Constructions & Gaussian Sums:** Non-elliptical derivation of Erdős' $\Omega(n^{1 + c/\log \log n})$ lower bound via the divisor function on sums of two squares $r_2(R^2)$.
- **The Crossing Number Inequality & SST Bound:** Step-by-step proof of the Spencer-Szemerédi-Trotter (1984) landmark bound $u(n) \le C n^{4/3}$ via point-circle incidence graphs and the crossing number inequality $\operatorname{cr}(G) \ge \frac{e^3}{29 v^2}$.
- **The Elekes-Sharir and Guth-Katz Framework:** Survey of the 3D rigid motion Lie group $\mathrm{SE}(2) \cong \mathbb{R}^3$ representation, polynomial partitioning, and its impact on combinatorial incidence geometry.
- **100% Machine-Checked Verification in Lean 4:** 2D rational geometry structures, squared Euclidean distance predicates, collinear chain invariants, and exact unit distance evaluations on unit square grids are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosUnitDistance.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosUnitDistance.lean)).

* **MSC (2020)**: 52C10, 05C10, 68V20, 52A10, 05C62
* **Keywords**: Erdős Unit Distance Problem, Combinatorial Geometry, Incidence Bounds, Crossing Number Inequality, Spencer-Szemerédi-Trotter, Guth-Katz Method, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
