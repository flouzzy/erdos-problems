# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Faber-Lovász Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Faber-Lovász Conjecture, Linear Hypergraphs, Graph Coloring, Chromatic Index, Projective Planes, Absorbing Method, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05C15, 05C65, 05B25, 68V20, 05D40`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Faber-Lovász Conjecture: A Detailed Treatise on Linear Hypergraph Colorings, Asymptotic Bounds, the Kang-Kelly-Kühn-Methuku-Osthus Breakthrough, and Certified Proofs</strong></p>

<p>The Erdős-Faber-Lovász (EFL) conjecture (Problem #05 in Paul Erdős' collection, 1972) is one of the most renowned open problems in extremal graph theory and combinatorics. The conjecture asserts that if A_1, ..., A_n are n cliques, each containing at most n vertices, such that any two distinct cliques intersect in at most one vertex (|A_i ∩ A_j| ≤ 1 for all i ≠ j, i.e. a linear hypergraph), then the chromatic number of their union graph satisfies χ(⋃_{i=1}^n A_i) ≤ n. Equivalently, every linear hypergraph on n vertices has chromatic index χ'(H) ≤ n. In 1992, Jeff Kahn established the asymptotic version χ(G) ≤ n + o(n). In 2021, Dong Yeap Kang, Tom Kelly, Daniela Kühn, Abhishek Methuku, and Deryk Osthus completely resolved the conjecture for all sufficiently large n ≥ n_0 using the absorbing method and fractional matching decompositions.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Dual Hypergraph Equivalence:</strong> Non-elliptical equivalence between vertex colorings of clique union graphs and chromatic indices of linear hypergraphs ($\chi'(H) \le |V(H)|$).</li>
  <li><strong>Projective Plane Extremality:</strong> Complete analysis of the finite projective plane configuration $PG(2, q)$ achieving exact equality $\chi(G) = n = q^2 + q + 1$.</li>
  <li><strong>Asymptotic &amp; Exact Proofs:</strong> Exposition of Jeff Kahn's asymptotic bound $\chi(G) \le n + o(n)$ (1992) and the complete resolution for large $n \ge n_0$ by Kang, Kelly, Kühn, Methuku, and Osthus (2021) via the absorbing method.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Linearity predicates and chromatic bound certifications for base configurations $n = 1, 2, 3$ are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosFaberLovasz.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05C15, 05C65, 05B25, 68V20, 05D40<br />
<strong>Keywords:</strong> Erdős-Faber-Lovász Conjecture, Linear Hypergraphs, Graph Coloring, Chromatic Index, Projective Planes, Absorbing Method, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Faber-Lovász Conjecture: A Detailed Treatise on Linear Hypergraph Colorings, Asymptotic Bounds, the Kang-Kelly-Kühn-Methuku-Osthus Breakthrough, and Certified Proofs**

The Erdős-Faber-Lovász (EFL) conjecture (Problem #05 in Paul Erdős' collection, 1972) is one of the most renowned open problems in extremal graph theory and combinatorics. The conjecture asserts that if A_1, ..., A_n are n cliques, each containing at most n vertices, such that any two distinct cliques intersect in at most one vertex (|A_i ∩ A_j| ≤ 1 for all i ≠ j, i.e. a linear hypergraph), then the chromatic number of their union graph satisfies χ(⋃_{i=1}^n A_i) ≤ n. Equivalently, every linear hypergraph on n vertices has chromatic index χ'(H) ≤ n. In 1992, Jeff Kahn established the asymptotic version χ(G) ≤ n + o(n). In 2021, Dong Yeap Kang, Tom Kelly, Daniela Kühn, Abhishek Methuku, and Deryk Osthus completely resolved the conjecture for all sufficiently large n ≥ n_0 using the absorbing method and fractional matching decompositions.

### Key Mathematical Results & Contributions:
- **Dual Hypergraph Equivalence:** Non-elliptical equivalence between vertex colorings of clique union graphs and chromatic indices of linear hypergraphs ($\chi'(H) \le |V(H)|$).
- **Projective Plane Extremality:** Complete analysis of the finite projective plane configuration $PG(2, q)$ achieving exact equality $\chi(G) = n = q^2 + q + 1$.
- **Asymptotic & Exact Proofs:** Exposition of Jeff Kahn's asymptotic bound $\chi(G) \le n + o(n)$ (1992) and the complete resolution for large $n \ge n_0$ by Kang, Kelly, Kühn, Methuku, and Osthus (2021) via the absorbing method.
- **100% Machine-Checked Verification in Lean 4:** Linearity predicates and chromatic bound certifications for base configurations $n = 1, 2, 3$ are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosFaberLovasz.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosFaberLovasz.lean)).

* **MSC (2020)**: 05C15, 05C65, 05B25, 68V20, 05D40
* **Keywords**: Erdős-Faber-Lovász Conjecture, Linear Hypergraphs, Graph Coloring, Chromatic Index, Projective Planes, Absorbing Method, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
