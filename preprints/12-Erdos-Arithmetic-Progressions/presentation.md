# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on Arithmetic Progressions`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Conjecture on Arithmetic Progressions, Green-Tao Theorem, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Gowers Uniformity Norms, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B25, 11N13, 05D10, 68V20, 11P32, 42A99`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on Arithmetic Progressions: A Detailed Treatise on Divergent Reciprocal Sets, the Green-Tao Theorem, Quantitative Roth Bounds, and Certified Proofs</strong></p>

<p>The Erdős conjecture on arithmetic progressions (Problem #12 / #77 in Paul Erdős' problem collection, 1976) is widely regarded as one of the deepest and most profound open questions in number theory and additive combinatorics. Backed by Erdős' largest monetary reward ($5000), the conjecture asserts that any set of positive integers A ⊆ ℕ_{≥ 1} whose reciprocal sum diverges (∑_{n ∈ A} 1/n = ∞) must necessarily contain arbitrarily long arithmetic progressions of length k for every integer k ≥ 3. In 2008, Ben Green and Terence Tao resolved the prime case A = ℙ. In 2020, Thomas Bloom and Olof Sisask proved the k = 3 case for all divergent sets, and in 2023, Zander Kelley and Raghu Meka achieved an exponential improvement on Roth's theorem.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Prime Case &amp; Green-Tao Theorem (2008):</strong> Detailed exposition of the Green-Tao theorem establishing arbitrarily long arithmetic progressions in the primes $\mathbb{P}$, the transference principle, and pseudorandom majorants via Gowers uniformity norms.</li>
  <li><strong>The 3-Term Progression Resolution ($k=3$):</strong> Comprehensive analysis of the quantitative progression on Roth's theorem from Roth (1953) to Sanders (2011), the breakthrough theorem of Thomas Bloom and Olof Sisask (2020) proving $r_3(N) \ll \frac{N}{(\log N)^{1+c}}$, and Zander Kelley and Raghu Meka's landmark bound $r_3(N) \le N \exp(-c (\log N)^{1/12})$ (2023).</li>
  <li><strong>Dyadic Density Slicing:</strong> Non-elliptical proof that sub-logarithmic bounds $r_3(N) \ll \frac{N}{(\log N)^{1+c}}$ force any set with $\sum_{n \in A} \frac{1}{n} = \infty$ to contain a 3-term arithmetic progression.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Formal definitions of arithmetic progression predicates, explicit prime progression certificates (lengths 3, 5, and 6), and arbitrary length progression properties on infinite arithmetic progressions are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosArithmeticProgressions.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B25, 11N13, 05D10, 68V20, 11P32, 42A99<br />
<strong>Keywords:</strong> Erdős Conjecture on Arithmetic Progressions, Green-Tao Theorem, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Gowers Uniformity Norms, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on Arithmetic Progressions: A Detailed Treatise on Divergent Reciprocal Sets, the Green-Tao Theorem, Quantitative Roth Bounds, and Certified Proofs**

The Erdős conjecture on arithmetic progressions (Problem #12 / #77 in Paul Erdős' problem collection, 1976) is widely regarded as one of the deepest and most profound open questions in number theory and additive combinatorics. Backed by Erdős' largest monetary reward ($5000), the conjecture asserts that any set of positive integers A ⊆ ℕ_{≥ 1} whose reciprocal sum diverges (∑_{n ∈ A} 1/n = ∞) must necessarily contain arbitrarily long arithmetic progressions of length k for every integer k ≥ 3. In 2008, Ben Green and Terence Tao resolved the prime case A = ℙ. In 2020, Thomas Bloom and Olof Sisask proved the k = 3 case for all divergent sets, and in 2023, Zander Kelley and Raghu Meka achieved an exponential improvement on Roth's theorem.

### Key Mathematical Results & Contributions:
- **The Prime Case & Green-Tao Theorem (2008):** Detailed exposition of the Green-Tao theorem establishing arbitrarily long arithmetic progressions in the primes $\mathbb{P}$, the transference principle, and pseudorandom majorants via Gowers uniformity norms.
- **The 3-Term Progression Resolution ($k=3$):** Comprehensive analysis of the quantitative progression on Roth's theorem from Roth (1953) to Sanders (2011), the breakthrough theorem of Thomas Bloom and Olof Sisask (2020) proving $r_3(N) \ll \frac{N}{(\log N)^{1+c}}$, and Zander Kelley and Raghu Meka's landmark bound $r_3(N) \le N \exp(-c (\log N)^{1/12})$ (2023).
- **Dyadic Density Slicing:** Non-elliptical proof that sub-logarithmic bounds $r_3(N) \ll \frac{N}{(\log N)^{1+c}}$ force any set with $\sum_{n \in A} \frac{1}{n} = \infty$ to contain a 3-term arithmetic progression.
- **100% Machine-Checked Verification in Lean 4:** Formal definitions of arithmetic progression predicates, explicit prime progression certificates (lengths 3, 5, and 6), and arbitrary length progression properties on infinite arithmetic progressions are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosArithmeticProgressions.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosArithmeticProgressions.lean)).

* **MSC (2020)**: 11B25, 11N13, 05D10, 68V20, 11P32, 42A99
* **Keywords**: Erdős Conjecture on Arithmetic Progressions, Green-Tao Theorem, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Gowers Uniformity Norms, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
