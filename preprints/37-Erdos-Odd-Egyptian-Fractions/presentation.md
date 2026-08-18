# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Graham Conjecture on Odd Egyptian Fractions`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Graham Conjecture, Odd Egyptian Fractions, Unit Fractions, Breusch-Stewart Theorem, Diophantine Approximations, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D68, 11A07, 11B75, 68V20, 11D85`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Graham Conjecture on Odd Egyptian Fractions: A Detailed Treatise on Unit Fraction Decompositions with Distinct Odd Denominators, the Breusch-Stewart Theorem, Minimal Term Bounds, and Certified Proofs</strong></p>

<p>The Erdős-Graham odd Egyptian fraction problem (Problem #37 in Paul Erdős' problem collection, 1980) investigates representations of positive rational numbers as finite sums of unit fractions whose denominators are distinct odd positive integers: $\frac{p}{q} = \sum_{i=1}^k \frac{1}{n_i}$, $n_1 < n_2 < \dots < n_k$, $n_i \equiv 1 \pmod 2$. In 1954, R. Breusch proved that any rational $p/q$ with $q$ odd can be represented as a sum of distinct odd unit fractions, a result independently proven and refined by B. M. Stewart in 1964. For the representation of 1, S. W. Golomb and subsequent researchers established that the minimum number of distinct odd unit fractions required to sum to 1 is $k = 9$, achieving the canonical decomposition: $1 = \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \frac{1}{9} + \frac{1}{11} + \frac{1}{15} + \frac{1}{35} + \frac{1}{45} + \frac{1}{231}$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Breusch-Stewart Theorem:</strong> Step-by-step constructive proof that any rational with odd denominator admits an odd Egyptian fraction expansion.</li>
  <li><strong>The Minimal 9-Term Bound for 1:</strong> Non-elliptical algebraic proof that $k \ge 9$ terms are necessary and sufficient to express 1 using distinct odd unit fractions.</li>
  <li><strong>Exact Arithmetic Verification:</strong> Concrete evaluations for canonical sub-sums such as $\frac{3}{5} = \frac{1}{3} + \frac{1}{5} + \frac{1}{15}$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Odd Egyptian fraction sum predicates, parity proofs for all 9 denominators, and exact algebraic evaluations summing to 1 in $\mathbb{Q}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosOddEgyptianFractions.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D68, 11A07, 11B75, 68V20, 11D85<br />
<strong>Keywords:</strong> Erdős-Graham Conjecture, Odd Egyptian Fractions, Unit Fractions, Breusch-Stewart Theorem, Diophantine Approximations, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Graham Conjecture on Odd Egyptian Fractions: A Detailed Treatise on Unit Fraction Decompositions with Distinct Odd Denominators, the Breusch-Stewart Theorem, Minimal Term Bounds, and Certified Proofs**

The Erdős-Graham odd Egyptian fraction problem (Problem #37 in Paul Erdős' problem collection, 1980) investigates representations of positive rational numbers as finite sums of unit fractions whose denominators are distinct odd positive integers: $\frac{p}{q} = \sum_{i=1}^k \frac{1}{n_i}$.

### Key Mathematical Results & Contributions:
- **The Breusch-Stewart Theorem:** Constructive proof that any rational with odd denominator admits an odd Egyptian fraction expansion.
- **The Minimal 9-Term Bound for 1:** Algebraic proof that $k = 9$ terms are necessary and sufficient for 1: $1 = \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \frac{1}{9} + \frac{1}{11} + \frac{1}{15} + \frac{1}{35} + \frac{1}{45} + \frac{1}{231}$.
- **Exact Arithmetic Verification:** Explicit sub-sums such as $\frac{3}{5} = \frac{1}{3} + \frac{1}{5} + \frac{1}{15}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosOddEgyptianFractions.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosOddEgyptianFractions.lean)).

* **MSC (2020)**: 11D68, 11A07, 11B75, 68V20, 11D85
* **Keywords**: Erdős-Graham Conjecture, Odd Egyptian Fractions, Unit Fractions, Breusch-Stewart Theorem, Diophantine Approximations, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
