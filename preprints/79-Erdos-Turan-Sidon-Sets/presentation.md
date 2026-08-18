# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Turán Sidon Sets Problem`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Turán Conjecture, Sidon Sets, B_2 Sequences, Additive Combinatorics, Singer Difference Sets, Finite Projective Planes, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B83, 05B10, 11B13, 68V20, 05B25`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Turán Sidon Sets Problem: A Detailed Treatise on $B_2$ Sequences, Singer Projective Difference Sets, Asymptotic Counting Bounds, and Certified Proofs</strong></p>

<p>The Erdős-Turán Sidon sets problem (Problem #79 in Paul Erdős' problem collection, 1941) is a seminal cornerstone of additive combinatorics, harmonic analysis, and finite geometry. A subset $A \subseteq \{1, \dots, n\}$ is called a Sidon set (or a $B_2$ set) if all pairwise sums $a + b$ with $a \le b$ are strictly distinct: $\forall a, b, c, d \in A, a + b = c + d \land a \le b \land c \le d \implies a = c \land b = d$. Let $F(n)$ denote the maximum cardinality of a Sidon set contained in $\{1, \dots, n\}$. In 1941, Paul Erdős and Pál Turán proved the classic upper bound $F(n) \le \sqrt{n} + n^{1/4} + 1$. In 1938, James Singer constructed perfect difference sets in finite projective planes $PG(2, q)$, providing matching lower bounds $F(n) \ge \sqrt{n} - O(n^{0.475})$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Foundational Sidon Set Setup:</strong> Precise algebraic definitions of $B_2$ sets, representation uniqueness, and difference set properties.</li>
  <li><strong>The Erdős-Turán Upper Bound (1941):</strong> Non-elliptical proof of $F(n) \le \sqrt{n} + n^{1/4} + 1$ via positive difference counting and Dirichlet shifts.</li>
  <li><strong>Singer Projective Difference Sets:</strong> Construction of perfect difference sets in $PG(2, q)$ establishing $|A| = q + 1 \sim \sqrt{n}$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Sidon set predicates, proof of singleton Sidon sets, and exhaustive certification of $\{1, 2, 4, 8\}$ and $\{0, 1, 3, 7\}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSidonSets.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B83, 05B10, 11B13, 68V20, 05B25<br />
<strong>Keywords:</strong> Erdős-Turán Conjecture, Sidon Sets, B_2 Sequences, Additive Combinatorics, Singer Difference Sets, Finite Projective Planes, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Turán Sidon Sets Problem: A Detailed Treatise on $B_2$ Sequences, Singer Projective Difference Sets, Asymptotic Counting Bounds, and Certified Proofs**

The Erdős-Turán Sidon sets problem (Problem #79 in Paul Erdős' problem collection, 1941) is a seminal cornerstone of additive combinatorics, harmonic analysis, and finite geometry. A subset $A \subseteq \{1, \dots, n\}$ is called a Sidon set (or a $B_2$ set) if all pairwise sums $a + b$ with $a \le b$ are strictly distinct.

### Key Mathematical Results & Contributions:
- **Foundational Sidon Set Setup:** Precise algebraic definitions of $B_2$ sets and difference set properties.
- **The Erdős-Turán Upper Bound (1941):** Proof of $F(n) \le \sqrt{n} + n^{1/4} + 1$.
- **Singer Projective Difference Sets:** Construction in $PG(2, q)$ establishing $|A| = q + 1 \sim \sqrt{n}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSidonSets.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSidonSets.lean)).

* **MSC (2020)**: 11B83, 05B10, 11B13, 68V20, 05B25
* **Keywords**: Erdős-Turán Conjecture, Sidon Sets, B_2 Sequences, Additive Combinatorics, Singer Difference Sets, Finite Projective Planes, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
