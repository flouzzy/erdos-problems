# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Sprague-Erdős Theorem on Sums of Distinct Squares`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Sprague-Erdős Theorem, Sums of Distinct Squares, Additive Partitions, 128 Maximal Obstruction, Waring-Type Problems, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11P05, 11D85, 11E25, 68V20, 05A17`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Sprague-Erdős Theorem on Sums of Distinct Squares: A Detailed Treatise on Additive Integer Partitions into Distinct Squares, the 128 Maximal Obstruction, and Certified Proofs</strong></p>

<p>The Sprague-Erdős distinct square sums problem (Problem #91 in Paul Erdős' problem collection / Sprague 1948) is a foundational milestone in additive number theory and restricted partition theory. It investigates the representation of positive integers as sums of distinct positive squares: $n = \sum_{i=1}^k x_i^2$, $1 \le x_1 < x_2 < \dots < x_k$. In 1948, R. Sprague proved that every integer strictly greater than $128$ can be expressed as a sum of distinct positive squares, establishing that $128$ is the <em>exact maximum exception</em> across all positive integers. There exist exactly 31 unrepresentable positive integers, the largest of which is 128.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Sprague Threshold Theorem (1948):</strong> Complete proof of the representability of all integers $n \ge 129$ as sums of distinct squares.</li>
  <li><strong>The 31 Exceptional Integers Census:</strong> Exhaustive characterization and algebraic obstruction analysis of the 31 unrepresentable positive integers terminating at 128.</li>
  <li><strong>Explicit Boundary Decompositions:</strong> Exact verified representations for $129 = 10^2 + 5^2 + 2^2$, $130 = 9^2 + 7^2$, $131 = 9^2 + 7^2 + 1^2$, and $132 = 9^2 + 5^2 + 4^2 + 3^2 + 1^2$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Distinct square sum predicates, positivity proofs, and exact square sum identities for boundary values are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosDistinctSquareSums.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11P05, 11D85, 11E25, 68V20, 05A17<br />
<strong>Keywords:</strong> Sprague-Erdős Theorem, Sums of Distinct Squares, Additive Partitions, 128 Maximal Obstruction, Waring-Type Problems, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Sprague-Erdős Theorem on Sums of Distinct Squares: A Detailed Treatise on Additive Integer Partitions into Distinct Squares, the 128 Maximal Obstruction, and Certified Proofs**

The Sprague-Erdős distinct square sums problem (Problem #91 in Paul Erdős' problem collection / Sprague 1948) is a foundational milestone in additive number theory and restricted partition theory. It investigates the representation of positive integers as sums of distinct positive squares: $n = \sum_{i=1}^k x_i^2$.

### Key Mathematical Results & Contributions:
- **The Sprague Threshold Theorem (1948):** Proof of the representability of all integers $n \ge 129$.
- **The 31 Exceptional Integers Census:** Exhaustive characterization of the 31 unrepresentable positive integers terminating at 128.
- **Explicit Boundary Decompositions:** Exact representations for $129 = 10^2 + 5^2 + 2^2$, $130 = 9^2 + 7^2$, $131 = 9^2 + 7^2 + 1^2$, and $132 = 9^2 + 5^2 + 4^2 + 3^2 + 1^2$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosDistinctSquareSums.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosDistinctSquareSums.lean)).

* **MSC (2020)**: 11P05, 11D85, 11E25, 68V20, 05A17
* **Keywords**: Sprague-Erdős Theorem, Sums of Distinct Squares, Additive Partitions, 128 Maximal Obstruction, Waring-Type Problems, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
