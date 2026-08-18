# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Moser Diophantine Equation`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Moser Equation, Diophantine Equations, Power Sums, Moser Sieve, Modular Arithmetic, Continued Fractions, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D41, 11B68, 11A07, 68V20, 11Y50`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Moser Diophantine Equation: A Detailed Treatise on Power Sum Exclusions, Moser's Modular Sieve, Continued Fractions, and Certified Proofs</strong></p>

<p>The Erdős-Moser Diophantine equation (Problem #11 in Paul Erdős' collection, 1953) asks whether the sum of consecutive powers 1^k + 2^k + ... + (m-1)^k = m^k has any positive integer solutions other than the trivial identity 1^1 + 2^1 = 3^1 (m = 3, k = 1). In 1953, Leo Moser established that any non-trivial solution must satisfy m > 10^{10^6}, and proved that k must be even, m - 1 must be prime, and that m is constrained by an infinite family of modular congruences. In 2011, Pieter Moree and colleagues pushed the bound to m > 10^{10^9}.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Critical Diagonal Scaling:</strong> Asymptotic derivation proving $m \approx \frac{k+1}{\ln 2}$.</li>
  <li><strong>Parity and Small $m$ Exclusions:</strong> Complete proofs that $k$ must be even and that no integer solutions exist for $m = 4$ and $m = 5$.</li>
  <li><strong>Moser's Modular Sieve:</strong> Non-elliptical proof that $p \mid (m - 1) \implies (m - 1) \mid k$, showing that any solution requires millions of distinct prime factors.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Strict monotonicity, power sum definitions, and exact solutions for $m=3, k=1$ alongside exclusions for $m=4, 5$ are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosMoserGeneral.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D41, 11B68, 11A07, 68V20, 11Y50<br />
<strong>Keywords:</strong> Erdős-Moser Equation, Diophantine Equations, Power Sums, Moser Sieve, Modular Arithmetic, Continued Fractions, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Moser Diophantine Equation: A Detailed Treatise on Power Sum Exclusions, Moser's Modular Sieve, Continued Fractions, and Certified Proofs**

The Erdős-Moser Diophantine equation (Problem #11 in Paul Erdős' collection, 1953) asks whether the sum of consecutive powers 1^k + 2^k + ... + (m-1)^k = m^k has any positive integer solutions other than the trivial identity 1^1 + 2^1 = 3^1 (m = 3, k = 1). In 1953, Leo Moser established that any non-trivial solution must satisfy m > 10^{10^6}, and proved that k must be even, m - 1 must be prime, and that m is constrained by an infinite family of modular congruences. In 2011, Pieter Moree and colleagues pushed the bound to m > 10^{10^9}.

### Key Mathematical Results & Contributions:
- **Critical Diagonal Scaling:** Asymptotic derivation proving $m \approx \frac{k+1}{\ln 2}$.
- **Parity and Small $m$ Exclusions:** Complete proofs that $k$ must be even and that no integer solutions exist for $m = 4$ and $m = 5$.
- **Moser's Modular Sieve:** Non-elliptical proof that $p \mid (m - 1) \implies (m - 1) \mid k$, showing that any solution requires millions of distinct prime factors.
- **100% Machine-Checked Verification in Lean 4:** Strict monotonicity, power sum definitions, and exact solutions for $m=3, k=1$ alongside exclusions for $m=4, 5$ are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosMoserGeneral.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosMoserGeneral.lean)).

* **MSC (2020)**: 11D41, 11B68, 11A07, 68V20, 11Y50
* **Keywords**: Erdős-Moser Equation, Diophantine Equations, Power Sums, Moser Sieve, Modular Arithmetic, Continued Fractions, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
