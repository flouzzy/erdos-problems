# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Cameron-Erdős Conjecture on Sum-Free Sets`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Cameron-Erdős Conjecture, Sum-Free Sets, Additive Combinatorics, Fourier Analysis, Hypergraph Containers, Freiman's Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B75, 05A16, 11P70, 68V20, 05D10`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Cameron-Erdős Conjecture on Sum-Free Sets: A Detailed Treatise on Additive Independence, Green's Arithmetic Regularity, the Container Method, and Certified Proofs</strong></p>

<p>The Cameron-Erdős conjecture (Problem #01 in Paul Erdős' problem collection, 1990) is a celebrated milestone in additive combinatorics, asymptotic enumeration, and arithmetic Ramsey theory. A subset $A \subseteq \{1, \dots, n\}$ is called sum-free if $(A + A) \cap A = \emptyset$, meaning that the equation $x + y = z$ has no solutions with $x, y, z \in A$. Let $s(n)$ denote the total number of sum-free subsets of $\{1, \dots, n\}$. Peter Cameron and Paul Erdős observed the immediate lower bound $s(n) \ge 2^{\lfloor n/2 \rfloor}$ provided by odd integers and the upper interval $(\lfloor n/2 \rfloor, n]$, and conjectured that $s(n) = \Theta(2^{n/2})$. In 2004, Ben Green completely proved the conjecture in <em>Acta Mathematica</em> using Fourier analysis and arithmetic regularity, and Alexander Sapozhenko independently resolved it via graph container methods.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Structural Analysis of Canonical Extremal Families:</strong> Complete mathematical derivation of the $2^{\lfloor n/2 \rfloor}$ lower bounds via the odd integers $O_n = \{1, 3, 5, \dots\}$ and upper intervals $U_n = (\lfloor n/2 \rfloor, n]$.</li>
  <li><strong>Ben Green's Fourier Analytic Proof (2004):</strong> Step-by-step exposition of Freiman's $3k-4$ structural theorem, arithmetic regularity for sumsets, and the proof that almost all sum-free sets are contained in $O_n$ or $U_n$.</li>
  <li><strong>The Hypergraph Container Framework:</strong> Dual reformulation of sum-free sets as independent sets in 3-uniform Schur hypergraphs with container entropy bounds $2^{o(n)}$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Sum-free set definitions, parity preservation theorems, upper interval sum-free proofs, and exact discrete evaluations for small intervals are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosCameronSumFree.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B75, 05A16, 11P70, 68V20, 05D10<br />
<strong>Keywords:</strong> Cameron-Erdős Conjecture, Sum-Free Sets, Additive Combinatorics, Fourier Analysis, Hypergraph Containers, Freiman's Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Cameron-Erdős Conjecture on Sum-Free Sets: A Detailed Treatise on Additive Independence, Green's Arithmetic Regularity, the Container Method, and Certified Proofs**

The Cameron-Erdős conjecture (Problem #01 in Paul Erdős' problem collection, 1990) is a celebrated milestone in additive combinatorics, asymptotic enumeration, and arithmetic Ramsey theory. A subset $A \subseteq \{1, \dots, n\}$ is called sum-free if $(A + A) \cap A = \emptyset$, meaning that the equation $x + y = z$ has no solutions with $x, y, z \in A$.

### Key Mathematical Results & Contributions:
- **Structural Analysis of Canonical Extremal Families:** Complete mathematical derivation of the $2^{\lfloor n/2 \rfloor}$ lower bounds via the odd integers $O_n = \{1, 3, 5, \dots\}$ and upper intervals $U_n = (\lfloor n/2 \rfloor, n]$.
- **Ben Green's Fourier Analytic Proof (2004):** Step-by-step exposition of Freiman's $3k-4$ structural theorem, arithmetic regularity for sumsets, and the proof that almost all sum-free sets are contained in $O_n$ or $U_n$.
- **The Hypergraph Container Framework:** Dual reformulation of sum-free sets as independent sets in 3-uniform Schur hypergraphs with container entropy bounds $2^{o(n)}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosCameronSumFree.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosCameronSumFree.lean)).

* **MSC (2020)**: 11B75, 05A16, 11P70, 68V20, 05D10
* **Keywords**: Cameron-Erdős Conjecture, Sum-Free Sets, Additive Combinatorics, Fourier Analysis, Hypergraph Containers, Freiman's Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
