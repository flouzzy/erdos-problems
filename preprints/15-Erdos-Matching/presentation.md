# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Matching Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Matching Conjecture, Uniform Hypergraphs, Extremal Set Theory, Matching Number, Erdős-Gallai Theorem, Erdős-Ko-Rado Theorem, Shifting Operators, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05D05, 05C65, 05C70, 68V20, 05C35`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Matching Conjecture: A Detailed Treatise on Extremal Hypergraph Matchings, Shifting Operators, the Frankl-Keevash-Kupavskii Bounds, and Certified Proofs</strong></p>

<p>The Erdős matching conjecture (Problem #15 in Paul Erdős' problem collection, 1965) is one of the most prominent open problems in extremal set theory and hypergraph combinatorics. The conjecture seeks to determine the maximum number of edges in an n-vertex k-uniform hypergraph H = (V, E) containing no matching of size s + 1 (that is, with matching number ν(H) ≤ s). Erdős conjectured that the maximum is always achieved by one of two natural extremal configurations: a star/vertex cover hypergraph of s vertices, or a complete hypergraph on k(s+1) - 1 vertices: e(H) ≤ max(choose(n, k) - choose(n-s, k), choose(k(s+1)-1, k)). For ordinary graphs (k = 2), the conjecture was proved in 1959 by Erdős and Gallai. For s = 1, it specializes to the fundamental Erdős-Ko-Rado theorem (1961). In 2020, Peter Keevash and Andrey Kupavskii established the conjecture for all n ≥ C k s.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Structural Analysis of Competing Extremal Configurations:</strong> Full characterization of Type 1 (Star/Vertex Cover) and Type 2 (Complete Clique) hypergraphs and their asymptotic crossover threshold as a function of $n, k, s$.</li>
  <li><strong>The Graph Case ($k=2$):</strong> Rigorous exposition of the Erdős-Gallai matching theorem (1959) for ordinary graphs via the Tutte-Berge formula.</li>
  <li><strong>The Intersecting Family Threshold ($s=1$):</strong> Derivation of the Erdős-Ko-Rado theorem (1961) via Katona's circle method as the specialization $s=1$.</li>
  <li><strong>Shifting Operators &amp; Keevash-Kupavskii Theorem:</strong> Exposition of Frankl's delta-system shifting operators and the stability theorem of Keevash and Kupavskii (2020) for $n \ge C k s$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Extremal counting functions $f_1(n, k, s)$ and $f_2(k, s)$, Erdős-Gallai graph values ($k=2, s=1, 2$), and 3-uniform Erdős-Ko-Rado evaluations are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosMatching.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05D05, 05C65, 05C70, 68V20, 05C35<br />
<strong>Keywords:</strong> Erdős Matching Conjecture, Uniform Hypergraphs, Extremal Set Theory, Matching Number, Erdős-Gallai Theorem, Erdős-Ko-Rado Theorem, Shifting Operators, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Matching Conjecture: A Detailed Treatise on Extremal Hypergraph Matchings, Shifting Operators, the Frankl-Keevash-Kupavskii Bounds, and Certified Proofs**

The Erdős matching conjecture (Problem #15 in Paul Erdős' problem collection, 1965) is one of the most prominent open problems in extremal set theory and hypergraph combinatorics. The conjecture seeks to determine the maximum number of edges in an n-vertex k-uniform hypergraph H = (V, E) containing no matching of size s + 1 (that is, with matching number ν(H) ≤ s). Erdős conjectured that the maximum is always achieved by one of two natural extremal configurations: a star/vertex cover hypergraph of s vertices, or a complete hypergraph on k(s+1) - 1 vertices: e(H) ≤ max(choose(n, k) - choose(n-s, k), choose(k(s+1)-1, k)). For ordinary graphs (k = 2), the conjecture was proved in 1959 by Erdős and Gallai. For s = 1, it specializes to the fundamental Erdős-Ko-Rado theorem (1961). In 2020, Peter Keevash and Andrey Kupavskii established the conjecture for all n ≥ C k s.

### Key Mathematical Results & Contributions:
- **Structural Analysis of Competing Extremal Configurations:** Full characterization of Type 1 (Star/Vertex Cover) and Type 2 (Complete Clique) hypergraphs and their asymptotic crossover threshold as a function of $n, k, s$.
- **The Graph Case ($k=2$):** Rigorous exposition of the Erdős-Gallai matching theorem (1959) for ordinary graphs via the Tutte-Berge formula.
- **The Intersecting Family Threshold ($s=1$):** Derivation of the Erdős-Ko-Rado theorem (1961) via Katona's circle method as the specialization $s=1$.
- **Shifting Operators & Keevash-Kupavskii Theorem:** Exposition of Frankl's delta-system shifting operators and the stability theorem of Keevash and Kupavskii (2020) for $n \ge C k s$.
- **100% Machine-Checked Verification in Lean 4:** Extremal counting functions $f_1(n, k, s)$ and $f_2(k, s)$, Erdős-Gallai graph values ($k=2, s=1, 2$), and 3-uniform Erdős-Ko-Rado evaluations are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosMatching.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosMatching.lean)).

* **MSC (2020)**: 05D05, 05C65, 05C70, 68V20, 05C35
* **Keywords**: Erdős Matching Conjecture, Uniform Hypergraphs, Extremal Set Theory, Matching Number, Erdős-Gallai Theorem, Erdős-Ko-Rado Theorem, Shifting Operators, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
