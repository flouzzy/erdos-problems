# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Ginzburg-Ziv Theorem on Zero-Sum Sequences`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Ginzburg-Ziv Theorem, Zero-Sum Sequences, Davenport Constant, Chevalley-Warning Theorem, Cauchy-Davenport Theorem, Kemnitz's Conjecture, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B75, 11P70, 05D10, 68V20, 20K01`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Ginzburg-Ziv Theorem on Zero-Sum Sequences: A Detailed Treatise on Combinatorial Zero-Sums, Chevalley-Warning Reductions, the Davenport Constant, and Certified Proofs</strong></p>

<p>The Erdős-Ginzburg-Ziv (EGZ) theorem (Problem #06 in Paul Erdős' problem collection, 1961) is a seminal milestone in additive number theory, finite group theory, and zero-sum Ramsey theory. The theorem establishes that every sequence of $2n - 1$ integers contains a subsequence of length exactly $n$ whose sum is divisible by $n$: $\forall a_1, \dots, a_{2n-1} \in \mathbb{Z}, \exists I \subseteq \{1, \dots, 2n-1\}, |I| = n \text{ and } \sum_{i \in I} a_i \equiv 0 \pmod n$. The threshold $2n - 1$ is strictly sharp, as demonstrated by the multiset containing $n - 1$ zeros and $n - 1$ ones.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Strict Sharpness Analysis:</strong> Full non-elliptical proof that the multiset of $n - 1$ zeros and $n - 1$ ones of length $2n - 2$ contains no $n$-term subsequence summing to $0 \pmod n$.</li>
  <li><strong>The Chevalley-Warning Polynomial Proof for Primes:</strong> Rigorous reduction to a system of two degree $p-1$ polynomials in $2p-1$ variables over $\mathbb{F}_p$, applying the Chevalley-Warning theorem to guarantee non-trivial $p$-subsequence zeros.</li>
  <li><strong>Multiplicative Composite Induction:</strong> Step-by-step inductive lift proving that if EGZ holds for $a$ and $b$, it unconditionally holds for $n = ab$.</li>
  <li><strong>Higher-Dimensional Generalizations:</strong> Survey of the Davenport constant $D(G)$, the generalized EGZ constant $\mathsf{s}(G)$, and Christian Reiher's (2007) resolution of Kemnitz's conjecture on $\mathbb{Z}_p^2$ ($\mathsf{s}(\mathbb{Z}_p^2) = 4p - 3$).</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> EGZ zero-sum predicates, base certificates for $n = 1, 2$, and exact sharpness bounds are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosGinzburgZiv.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B75, 11P70, 05D10, 68V20, 20K01<br />
<strong>Keywords:</strong> Erdős-Ginzburg-Ziv Theorem, Zero-Sum Sequences, Davenport Constant, Chevalley-Warning Theorem, Cauchy-Davenport Theorem, Kemnitz's Conjecture, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Ginzburg-Ziv Theorem on Zero-Sum Sequences: A Detailed Treatise on Combinatorial Zero-Sums, Chevalley-Warning Reductions, the Davenport Constant, and Certified Proofs**

The Erdős-Ginzburg-Ziv (EGZ) theorem (Problem #06 in Paul Erdős' problem collection, 1961) is a seminal milestone in additive number theory, finite group theory, and zero-sum Ramsey theory. The theorem establishes that every sequence of $2n - 1$ integers contains a subsequence of length exactly $n$ whose sum is divisible by $n$: $\forall a_1, \dots, a_{2n-1} \in \mathbb{Z}, \exists I \subseteq \{1, \dots, 2n-1\}, |I| = n \text{ and } \sum_{i \in I} a_i \equiv 0 \pmod n$.

### Key Mathematical Results & Contributions:
- **Strict Sharpness Analysis:** Full non-elliptical proof that the multiset of $n - 1$ zeros and $n - 1$ ones of length $2n - 2$ contains no $n$-term subsequence summing to $0 \pmod n$.
- **The Chevalley-Warning Polynomial Proof for Primes:** Rigorous reduction to a system of two degree $p-1$ polynomials in $2p-1$ variables over $\mathbb{F}_p$.
- **Multiplicative Composite Induction:** Step-by-step inductive lift proving that if EGZ holds for $a$ and $b$, it unconditionally holds for $n = ab$.
- **Higher-Dimensional Generalizations:** Survey of the Davenport constant and Christian Reiher's (2007) resolution of Kemnitz's conjecture on $\mathbb{Z}_p^2$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosGinzburgZiv.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosGinzburgZiv.lean)).

* **MSC (2020)**: 11B75, 11P70, 05D10, 68V20, 20K01
* **Keywords**: Erdős-Ginzburg-Ziv Theorem, Zero-Sum Sequences, Davenport Constant, Chevalley-Warning Theorem, Cauchy-Davenport Theorem, Kemnitz's Conjecture, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
