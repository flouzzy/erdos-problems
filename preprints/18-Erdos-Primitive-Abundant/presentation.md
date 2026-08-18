# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on Primitive Abundant Numbers`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Primitive Abundant Numbers, Divisor Sum Function, Index of Abundance, Reciprocal Sums, Asymptotic Counting, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11A25, 11N37, 11N25, 68V20, 11B83`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on Primitive Abundant Numbers: A Detailed Treatise on Divisor Sums, Reciprocal Convergence, the Erdős Asymptotic Counting Theorem, and Certified Proofs</strong></p>

<p>The Erdős primitive abundant numbers problem (Problem #18 in Paul Erdős' problem collection, 1934) is a seminal milestone in multiplicative number theory, asymptotic density theory, and the arithmetic distribution of divisor sums. Let $\sigma(n) \coloneqq \sum_{d \mid n} d$ denote the sum of positive divisors of $n$. An integer $n \ge 1$ is called abundant if $\sigma(n) \ge 2n$, and primitive abundant if $n$ is abundant while every proper divisor $d \mid n$ ($d < n$) is deficient ($\sigma(d) < 2d$). Let $\mathcal{A}$ denote the set of primitive abundant numbers, and let $A(x) \coloneqq \# \{ n \le x \mid n \in \mathcal{A} \}$. In 1934, Paul Erdős proved that the sum of reciprocals of all primitive abundant numbers converges: $\sum_{n \in \mathcal{A}} \frac{1}{n} < \infty$, and established double-exponential counting bounds for $A(x)$. In 2013, Mitsuo Kobayashi established that the reciprocal sum is bounded: $\sum_{n \in \mathcal{A}} \frac{1}{n} \in (0.286, 0.407)$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Divisor Monotonicity of Abundance:</strong> Non-elliptical proof that the index of abundance $I(n) \coloneqq \sigma(n)/n$ is strictly increasing under proper divisor extensions ($I(d) < I(n)$).</li>
  <li><strong>Erdős' Reciprocal Convergence Theorem (1934):</strong> Step-by-step exposition of the convergence proof for $\sum_{n \in \mathcal{A}} 1/n < \infty$ via prime factor sieve partitions.</li>
  <li><strong>Asymptotic Counting Bounds:</strong> Derivation of the double-exponential bounds $\frac{x}{\exp(c_1 \sqrt{\log x \log \log x})} \le A(x) \le \frac{x}{\exp(c_2 \sqrt{\log x \log \log x})}$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Divisor sum predicates, proof that 6 is primitive abundant, proof that 12 is abundant but not primitive abundant, and certified evaluations on 20 and 28 are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosPrimitiveAbundant.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11A25, 11N37, 11N25, 68V20, 11B83<br />
<strong>Keywords:</strong> Erdős Primitive Abundant Numbers, Divisor Sum Function, Index of Abundance, Reciprocal Sums, Asymptotic Counting, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on Primitive Abundant Numbers: A Detailed Treatise on Divisor Sums, Reciprocal Convergence, the Erdős Asymptotic Counting Theorem, and Certified Proofs**

The Erdős primitive abundant numbers problem (Problem #18 in Paul Erdős' problem collection, 1934) is a seminal milestone in multiplicative number theory, asymptotic density theory, and the arithmetic distribution of divisor sums. Let $\sigma(n) \coloneqq \sum_{d \mid n} d$ denote the sum of positive divisors of $n$.

### Key Mathematical Results & Contributions:
- **Divisor Monotonicity of Abundance:** Strict inequality $I(d) < I(n)$ for proper divisors $d < n$.
- **Erdős' Reciprocal Convergence Theorem (1934):** Step-by-step exposition of the convergence proof for $\sum_{n \in \mathcal{A}} 1/n < \infty$.
- **Asymptotic Counting Bounds:** Derivation of the bounds $\frac{x}{\exp(c_1 \sqrt{\log x \log \log x})} \le A(x) \le \frac{x}{\exp(c_2 \sqrt{\log x \log \log x})}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosPrimitiveAbundant.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosPrimitiveAbundant.lean)).

* **MSC (2020)**: 11A25, 11N37, 11N25, 68V20, 11B83
* **Keywords**: Erdős Primitive Abundant Numbers, Divisor Sum Function, Index of Abundance, Reciprocal Sums, Asymptotic Counting, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
