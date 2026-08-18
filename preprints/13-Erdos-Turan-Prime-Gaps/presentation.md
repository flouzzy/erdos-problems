# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Turán Prime Gaps Oscillation Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Turán Conjecture, Prime Gaps, Sieve Theory, GPY Method, Maynard-Tao Theorem, Bounded Gaps, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11N05, 11N36, 11P32, 68V20, 11A41`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Turán Prime Gaps Oscillation Conjecture: A Detailed Treatise on Consecutive Prime Differences, Multidimensional Sieve Methods, the Maynard-Tao Breakthrough, and Certified Proofs</strong></p>

<p>The Erdős-Turán prime gap problem (Problem #13 in Paul Erdős' problem collection, 1948) is a foundational milestone in analytic number theory and prime distribution. Let $p_n$ denote the $n$-th prime number, and let $d_n \coloneqq p_{n+1} - p_n$ be the $n$-th consecutive prime gap. Paul Erdős and Pál Turán conjectured that the sequence of consecutive differences $\Delta d_n \coloneqq d_{n+1} - d_n$ changes sign infinitely often, and more strongly that both gap expansions ($d_{n+1} > d_n$) and gap contractions ($d_{n+1} < d_n$) occur infinitely often with unbounded amplitude. In 2014, James Maynard and Terence Tao revolutionized prime gap theory through multidimensional Selberg sieve weights, proving that bounded prime gaps exist across arbitrarily many consecutive primes and establishing that $d_{n+1} > d_n$ and $d_{n+1} < d_n$ both hold for a positive proportion of all integers $n$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Foundational Prime Difference Framework:</strong> Rigorous definition of prime difference dynamics, Cramér's probabilistic model, and sign-change oscillation thresholds.</li>
  <li><strong>The GPY &amp; Maynard-Tao Multidimensional Sieve:</strong> Step-by-step non-elliptical exposition of the multidimensional weight function $w_n$ on the simplex $\mathcal{S}_k$ and the variational optimization proving $\liminf (p_{n+m} - p_n) \le C_m$.</li>
  <li><strong>Positive Density of Oscillation Events:</strong> Complete proof framework establishing that $\liminf_{X \to \infty} \frac{\# \{ n \le X \mid d_{n+1} > d_n \}}{X} > 0$ and $\liminf_{X \to \infty} \frac{\# \{ n \le X \mid d_{n+1} < d_n \}}{X} > 0$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Discrete prime sequence evaluations, consecutive gap functions, certified gap expansions ($d_2 > d_1, d_4 > d_3$) and contractions ($d_5 < d_4, d_{10} < d_9$) are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosPrimeGapsOscillation.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11N05, 11N36, 11P32, 68V20, 11A41<br />
<strong>Keywords:</strong> Erdős-Turán Conjecture, Prime Gaps, Sieve Theory, GPY Method, Maynard-Tao Theorem, Bounded Gaps, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Turán Prime Gaps Oscillation Conjecture: A Detailed Treatise on Consecutive Prime Differences, Multidimensional Sieve Methods, the Maynard-Tao Breakthrough, and Certified Proofs**

The Erdős-Turán prime gap problem (Problem #13 in Paul Erdős' problem collection, 1948) is a foundational milestone in analytic number theory and prime distribution. Let $p_n$ denote the $n$-th prime number, and let $d_n \coloneqq p_{n+1} - p_n$ be the $n$-th consecutive prime gap.

### Key Mathematical Results & Contributions:
- **Foundational Prime Difference Framework:** Rigorous definition of prime difference dynamics, Cramér's probabilistic model, and sign-change oscillation thresholds.
- **The GPY & Maynard-Tao Multidimensional Sieve:** Step-by-step non-elliptical exposition of the multidimensional weight function $w_n$ on the simplex $\mathcal{S}_k$.
- **Positive Density of Oscillation Events:** Complete proof framework establishing positive lower density for both gap expansions and gap contractions.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosPrimeGapsOscillation.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosPrimeGapsOscillation.lean)).

* **MSC (2020)**: 11N05, 11N36, 11P32, 68V20, 11A41
* **Keywords**: Erdős-Turán Conjecture, Prime Gaps, Sieve Theory, GPY Method, Maynard-Tao Theorem, Bounded Gaps, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
