# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Lorenz Attractor and Smale's 14th Problem`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Smale's 14th Problem, Lorenz Attractor, Chaotic Dynamics, Strange Attractor, Validated Interval Arithmetic, Poincaré Maps, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `37D45, 34C28, 37C10, 68V20, 65G20`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Lorenz Attractor and Smale's 14th Problem: A Detailed Treatise on Validated Interval Arithmetic, Normal Form Theory, Geometric Strange Attractors, and Certified Proofs</strong></p>

<p>Smale's 14th Problem (Steve Smale, 2000) asks whether the classical Lorenz dynamical system (Edward Lorenz, 1963): $\dot{x} = \sigma (y - x), \dot{y} = x (\rho - z) - y, \dot{z} = x y - \beta z$ with standard parameter values $\sigma = 10, \rho = 28, \beta = 8/3$ admits a robust geometric strange attractor with hyperbolic structure. In 2002, Warwick Tucker solved Smale's 14th problem in the affirmative using rigorous computer-assisted interval arithmetic and normal form theory.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Uniform Phase Space Volume Contraction:</strong> Non-elliptical proof that $\operatorname{div} F = -\sigma - 1 - \beta = -41/3 < 0$, ensuring exponential phase space volume decay.</li>
  <li><strong>Complete Equilibrium Classification:</strong> Exact algebraic derivation of the origin $(0,0,0)$ and symmetric fixed points $C_\pm = (\pm 6\sqrt{2}, \pm 6\sqrt{2}, 27)$.</li>
  <li><strong>Tucker's Computational Hyperbolicity Architecture:</strong> Rigorous validation of Poincaré return maps, invariant cone fields, and trapping regions.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Divergence identities, equilibrium coordinates, and Jacobian properties are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/Smale14LorenzAttractor.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 37D45, 34C28, 37C10, 68V20, 65G20<br />
<strong>Keywords:</strong> Smale's 14th Problem, Lorenz Attractor, Chaotic Dynamics, Strange Attractor, Validated Interval Arithmetic, Poincaré Maps, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Lorenz Attractor and Smale's 14th Problem: A Detailed Treatise on Validated Interval Arithmetic, Normal Form Theory, Geometric Strange Attractors, and Certified Proofs**

Smale's 14th Problem (Steve Smale, 2000) asks whether the classical Lorenz dynamical system (Edward Lorenz, 1963) admits a robust geometric strange attractor. In 2002, Warwick Tucker solved Smale's 14th problem in the affirmative using rigorous computer-assisted interval arithmetic and normal form theory.

### Key Mathematical Results & Contributions:
- **Uniform Phase Space Volume Contraction:** Proof that $\operatorname{div} F = -41/3 < 0$.
- **Complete Equilibrium Classification:** Origin and $C_\pm = (\pm 6\sqrt{2}, \pm 6\sqrt{2}, 27)$.
- **Tucker's Hyperbolicity Proof:** Invariant cone fields on Poincaré sections.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/Smale14LorenzAttractor.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/Smale14LorenzAttractor.lean)).

* **MSC (2020)**: 37D45, 34C28, 37C10, 68V20, 65G20
* **Keywords**: Smale's 14th Problem, Lorenz Attractor, Chaotic Dynamics, Strange Attractor, Validated Interval Arithmetic, Poincaré Maps, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
