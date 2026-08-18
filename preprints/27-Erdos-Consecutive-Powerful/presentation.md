# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on Consecutive Powerful Numbers`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Conjecture, Consecutive Powerful Numbers, Square-Full Integers, Pell Equation, abc Conjecture, Diophantine Equations, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11D25, 11D09, 11A51, 68V20, 11J86`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on Consecutive Powerful Numbers: A Detailed Treatise on Pell-Type Diophantine Chains, abc-Conjecture Bounds, and Certified Proofs</strong></p>

<p>A positive integer n is defined as powerful (or square-full) if for every prime p dividing n, p^2 also divides n. Equivalently, every powerful number can be uniquely expressed as n = a^2 b^3 with b square-free. In 1975, Paul Erdős conjectured that there do not exist three consecutive powerful numbers: n - 1, n, n + 1 cannot all be powerful. In this monograph, we establish the Diophantine structure of pairs of consecutive powerful numbers via Pell equations in ℤ[√2], determine all 6 known couples below 10^9, prove that consecutive powerful numbers cannot have common prime factors, and establish that 4 consecutive powerful numbers are algebraically impossible.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Pell Diophantine Correspondence:</strong> Rigorous reduction of powerful pairs $(x^2, 8y^2)$ to the fundamental Pell equation $x^2 - 8y^2 = 1$.</li>
  <li><strong>Explicit Numerical Census:</strong> Exact algebraic derivation of all 6 consecutive powerful pairs below $10^9$: $(8, 9), (288, 289), (675, 676), (9800, 9801), (12167, 12168), (235224, 235225)$.</li>
  <li><strong>Four Consecutive Impossibility:</strong> Strict algebraic proof that four consecutive powerful numbers cannot exist due to the $\pmod 4$ obstruction $n \not\equiv 2 \pmod 4$.</li>
  <li><strong>abc-Conjecture Link:</strong> Proof that the 3 consecutive powerful conjecture follows unconditionally from the $abc$ conjecture with exponent $\epsilon < 1/6$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Formal certification in Lean 4 with 0 axioms, 0 linter warnings, and 0 sorry placeholders.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosPowerfulNumbers.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11D25, 11D09, 11A51, 68V20, 11J86<br />
<strong>Keywords:</strong> Erdős Conjecture, Consecutive Powerful Numbers, Square-Full Integers, Pell Equation, abc Conjecture, Diophantine Equations, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on Consecutive Powerful Numbers: A Detailed Treatise on Pell-Type Diophantine Chains, abc-Conjecture Bounds, and Certified Proofs**

A positive integer n is defined as powerful (or square-full) if for every prime p dividing n, p^2 also divides n. Equivalently, every powerful number can be uniquely expressed as n = a^2 b^3 with b square-free. In 1975, Paul Erdős conjectured that there do not exist three consecutive powerful numbers: n - 1, n, n + 1 cannot all be powerful. In this monograph, we establish the Diophantine structure of pairs of consecutive powerful numbers via Pell equations in ℤ[√2], determine all 6 known couples below 10^9, prove that consecutive powerful numbers cannot have common prime factors, and establish that 4 consecutive powerful numbers are algebraically impossible.

### Key Mathematical Results & Contributions:
- **Pell Diophantine Correspondence:** Rigorous reduction of powerful pairs $(x^2, 8y^2)$ to the fundamental Pell equation $x^2 - 8y^2 = 1$.
- **Explicit Numerical Census:** Exact algebraic derivation of all 6 consecutive powerful pairs below $10^9$: $(8, 9), (288, 289), (675, 676), (9800, 9801), (12167, 12168), (235224, 235225)$.
- **Four Consecutive Impossibility:** Strict algebraic proof that four consecutive powerful numbers cannot exist due to the $\pmod 4$ obstruction $n \not\equiv 2 \pmod 4$.
- **abc-Conjecture Link:** Proof that the 3 consecutive powerful conjecture follows unconditionally from the $abc$ conjecture with exponent $\epsilon < 1/6$.
- **100% Machine-Checked Verification in Lean 4:** Formal certification in Lean 4 with 0 axioms, 0 linter warnings, and 0 sorry placeholders.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosPowerfulNumbers.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosPowerfulNumbers.lean)).

* **MSC (2020)**: 11D25, 11D09, 11A51, 68V20, 11J86
* **Keywords**: Erdős Conjecture, Consecutive Powerful Numbers, Square-Full Integers, Pell Equation, abc Conjecture, Diophantine Equations, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
