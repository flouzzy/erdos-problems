# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Divisor Gaps Conjecture and the Maier-Tenenbaum Theorem`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Divisor Gaps Conjecture, Maier-Tenenbaum Theorem, Hooley's Delta Function, Divisor Distribution, Probabilistic Number Theory, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11N37, 11N25, 11K65, 68V20, 11A25`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Divisor Gaps Conjecture and the Maier-Tenenbaum Theorem: A Detailed Treatise on Consecutive Divisor Ratios, Hooley's $\Delta$-Function, Probabilistic Number Theory, and Certified Proofs</strong></p>

<p>The Erdős divisor gaps problem (Problem #40 in Paul Erdős' problem collection, 1948) is a landmark question in probabilistic and multiplicative number theory. Let $1 = d_1 < d_2 < \dots < d_{\tau(n)} = n$ be the sequence of positive divisors of $n$. Paul Erdős conjectured that for almost all positive integers $n$ (on a set of asymptotic density 1), there exist two consecutive divisors that are exceptionally close: $\exists i \in \{1, \dots, \tau(n) - 1\}, d_{i+1} \le 2 d_i$. In 1984, Hendrik Maier and Gérald Tenenbaum proved this conjecture in their celebrated <em>Annals of Mathematics</em> paper by analyzing the distribution of divisors through Hooley's $\Delta$-function: $\Delta(n) \coloneqq \max_{u \in \mathbb{R}} \# \{ d \mid n \mid e^u < d \le e^{u+1} \}$. Maier and Tenenbaum established that $\Delta(n) \to \infty$ for almost all $n$, settling Erdős' conjecture in the affirmative.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Foundational Divisor Ratio Framework:</strong> Formal definition of ordered divisor sequences, proximity ratios $d_{i+1}/d_i$, and the concentration of divisors.</li>
  <li><strong>The Maier-Tenenbaum Theorem (Annals 1984):</strong> Detailed exposition of the analytic density proof establishing that almost all integers have divisors satisfying $d_{i+1} \le 2 d_i$.</li>
  <li><strong>Parametric Multiple-of-6 Constructions:</strong> Non-elliptical proof that every multiple of 6 ($n = 6k$) unconditionally satisfies the 2-close divisor property via $d_1 = 2k$ and $d_2 = 3k$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Divisor proximity predicates, certified verification on 6 and 12, and general parametric theorem for all multiples of 6 are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosDivisorGaps.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11N37, 11N25, 11K65, 68V20, 11A25<br />
<strong>Keywords:</strong> Erdős Divisor Gaps Conjecture, Maier-Tenenbaum Theorem, Hooley's Delta Function, Divisor Distribution, Probabilistic Number Theory, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Divisor Gaps Conjecture and the Maier-Tenenbaum Theorem: A Detailed Treatise on Consecutive Divisor Ratios, Hooley's $\Delta$-Function, Probabilistic Number Theory, and Certified Proofs**

The Erdős divisor gaps problem (Problem #40 in Paul Erdős' problem collection, 1948) is a landmark question in probabilistic and multiplicative number theory. Let $1 = d_1 < d_2 < \dots < d_{\tau(n)} = n$ be the sequence of positive divisors of $n$.

### Key Mathematical Results & Contributions:
- **Foundational Divisor Ratio Framework:** Ordered divisor sequences and proximity ratios $d_{i+1}/d_i$.
- **The Maier-Tenenbaum Theorem (Annals 1984):** Proof establishing that almost all integers have divisors satisfying $d_{i+1} \le 2 d_i$.
- **Parametric Multiple-of-6 Constructions:** Proof that every multiple of 6 ($n = 6k$) satisfies the 2-close divisor property via $d_1 = 2k$ and $d_2 = 3k$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosDivisorGaps.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosDivisorGaps.lean)).

* **MSC (2020)**: 11N37, 11N25, 11K65, 68V20, 11A25
* **Keywords**: Erdős Divisor Gaps Conjecture, Maier-Tenenbaum Theorem, Hooley's Delta Function, Divisor Distribution, Probabilistic Number Theory, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
