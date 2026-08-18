# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Square Factors of Central Binomial Coefficients`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Binomial Conjecture, Central Binomial Coefficient, Square-Free Integers, Kummer's Theorem, p-adic Valuations, Granville-Ramaré Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B65, 11A51, 11N05, 68V20, 05A10`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Square Factors of Central Binomial Coefficients: A Detailed Treatise on Kummer's Theorem, Prime Base Expansions, the Granville-Ramaré Theorem, and Certified Proofs</strong></p>

<p>The Erdős square-free binomial coefficient conjecture (Problem #32 in Paul Erdős' problem collection, 1975) is a cornerstone milestone in multiplicative number theory and prime distribution. The conjecture asserts that for all integers $n > 4$, the central binomial coefficient $\binom{2n}{n}$ is never square-free: $\forall n > 4, \exists p \in \mathbb{P}, p^2 \mid \binom{2n}{n}$. The only integers for which $\binom{2n}{n}$ is square-free are $n = 1$ ($\binom{2}{1} = 2$), $n = 2$ ($\binom{4}{2} = 6$), and $n = 4$ ($\binom{8}{4} = 70 = 2 \cdot 5 \cdot 7$). In 1985, András Sárközy proved the conjecture for all sufficiently large $n$. In 1996, Andrew Granville and Olivier Ramaré completely and unconditionally proved the conjecture for all $n > 4$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Full Exception Census:</strong> Complete derivation and classification of the exact square-free exception set $\mathcal{E} = \{1, 2, 4\}$ with $\binom{2}{1} = 2$, $\binom{4}{2} = 6$, and $\binom{8}{4} = 70$.</li>
  <li><strong>Kummer's Carry Theorem:</strong> Step-by-step connection between $p$-adic valuations $\nu_p\left(\binom{2n}{n}\right)$ and base-$p$ arithmetic carries during the addition $n + n$.</li>
  <li><strong>The Granville-Ramaré Framework (1996):</strong> Comprehensive exposition of the computational threshold ($n \le 2^{30}$) and medium prime interval sieving ($\sqrt{2n} < p \le \sqrt{8n/3}$) via explicit Prime Number Theorem estimates.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Central binomial coefficient evaluations and square-prime divisibility proofs for $n = 3, 5, 6, 7, 8$ ($p = 2, 3$) are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosCentralBinomialSquareFree.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B65, 11A51, 11N05, 68V20, 05A10<br />
<strong>Keywords:</strong> Erdős Binomial Conjecture, Central Binomial Coefficient, Square-Free Integers, Kummer's Theorem, p-adic Valuations, Granville-Ramaré Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Square Factors of Central Binomial Coefficients: A Detailed Treatise on Kummer's Theorem, Prime Base Expansions, the Granville-Ramaré Theorem, and Certified Proofs**

The Erdős square-free binomial coefficient conjecture (Problem #32 in Paul Erdős' problem collection, 1975) is a cornerstone milestone in multiplicative number theory and prime distribution. The conjecture asserts that for all integers $n > 4$, the central binomial coefficient $\binom{2n}{n}$ is never square-free: $\forall n > 4, \exists p \in \mathbb{P}, p^2 \mid \binom{2n}{n}$. The only integers for which $\binom{2n}{n}$ is square-free are $n = 1$ ($\binom{2}{1} = 2$), $n = 2$ ($\binom{4}{2} = 6$), and $n = 4$ ($\binom{8}{4} = 70$).

### Key Mathematical Results & Contributions:
- **Full Exception Census:** Complete derivation and classification of the exact square-free exception set $\mathcal{E} = \{1, 2, 4\}$ with $\binom{2}{1} = 2$, $\binom{4}{2} = 6$, and $\binom{8}{4} = 70$.
- **Kummer's Carry Theorem:** Step-by-step connection between $p$-adic valuations $\nu_p\left(\binom{2n}{n}\right)$ and base-$p$ arithmetic carries during the addition $n + n$.
- **The Granville-Ramaré Framework (1996):** Comprehensive exposition of the computational threshold ($n \le 2^{30}$) and medium prime interval sieving ($\sqrt{2n} < p \le \sqrt{8n/3}$) via explicit Prime Number Theorem estimates.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosCentralBinomialSquareFree.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosCentralBinomialSquareFree.lean)).

* **MSC (2020)**: 11B65, 11A51, 11N05, 68V20, 05A10
* **Keywords**: Erdős Binomial Conjecture, Central Binomial Coefficient, Square-Free Integers, Kummer's Theorem, p-adic Valuations, Granville-Ramaré Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
