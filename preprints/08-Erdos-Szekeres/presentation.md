# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Szekeres Convex Polygon Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Szekeres Conjecture, Happy Ending Problem, Convex Polygon, General Position, Cup-Cap Theorem, Andrew Suk, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `52C10, 05D10, 52A10, 68V20, 05A17`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Szekeres Convex Polygon Conjecture: A Detailed Treatise on Planar General Position, the Happy Ending Problem, Suk's Asymptotic Breakthrough, and Certified Proofs</strong></p>

<p>The Erdős-Szekeres convex polygon conjecture (Problem #08 in Paul Erdős' collection, 1935), famously christened the 'Happy Ending Problem', is a foundational milestone of combinatorial geometry and Ramsey theory. The conjecture states that any set of N ≥ 2^{n-2} + 1 points in the Euclidean plane in general position (no three collinear) must contain at least n points in convex position forming the vertices of a convex n-gon. The bound is known to be exact for n = 3 (3 points), n = 4 (5 points, proved by Esther Klein), n = 5 (9 points, proved by Makai), and n = 6 (17 points, proved by Szekeres and Peters in 2006). In 2017, Andrew Suk established the definitive near-optimal asymptotic upper bound N(n) = 2^{n + o(n)} in the Annals of Mathematics.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Happy Ending Theorem:</strong> Complete proof of Esther Klein's theorem $g(4) = 5$ by case analysis on convex hulls.</li>
  <li><strong>The Cup-Cap Duality:</strong> Step-by-step proof of the Erdős-Szekeres Cup-Cap Theorem establishing $N(m, \ell) = \binom{m + \ell - 4}{m - 2} + 1$.</li>
  <li><strong>Suk's Asymptotic Breakthrough (2017):</strong> Exposition of Andrew Suk's proof $N(n) = 2^{n + o(n)}$ using dual line arrangements, hypergraph Ramsey theory, and positive-fraction selection lemmas.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> 2D orientation predicates, convex quadrilateral existence on 5 points, and binomial Cup-Cap identities are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSzekeres.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 52C10, 05D10, 52A10, 68V20, 05A17<br />
<strong>Keywords:</strong> Erdős-Szekeres Conjecture, Happy Ending Problem, Convex Polygon, General Position, Cup-Cap Theorem, Andrew Suk, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Szekeres Convex Polygon Conjecture: A Detailed Treatise on Planar General Position, the Happy Ending Problem, Suk's Asymptotic Breakthrough, and Certified Proofs**

The Erdős-Szekeres convex polygon conjecture (Problem #08 in Paul Erdős' collection, 1935), famously christened the 'Happy Ending Problem', is a foundational milestone of combinatorial geometry and Ramsey theory. The conjecture states that any set of N ≥ 2^{n-2} + 1 points in the Euclidean plane in general position (no three collinear) must contain at least n points in convex position forming the vertices of a convex n-gon. The bound is known to be exact for n = 3 (3 points), n = 4 (5 points, proved by Esther Klein), n = 5 (9 points, proved by Makai), and n = 6 (17 points, proved by Szekeres and Peters in 2006). In 2017, Andrew Suk established the definitive near-optimal asymptotic upper bound N(n) = 2^{n + o(n)} in the Annals of Mathematics.

### Key Mathematical Results & Contributions:
- **The Happy Ending Theorem:** Complete proof of Esther Klein's theorem $g(4) = 5$ by case analysis on convex hulls.
- **The Cup-Cap Duality:** Step-by-step proof of the Erdős-Szekeres Cup-Cap Theorem establishing $N(m, \ell) = \binom{m + \ell - 4}{m - 2} + 1$.
- **Suk's Asymptotic Breakthrough (2017):** Exposition of Andrew Suk's proof $N(n) = 2^{n + o(n)}$ using dual line arrangements, hypergraph Ramsey theory, and positive-fraction selection lemmas.
- **100% Machine-Checked Verification in Lean 4:** 2D orientation predicates, convex quadrilateral existence on 5 points, and binomial Cup-Cap identities are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSzekeres.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSzekeres.lean)).

* **MSC (2020)**: 52C10, 05D10, 52A10, 68V20, 05A17
* **Keywords**: Erdős-Szekeres Conjecture, Happy Ending Problem, Convex Polygon, General Position, Cup-Cap Theorem, Andrew Suk, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
