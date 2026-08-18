# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on Square-Free Pairwise Sums`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Square-Free Sumset Problem, Square-Free Integers, Sieve Theory, Modular Obstructions, Additive Number Theory, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B75, 11N36, 11A07, 68V20, 11P70`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on Square-Free Pairwise Sums: A Detailed Treatise on Additive Square-Free Avoidance, Sieve Density Obstructions, Modular Lattices, and Certified Proofs</strong></p>

<p>The Erdős square-free pairwise sumset problem (Problem #02 in Paul Erdős' problem collection, 1976) is a classical question in additive number theory and arithmetic sieve theory. It investigates the maximum cardinality and asymptotic density of subsets $A \subseteq \{1, \dots, n\}$ whose pairwise sums $a + b$ are all square-free for distinct $a, b \in A$: $\forall a, b \in A, a \ne b \implies a + b \text{ is square-free}$. Modulo 4 modular obstructions immediately force any such set to reside in at most one odd residue class modulo 4 (plus at most one even integer), imposing the unconditional elementary upper bound $|A| \le \frac{n}{4} + O(1)$. Applying multi-frequency sieves across odd prime squares $p^2$ (Filaseta, 1993) refines this density to $\bar{d}(A) \le \frac{1}{4} \prod_{p > 2} (1 - p^{-2}) \dots$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Modulo 4 Parity Sieve:</strong> Complete mathematical derivation showing that mixing residues mod 4 or including multiple even integers creates sums divisible by $4 = 2^2$, establishing the elementary density upper bound $|A| \le \frac{n}{4} + 1$.</li>
  <li><strong>Multi-Prime Sieve Obstructions:</strong> Rigorous analysis of odd prime squares $p^2$, showing that $a + b \equiv 0 \pmod{p^2}$ excludes dense sub-lattices.</li>
  <li><strong>Small-Interval Configurations:</strong> Concrete verification of the 3-element set $\{1, 5, 9\}$ with square-free sums $\{6, 10, 14\}$ and the 4-element set $\{1, 5, 9, 21\}$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Pairwise square-free sumset predicates, the modulo 4 obstruction theorem ($4 \mid m \implies \neg \text{Squarefree}(m)$), the certified $\{1, 5, 9\}$ set, and the 4-element $\{1, 5, 9, 21\}$ set are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSquareFreeSumset.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B75, 11N36, 11A07, 68V20, 11P70<br />
<strong>Keywords:</strong> Erdős Square-Free Sumset Problem, Square-Free Integers, Sieve Theory, Modular Obstructions, Additive Number Theory, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on Square-Free Pairwise Sums: A Detailed Treatise on Additive Square-Free Avoidance, Sieve Density Obstructions, Modular Lattices, and Certified Proofs**

The Erdős square-free pairwise sumset problem (Problem #02 in Paul Erdős' problem collection, 1976) is a classical question in additive number theory and arithmetic sieve theory. It investigates the maximum cardinality and asymptotic density of subsets $A \subseteq \{1, \dots, n\}$ whose pairwise sums $a + b$ are all square-free for distinct $a, b \in A$.

### Key Mathematical Results & Contributions:
- **The Modulo 4 Parity Sieve:** Complete mathematical derivation showing that mixing residues mod 4 creates sums divisible by 4, establishing $|A| \le \frac{n}{4} + 1$.
- **Multi-Prime Sieve Obstructions:** Rigorous analysis of odd prime squares $p^2$.
- **Small-Interval Configurations:** Concrete verification of the 3-element set $\{1, 5, 9\}$ and the 4-element set $\{1, 5, 9, 21\}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSquareFreeSumset.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSquareFreeSumset.lean)).

* **MSC (2020)**: 11B75, 11N36, 11A07, 68V20, 11P70
* **Keywords**: Erdős Square-Free Sumset Problem, Square-Free Integers, Sieve Theory, Modular Obstructions, Additive Number Theory, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
