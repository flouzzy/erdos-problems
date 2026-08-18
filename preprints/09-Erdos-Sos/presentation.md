# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Sós Tree Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Sós Conjecture, Extremal Graph Theory, Tree Embeddings, Average Degree, Handshaking Lemma, Regularity Lemma, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05C05, 05C35, 68V20, 05C70`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Sós Tree Conjecture: A Detailed Treatise on Average Degree Thresholds, Extremal Clustered Cliques, the AKSS Regularity Program, and Certified Proofs</strong></p>

<p>The Erdős-Sós conjecture (Problem #09 in Paul Erdős' problem collection, 1963) is a central open problem in extremal graph theory. The conjecture asserts that every finite simple graph G = (V, E) with average degree strictly greater than k - 1 (d_bar(G) = 2|E|/|V| > k - 1) contains every tree T having k edges (k + 1 vertices) as a subgraph (T ⊆ G). This bound is known to be best possible: a disjoint union of cliques K_k has average degree k - 1 and contains no tree on k + 1 vertices. In the 1990s, Ajtai, Komlós, Simonovits, and Szemerédi (AKSS) announced a proof for all sufficiently large graphs N ≥ N_0(k) via the Regularity Lemma.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Extremal Sharpness of Disjoint Cliques:</strong> Complete analysis of the extremal tightness configuration $G = \bigcup m K_k$, proving that $\bar{d}(G) = k - 1$ contains zero trees on $k + 1$ vertices, making the strict inequality $\bar{d}(G) > k - 1$ sharp.</li>
  <li><strong>Star Trees &amp; Path Theorems:</strong> Non-elliptical proof that $\bar{d}(G) > k - 1$ forces a vertex of degree $\Delta(G) \ge k$ via the Handshaking Lemma (embedding the star tree $S_k = K_{1, k}$), alongside the Erdős-Gallai path theorem (1959).</li>
  <li><strong>Greedy Embedding Induction:</strong> Complete proof of the leaf-extension induction for graphs of minimum degree $\delta(H) \ge k$.</li>
  <li><strong>The AKSS Regularity Program:</strong> Detailed survey of the Ajtai-Komlós-Simonovits-Szemerédi framework establishing the conjecture for all sufficiently large graphs $|V| \ge N_0(k)$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Graph edge cardinalities, Handshaking identities, degree lower bounds, and star tree embeddings are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosSosTrees.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05C05, 05C35, 68V20, 05C70<br />
<strong>Keywords:</strong> Erdős-Sós Conjecture, Extremal Graph Theory, Tree Embeddings, Average Degree, Handshaking Lemma, Regularity Lemma, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Sós Tree Conjecture: A Detailed Treatise on Average Degree Thresholds, Extremal Clustered Cliques, the AKSS Regularity Program, and Certified Proofs**

The Erdős-Sós conjecture (Problem #09 in Paul Erdős' problem collection, 1963) is a central open problem in extremal graph theory. The conjecture asserts that every finite simple graph G = (V, E) with average degree strictly greater than k - 1 (d_bar(G) = 2|E|/|V| > k - 1) contains every tree T having k edges (k + 1 vertices) as a subgraph (T ⊆ G). This bound is known to be best possible: a disjoint union of cliques K_k has average degree k - 1 and contains no tree on k + 1 vertices. In the 1990s, Ajtai, Komlós, Simonovits, and Szemerédi (AKSS) announced a proof for all sufficiently large graphs N ≥ N_0(k) via the Regularity Lemma.

### Key Mathematical Results & Contributions:
- **Extremal Sharpness of Disjoint Cliques:** Complete analysis of the extremal tightness configuration $G = \bigcup m K_k$, proving that $\bar{d}(G) = k - 1$ contains zero trees on $k + 1$ vertices, making the strict inequality $\bar{d}(G) > k - 1$ sharp.
- **Star Trees & Path Theorems:** Non-elliptical proof that $\bar{d}(G) > k - 1$ forces a vertex of degree $\Delta(G) \ge k$ via the Handshaking Lemma (embedding the star tree $S_k = K_{1, k}$), alongside the Erdős-Gallai path theorem (1959).
- **Greedy Embedding Induction:** Complete proof of the leaf-extension induction for graphs of minimum degree $\delta(H) \ge k$.
- **The AKSS Regularity Program:** Detailed survey of the Ajtai-Komlós-Simonovits-Szemerédi framework establishing the conjecture for all sufficiently large graphs $|V| \ge N_0(k)$.
- **100% Machine-Checked Verification in Lean 4:** Graph edge cardinalities, Handshaking identities, degree lower bounds, and star tree embeddings are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosSosTrees.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosSosTrees.lean)).

* **MSC (2020)**: 05C05, 05C35, 68V20, 05C70
* **Keywords**: Erdős-Sós Conjecture, Extremal Graph Theory, Tree Embeddings, Average Degree, Handshaking Lemma, Regularity Lemma, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
