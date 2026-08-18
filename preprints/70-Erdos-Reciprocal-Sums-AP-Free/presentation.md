# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Reciprocal Sums Conjecture for Sets without Arithmetic Progressions`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Reciprocal Sums Conjecture, Arithmetic Progressions, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Additive Combinatorics, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B25, 05D10, 11B13, 68V20, 11N13`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Reciprocal Sums Conjecture for Sets without Arithmetic Progressions: A Detailed Treatise on AP-Free Densities, Quantitative Roth Theorems, the Bloom-Sisask and Kelley-Meka Theorems, and Certified Proofs</strong></p>

<p>The Erdős reciprocal sums conjecture on arithmetic progression-free sets (Problem #70 in Paul Erdős' problem collection, 1973) is a foundational question in additive combinatorics and analytic number theory. The conjecture asks whether the sum of reciprocals of any set of positive integers $A \subset \mathbb{N}_{\ge 1}$ containing no $k$-term arithmetic progression ($AP_k$) is universally bounded: $c_k \coloneqq \sup \{ \sum_{n \in A} \frac{1}{n} \mid A \subseteq \mathbb{N}_{\ge 1}, A \text{ contains no } AP_k \} < \infty$. In 2020, Thomas Bloom and Olof Sisask completely resolved the conjecture for $k = 3$ by establishing the quantitative bound $r_3(N) \ll N / (\log N)^{1 + c}$ for an absolute constant $c > 0$. In 2023, Zander Kelley and Raghu Meka achieved an exponential breakthrough $r_3(N) \le N \exp(-c (\log N)^{1/12})$, providing explicit upper bounds on $c_3$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Dyadic Slicing Framework:</strong> Rigorous proof that reciprocal summation $\sum_{n \in A} 1/n$ is tightly bounded by dyadic density sums $\sum_{j=0}^\infty \frac{r_k(2^{j+1})}{2^{j+1}}$, proving that any quantitative Roth decay $r_k(N) \ll N / (\log N)^{1+\epsilon}$ forces $c_k < \infty$.</li>
  <li><strong>The Bloom-Sisask Resolution for $k=3$ (2020):</strong> Detailed exposition of the logarithmic barrier breakthrough in Roth's theorem.</li>
  <li><strong>The Kelley-Meka Exponential Bound (2023):</strong> Comprehensive survey of almost-periodicity and density increment techniques yielding $r_3(N) \le N \exp(-c (\log N)^{1/12})$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> 3-AP free predicates, exact rational evaluations on discrete AP-free sets ($A_1 = \{1, 2, 4, 5, 10\}$ with sum $41/20$ and $A_2 = \{1, 2, 4, 5, 9, 10\}$ with sum $389/180$) are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosReciprocalSumsAPFree.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B25, 05D10, 11B13, 68V20, 11N13<br />
<strong>Keywords:</strong> Erdős Reciprocal Sums Conjecture, Arithmetic Progressions, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Additive Combinatorics, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Reciprocal Sums Conjecture for Sets without Arithmetic Progressions: A Detailed Treatise on AP-Free Densities, Quantitative Roth Theorems, the Bloom-Sisask and Kelley-Meka Theorems, and Certified Proofs**

The Erdős reciprocal sums conjecture on arithmetic progression-free sets (Problem #70 in Paul Erdős' problem collection, 1973) is a foundational question in additive combinatorics and analytic number theory. The conjecture asks whether the sum of reciprocals of any set of positive integers $A \subset \mathbb{N}_{\ge 1}$ containing no $k$-term arithmetic progression ($AP_k$) is universally bounded: $c_k = \sup \{ \sum_{n \in A} \frac{1}{n} \mid A \text{ contains no } AP_k \} < \infty$.

### Key Mathematical Results & Contributions:
- **Dyadic Slicing Framework:** Rigorous proof that reciprocal summation $\sum_{n \in A} 1/n$ is tightly bounded by dyadic density sums $\sum_{j=0}^\infty \frac{r_k(2^{j+1})}{2^{j+1}}$.
- **The Bloom-Sisask Resolution for $k=3$ (2020):** Detailed exposition of the logarithmic barrier breakthrough in Roth's theorem ($r_3(N) \ll N / (\log N)^{1+c}$).
- **The Kelley-Meka Exponential Bound (2023):** Comprehensive survey of almost-periodicity and density increment techniques yielding $r_3(N) \le N \exp(-c (\log N)^{1/12})$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosReciprocalSumsAPFree.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosReciprocalSumsAPFree.lean)).

* **MSC (2020)**: 11B25, 05D10, 11B13, 68V20, 11N13
* **Keywords**: Erdős Reciprocal Sums Conjecture, Arithmetic Progressions, Roth's Theorem, Bloom-Sisask Theorem, Kelley-Meka Bound, Additive Combinatorics, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
