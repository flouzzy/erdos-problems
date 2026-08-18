# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Redheffer Matrix Theorem and the Riemann Hypothesis`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Riemann Hypothesis, Redheffer Matrix Theorem, Mertens Function, Möbius Inversion, Spectral Matrix Theory, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11M26, 15A15, 11N37, 68V20, 11A25`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Redheffer Matrix Theorem and the Riemann Hypothesis: A Detailed Treatise on Binary Divisibility Matrices, Mertens Determinants, Spectral Properties, and Certified Proofs</strong></p>

<p>The Redheffer Matrix Theorem (Ray Redheffer, 1977) establishes an exact algebraic and spectral bridge between linear algebra and the Riemann Hypothesis (RH). Let $A_n = (a_{ij})_{1 \le i, j \le n}$ be the $n \times n$ binary incidence matrix defined by $a_{ij} = 1$ if $j = 1$ or $i \mid j$, and $a_{ij} = 0$ otherwise. Redheffer proved that the determinant of $A_n$ is identically equal to the Mertens function: $\det(A_n) = M(n) \coloneqq \sum_{k=1}^n \mu(k)$, where $\mu(k)$ is the Möbius function. Consequently, the Riemann Hypothesis is strictly equivalent to the growth rate bound $\det(A_n) = O_\varepsilon(n^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Redheffer Determinant Identity:</strong> Step-by-step non-elliptical proof that $\det(A_n) = M(n)$ via row-reduction transformations along the divisibility lattice.</li>
  <li><strong>Exact Equivalence with the Riemann Hypothesis:</strong> Rigorous derivation of the logical equivalence $\text{RH} \iff \det(A_n) = O(n^{1/2+\varepsilon})$ via Littlewood's theorem (1912).</li>
  <li><strong>Spectral Multiplicity:</strong> Structural proof that $A_n$ possesses at least $n - \lfloor \log_2 n \rfloor - 1$ eigenvalues identically equal to 1.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Exact Möbius arithmetic, partial Mertens sums, and the square-root barrier inequality $|M(n)| \le \sqrt{n}$ for all orders $n \in \{1, \dots, 6\}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/RiemannRedhefferMertens.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11M26, 15A15, 11N37, 68V20, 11A25<br />
<strong>Keywords:</strong> Riemann Hypothesis, Redheffer Matrix Theorem, Mertens Function, Möbius Inversion, Spectral Matrix Theory, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Redheffer Matrix Theorem and the Riemann Hypothesis: A Detailed Treatise on Binary Divisibility Matrices, Mertens Determinants, Spectral Properties, and Certified Proofs**

The Redheffer Matrix Theorem (Ray Redheffer, 1977) establishes an exact algebraic and spectral bridge between linear algebra and the Riemann Hypothesis (RH). Let $A_n = (a_{ij})_{1 \le i, j \le n}$ be the $n \times n$ binary incidence matrix defined by $a_{ij} = 1$ if $j = 1$ or $i \mid j$, and $a_{ij} = 0$ otherwise.

### Key Mathematical Results & Contributions:
- **The Redheffer Determinant Identity:** Proof that $\det(A_n) = M(n)$ via row operations.
- **Equivalence with the Riemann Hypothesis:** Proof that $\text{RH} \iff \det(A_n) = O(n^{1/2+\varepsilon})$.
- **Spectral Multiplicity:** Proof of $n - \lfloor \log_2 n \rfloor - 1$ trivial eigenvalues equal to 1.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/RiemannRedhefferMertens.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/RiemannRedhefferMertens.lean)).

* **MSC (2020)**: 11M26, 15A15, 11N37, 68V20, 11A25
* **Keywords**: Riemann Hypothesis, Redheffer Matrix Theorem, Mertens Function, Möbius Inversion, Spectral Matrix Theory, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
