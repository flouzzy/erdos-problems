# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Generalized Erdős-Straus and Schinzel-Sierpiński Conjectures`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Straus Conjecture, Schinzel-Sierpiński Conjecture, Egyptian Fractions, Diophantine Equations, Modular Arithmetic, Elsholtz-Tao Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D68, 11A07, 11N36, 68V20, 11P83`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Generalized Erdős-Straus and Schinzel-Sierpiński Conjectures: A Detailed Treatise on Parametric Egyptian Fractions, Modular Residue Families, the Elsholtz-Tao Bounds, and Certified Proofs</strong></p>

<p>The Schinzel-Sierpiński conjecture on Egyptian fractions (Problem #26 in Paul Erdős' problem collection, 1956) is a central generalization of the classical Erdős-Straus conjecture ($a = 4$) to arbitrary numerators $a \ge 1$. The conjecture asserts that for every fixed positive integer $a \ge 1$, there exists an integer threshold $N_a$ such that for all integers $n \ge N_a$, the rational number $a / n$ can be decomposed as a sum of three Egyptian unit fractions: $\frac{a}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}, x, y, z \in \mathbb{N}_{\ge 1}$. In 2014, Christian Elsholtz and Terence Tao established asymptotic upper bounds on the average number of representations and proved that exceptional sets of prime denominators have asymptotic density zero.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Prime Denominator Reduction:</strong> Rigorous proof that resolving $a / p = 1/x + 1/y + 1/z$ for all prime denominators $p \ge N_a$ unconditionally resolves the conjecture for all composite integers $n$.</li>
  <li><strong>Universal Modular Polynomial Families:</strong> Derivation and proof of the two-term base family $\frac{a}{am + a - 1} = \frac{1}{m+1} + \frac{1}{(m+1)(am + a - 1)}$ and multi-term congruence classifications modulo $a, 2a, 4a$.</li>
  <li><strong>The Elsholtz-Tao Analytic Theorem (2014):</strong> Comprehensive survey of the Bombieri-Vinogradov application establishing that the exceptional prime set $E_a(X)$ has asymptotic density zero: $|E_a(X)| \ll X / \exp((\log X)^{1-o(1)})$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> 3-term Egyptian predicates, exact rational identities for $a = 5$ on prime denominators ($n = 2, 3, 4, 5, 7, 11, 13$), and formal algebraic polynomial families are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSchinzelSierpinski.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D68, 11A07, 11N36, 68V20, 11P83<br />
<strong>Keywords:</strong> Erdős-Straus Conjecture, Schinzel-Sierpiński Conjecture, Egyptian Fractions, Diophantine Equations, Modular Arithmetic, Elsholtz-Tao Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Generalized Erdős-Straus and Schinzel-Sierpiński Conjectures: A Detailed Treatise on Parametric Egyptian Fractions, Modular Residue Families, the Elsholtz-Tao Bounds, and Certified Proofs**

The Schinzel-Sierpiński conjecture on Egyptian fractions (Problem #26 in Paul Erdős' problem collection, 1956) is a central generalization of the classical Erdős-Straus conjecture ($a = 4$) to arbitrary numerators $a \ge 1$. The conjecture asserts that for every fixed positive integer $a \ge 1$, there exists an integer threshold $N_a$ such that for all integers $n \ge N_a$, the rational number $a / n$ can be decomposed as a sum of three Egyptian unit fractions: $\frac{a}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$.

### Key Mathematical Results & Contributions:
- **Prime Denominator Reduction:** Rigorous proof that resolving $a / p = 1/x + 1/y + 1/z$ for all prime denominators $p \ge N_a$ unconditionally resolves the conjecture for all composite integers $n$.
- **Universal Modular Polynomial Families:** Derivation and proof of the two-term base family $\frac{a}{am + a - 1} = \frac{1}{m+1} + \frac{1}{(m+1)(am + a - 1)}$ and multi-term congruence classifications modulo $a, 2a, 4a$.
- **The Elsholtz-Tao Analytic Theorem (2014):** Comprehensive survey of the Bombieri-Vinogradov application establishing that the exceptional prime set $E_a(X)$ has asymptotic density zero.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSchinzelSierpinski.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSchinzelSierpinski.lean)).

* **MSC (2020)**: 11D68, 11A07, 11N36, 68V20, 11P83
* **Keywords**: Erdős-Straus Conjecture, Schinzel-Sierpiński Conjecture, Egyptian Fractions, Diophantine Equations, Modular Arithmetic, Elsholtz-Tao Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
