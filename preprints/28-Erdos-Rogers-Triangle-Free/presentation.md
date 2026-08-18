# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Rogers Problem on Triangle-Free Induced Subgraphs`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Rogers Problem, Extremal Graph Theory, Ramsey Theory, Triangle-Free Induced Subgraphs, K_4-Free Graphs, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05C35, 05C55, 05D10, 68V20, 05C69`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Rogers Problem on Triangle-Free Induced Subgraphs: A Detailed Treatise on $K_4$-Free Graph Structures, Ramsey Multi-Partite Bounds, the Dudek-Retter-Rödl-Sudakov Scaling, and Certified Proofs</strong></p>

<p>The Erdős-Rogers problem (Problem #28 in Paul Erdős' problem collection, 1962) is a celebrated question in extremal graph theory and generalized Ramsey theory. Let $G = (V, E)$ be a finite simple graph on $n$ vertices containing no 4-clique $K_4$ ($\omega(G) < 4$). The Erdős-Rogers problem investigates the minimum over all $n$-vertex $K_4$-free graphs of the maximum size of a triangle-free ($K_3$-free) induced subgraph: $f_{4, 3}(n) \coloneqq \min \{ \max \{ |S| \mid S \subseteq V, G[S] \text{ is } K_3\text{-free} \} \mid |V| = n, G \text{ is } K_4\text{-free} \}$. In 1962, Paul Erdős and C. A. Rogers proved the upper bound $f_{4, 3}(n) = O(n^{1/2} (\log n)^{1/2})$. In 2014, Andrzej Dudek, Tom Retter, and Vojtěch Rödl, and independently Benny Sudakov, established the definitive tight asymptotic scaling: $f_{4, 3}(n) = \Theta(\sqrt{n \log n})$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Foundational Erdős-Rogers Setup:</strong> Rigorous definition of generalized Ramsey-type functions $f_{s, t}(n)$, clique bounds, and the reduction from $K_4$-freeness to triangle-free neighborhoods.</li>
  <li><strong>Neighborhood &amp; Independence Counting:</strong> Step-by-step non-elliptical proof that for any vertex $v$, $G[N(v)]$ is $K_3$-free, and applying Caro-Wei/Turán bounds to derive the $\Omega(\sqrt{n \log n})$ lower bound.</li>
  <li><strong>The Dudek-Retter-Rödl &amp; Sudakov Tight Scaling:</strong> Exposition of the matching upper and lower bounds establishing $f_{4, 3}(n) = \Theta(\sqrt{n \log n})$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Graph clique predicates, proof that $K_3$-free graphs are unconditionally $K_4$-free, and machine-checked proof that independent sets are triangle-free are certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosRogersTriangleFree.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05C35, 05C55, 05D10, 68V20, 05C69<br />
<strong>Keywords:</strong> Erdős-Rogers Problem, Extremal Graph Theory, Ramsey Theory, Triangle-Free Induced Subgraphs, K_4-Free Graphs, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Rogers Problem on Triangle-Free Induced Subgraphs: A Detailed Treatise on $K_4$-Free Graph Structures, Ramsey Multi-Partite Bounds, the Dudek-Retter-Rödl-Sudakov Scaling, and Certified Proofs**

The Erdős-Rogers problem (Problem #28 in Paul Erdős' problem collection, 1962) is a celebrated question in extremal graph theory and generalized Ramsey theory. Let $G = (V, E)$ be a finite simple graph on $n$ vertices containing no 4-clique $K_4$ ($\omega(G) < 4$).

### Key Mathematical Results & Contributions:
- **Foundational Erdős-Rogers Setup:** Rigorous definition of generalized Ramsey-type functions $f_{s, t}(n)$.
- **Neighborhood & Independence Counting:** Step-by-step non-elliptical proof that neighborhoods in $K_4$-free graphs are $K_3$-free.
- **The Dudek-Retter-Rödl & Sudakov Tight Scaling:** Exposition of the matching upper and lower bounds establishing $f_{4, 3}(n) = \Theta(\sqrt{n \log n})$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosRogersTriangleFree.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosRogersTriangleFree.lean)).

* **MSC (2020)**: 05C35, 05C55, 05D10, 68V20, 05C69
* **Keywords**: Erdős-Rogers Problem, Extremal Graph Theory, Ramsey Theory, Triangle-Free Induced Subgraphs, K_4-Free Graphs, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
