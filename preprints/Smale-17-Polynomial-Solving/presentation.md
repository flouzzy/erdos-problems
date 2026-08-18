# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On Polynomial System Solving in Average Polynomial Time and Smale's 17th Problem`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Smale's 17th Problem, Polynomial System Solving, Average Polynomial Time, Homotopy Continuation, Projective Newton Method, Bézout Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `68Q25, 65H10, 14Q20, 68V20, 14N05`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On Polynomial System Solving in Average Polynomial Time and Smale's 17th Problem: A Detailed Treatise on Projective Newton Homotopies, Condition Metric Geometry, Beltrán-Pardo Randomization, and Pierre Lairez's Theorem</strong></p>

<p>Smale's 17th Problem (Steve Smale, 2000) asks: "Can a zero of $n$ complex polynomial equations in $n+1$ homogeneous variables be found on average in polynomial time with respect to the input size $N$?" Between 2008 and 2016, this foundational challenge in numerical algebraic geometry was completely resolved through a sequence of breakthroughs by Carlos Beltrán, Luis Miguel Pardo, Felipe Cucker, Peter Bürgisser, and Pierre Lairez.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Input Space and Bézout Root Geometry:</strong> Exact formulation of the complex projective space dimension $N = \sum \binom{n+d_i}{d_i}$ and root count $\mathcal{D} = \prod d_i$.</li>
  <li><strong>Shub-Smale Solution Variety:</strong> Theoretical architecture of the condition number $\mu_{\text{norm}}(f, \zeta)$ and Riemannian condition metric.</li>
  <li><strong>Pierre Lairez's Resolution (2016):</strong> Complete analysis of the deterministic continuation algorithm achieving $T_{\text{avg}}(N) = O(N^6)$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Bézout bounds, projective input dimensions, and combinatorial binomial coefficients are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/Smale17PolynomialSolving.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 68Q25, 65H10, 14Q20, 68V20, 14N05<br />
<strong>Keywords:</strong> Smale's 17th Problem, Polynomial System Solving, Average Polynomial Time, Homotopy Continuation, Projective Newton Method, Bézout Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On Polynomial System Solving in Average Polynomial Time and Smale's 17th Problem: A Detailed Treatise on Projective Newton Homotopies, Condition Metric Geometry, Beltrán-Pardo Randomization, and Pierre Lairez's Theorem**

Smale's 17th Problem (Steve Smale, 2000) asks whether polynomial systems can be solved on average in polynomial time. Resolved by Beltrán-Pardo (2008), Bürgisser-Cucker (2011), and Pierre Lairez (2016).

### Key Mathematical Results & Contributions:
- **Input Space & Bézout Root Geometry:** $N = \sum \binom{n+d_i}{d_i}$ and $\mathcal{D} = \prod d_i$.
- **Shub-Smale Condition Framework:** Condition metric on the solution variety $V$.
- **Lairez's Theorem (2016):** Deterministic algorithm in average polynomial time $O(N^6)$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/Smale17PolynomialSolving.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/Smale17PolynomialSolving.lean)).

* **MSC (2020)**: 68Q25, 65H10, 14Q20, 68V20, 14N05
* **Keywords**: Smale's 17th Problem, Polynomial System Solving, Average Polynomial Time, Homotopy Continuation, Projective Newton Method, Bézout Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
