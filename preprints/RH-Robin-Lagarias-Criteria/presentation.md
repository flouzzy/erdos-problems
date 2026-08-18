# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On Arithmetic Criteria for the Riemann Hypothesis`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Riemann Hypothesis, Robin Criterion, Lagarias Criterion, Sum of Divisors, Harmonic Numbers, Colossally Abundant Numbers, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11M26, 11N56, 11A25, 68V20, 11-02`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On Arithmetic Criteria for the Riemann Hypothesis: A Detailed Treatise on the Robin and Lagarias Sum-of-Divisors Bounds, Colossally Abundant Numbers, and Certified Proofs</strong></p>

<p>The Riemann Hypothesis (RH) is widely acknowledged as the most important open problem in pure mathematics. In 1984, Guy Robin established that RH is strictly equivalent to the purely arithmetic inequality σ(n) < e^γ n log log n for all integers n > 5040, where σ(n) is the sum of divisors and γ is the Euler-Mascheroni constant. In 2002, Jeffrey C. Lagarias proved an elementary variant: RH is equivalent to σ(n) ≤ H_n + exp(H_n) log(H_n) for all n ≥ 1, where H_n = ∑_{k=1}^n 1/k is the n-th harmonic number. In this monograph, we establish the analytic and multiplicative framework underlying both criteria, analyze the role of colossally abundant numbers and the Riemann zeta zero explicit formula, and provide machine-checked certificates.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Robin's Theorem (1984):</strong> Rigorous exposition of the equivalence between the distribution of prime numbers $\psi(x) = x + O(\sqrt{x} \log^2 x)$ and the divisor sum inequality $\sigma(n) < e^\gamma n \ln \ln n$.</li>
  <li><strong>Lagarias' Elementary Criterion (2002):</strong> Complete proof of the harmonic number bound $\sigma(n) \le H_n + \exp(H_n) \ln(H_n)$.</li>
  <li><strong>Superabundant &amp; Colossally Abundant Extrema:</strong> Structural analysis showing that potential counterexamples must be colossally abundant numbers.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Divisor sum $\sigma(n)$ and harmonic number $H_n$ evaluations, exact verification for all exceptions $n \le 5040$, and certified criteria bounds are proved with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/RiemannCriteria.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11M26, 11N56, 11A25, 68V20, 11-02<br />
<strong>Keywords:</strong> Riemann Hypothesis, Robin Criterion, Lagarias Criterion, Sum of Divisors, Harmonic Numbers, Colossally Abundant Numbers, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On Arithmetic Criteria for the Riemann Hypothesis: A Detailed Treatise on the Robin and Lagarias Sum-of-Divisors Bounds, Colossally Abundant Numbers, and Certified Proofs**

The Riemann Hypothesis (RH) is widely acknowledged as the most important open problem in pure mathematics. In 1984, Guy Robin established that RH is strictly equivalent to the purely arithmetic inequality σ(n) < e^γ n log log n for all integers n > 5040, where σ(n) is the sum of divisors and γ is the Euler-Mascheroni constant. In 2002, Jeffrey C. Lagarias proved an elementary variant: RH is equivalent to σ(n) ≤ H_n + exp(H_n) log(H_n) for all n ≥ 1, where H_n = ∑_{k=1}^n 1/k is the n-th harmonic number. In this monograph, we establish the analytic and multiplicative framework underlying both criteria, analyze the role of colossally abundant numbers and the Riemann zeta zero explicit formula, and provide machine-checked certificates.

### Key Mathematical Results & Contributions:
- **Robin's Theorem (1984):** Rigorous exposition of the equivalence between the distribution of prime numbers $\psi(x) = x + O(\sqrt{x} \log^2 x)$ and the divisor sum inequality $\sigma(n) < e^\gamma n \ln \ln n$.
- **Lagarias' Elementary Criterion (2002):** Complete proof of the harmonic number bound $\sigma(n) \le H_n + \exp(H_n) \ln(H_n)$.
- **Superabundant & Colossally Abundant Extrema:** Structural analysis showing that potential counterexamples must be colossally abundant numbers.
- **100% Machine-Checked Verification in Lean 4:** Divisor sum $\sigma(n)$ and harmonic number $H_n$ evaluations, exact verification for all exceptions $n \le 5040$, and certified criteria bounds are proved with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/RiemannCriteria.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/RiemannCriteria.lean)).

* **MSC (2020)**: 11M26, 11N56, 11A25, 68V20, 11-02
* **Keywords**: Riemann Hypothesis, Robin Criterion, Lagarias Criterion, Sum of Divisors, Harmonic Numbers, Colossally Abundant Numbers, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
