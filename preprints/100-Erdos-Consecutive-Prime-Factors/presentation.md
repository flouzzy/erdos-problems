# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Mahler Theorem on Prime Factors of Consecutive Integers`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Mahler Theorem, Greatest Prime Factor, Consecutive Integers, Linear Forms in Logarithms, Baker's Method, Diophantine Approximations, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11N05, 11D61, 11J86, 68V20, 11A41`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Mahler Theorem on Prime Factors of Consecutive Integers: A Detailed Treatise on Greatest Prime Factors of Products $n(n+1)$, $p$-Adic Thue-Siegel Approximations, Baker's Logarithmic Forms, and Certified Proofs</strong></p>

<p>The Erdős-Mahler consecutive prime factor problem (Problem #100 in Paul Erdős' problem collection / 1937) is a fundamental landmark in Diophantine number theory, prime distribution, and effective transcendence theory. Let $P(m)$ denote the greatest prime factor of an integer $m \ge 2$. In 1935, Kurt Mahler proved that $P(n(n+1)) \to \infty$ as $n \to \infty$ using $p$-adic Thue-Siegel approximations. In 1937, Paul Erdős established quantitative lower bounds and conjectured that $P(n(n+1)) > c \log \log n$. In subsequent decades, A. Schinzel, T. N. Shorey, R. Tijdeman, and C. L. Stewart applied Alan Baker's theory of linear forms in logarithms of algebraic numbers to prove effective lower bounds of the form $P(n(n+1)) \gg \log \log n \frac{\log \log \log n}{\log \log \log \log n}$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Consecutive Coprimality and Prime Partitioning:</strong> Formal non-elliptical proof that $\gcd(n, n+1) = 1$, ensuring disjoint prime factor sets between $n$ and $n+1$.</li>
  <li><strong>The Mahler-Erdős Divergence Theorem:</strong> Detailed structural analysis showing that $P(n(n+1)) \to \infty$ as $n \to \infty$.</li>
  <li><strong>Effective Baker-Type Lower Bounds:</strong> Survey of linear forms in logarithms establishing quantitative bounds on greatest prime factors.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Formal proofs of consecutive coprimality, exclusion of common prime divisors, and exact prime factor certifications for $n \in \{8, 14, 24\}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosPrimeFactorsConsecutive.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11N05, 11D61, 11J86, 68V20, 11A41<br />
<strong>Keywords:</strong> Erdős-Mahler Theorem, Greatest Prime Factor, Consecutive Integers, Linear Forms in Logarithms, Baker's Method, Diophantine Approximations, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Mahler Theorem on Prime Factors of Consecutive Integers: A Detailed Treatise on Greatest Prime Factors of Products $n(n+1)$, $p$-Adic Thue-Siegel Approximations, Baker's Logarithmic Forms, and Certified Proofs**

The Erdős-Mahler consecutive prime factor problem (Problem #100 in Paul Erdős' problem collection / 1937) is a fundamental landmark in Diophantine number theory, prime distribution, and effective transcendence theory. Let $P(m)$ denote the greatest prime factor of an integer $m \ge 2$.

### Key Mathematical Results & Contributions:
- **Consecutive Coprimality:** Proof that $\gcd(n, n+1) = 1$, ensuring disjoint prime factor sets.
- **The Mahler-Erdős Divergence Theorem:** Analysis showing $P(n(n+1)) \to \infty$ as $n \to \infty$.
- **Effective Baker-Type Lower Bounds:** Quantitative bounds via linear forms in logarithms.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosPrimeFactorsConsecutive.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosPrimeFactorsConsecutive.lean)).

* **MSC (2020)**: 11N05, 11D61, 11J86, 68V20, 11A41
* **Keywords**: Erdős-Mahler Theorem, Greatest Prime Factor, Consecutive Integers, Linear Forms in Logarithms, Baker's Method, Diophantine Approximations, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
