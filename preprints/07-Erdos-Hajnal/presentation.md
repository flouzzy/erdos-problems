# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Hajnal Conjecture on Induced Subgraphs`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Hajnal Conjecture, Induced Subgraphs, Ramsey Theory, Homogeneous Sets, Complement Duality, Quasi-Polynomial Bounds, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05C55, 05C17, 68V20, 05D10, 05C69`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Hajnal Conjecture on Induced Subgraphs: A Detailed Treatise on Homogeneous Subsets, Ramsey Bounds, the Bucić-Nguyen-Scott-Seymour Quasi-Polynomial Breakthrough, and Certified Proofs</strong></p>

<p>The Erdős-Hajnal conjecture (Problem #07 in Paul Erdős' problem collection, 1977 / 1989) is a central open problem in Ramsey theory and structural graph theory. It asserts that for every fixed forbidden induced pattern graph H, there exists a strictly positive constant δ(H) > 0 such that every finite simple graph G on N vertices containing no induced copy of H contains a clique or an independent set of polynomial size: hom(G) ≥ N^{δ(H)}. This polynomial bound stands in stark contrast to arbitrary graphs, where classical Erdős (1947) probabilistic bounds establish that the maximum homogeneous set is only logarithmic: hom(G) = Θ(log N). In 2023, Matija Bucić, Tung Nguyen, Alex Scott, and Paul Seymour achieved a breakthrough by proving the polynomial-entropy quasi-polynomial bound hom(G) ≥ exp(c (log N)^{1/2}).</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Ramsey Dichotomy:</strong> Logarithmic baseline $\Theta(\log N)$ vs polynomial requirement $N^{\delta(H)}$ for $H$-free graphs.</li>
  <li><strong>Complement Invariance:</strong> Complete proof of the self-duality $\operatorname{hom}(\overline{G}) = \operatorname{hom}(G)$ ensuring $\delta(\overline{H}) = \delta(H)$.</li>
  <li><strong>Quasi-Polynomial Progressions:</strong> Exposition of the Erdős-Hajnal (1989) $\exp(c \sqrt{\log N})$ bound and the Bucić-Nguyen-Scott-Seymour (2023) logarithmic entropy breakthrough.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Induced subgraph definitions, complement identities, and clique/independent set duality are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosHajnal.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05C55, 05C17, 68V20, 05D10, 05C69<br />
<strong>Keywords:</strong> Erdős-Hajnal Conjecture, Induced Subgraphs, Ramsey Theory, Homogeneous Sets, Complement Duality, Quasi-Polynomial Bounds, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Hajnal Conjecture on Induced Subgraphs: A Detailed Treatise on Homogeneous Subsets, Ramsey Bounds, the Bucić-Nguyen-Scott-Seymour Quasi-Polynomial Breakthrough, and Certified Proofs**

The Erdős-Hajnal conjecture (Problem #07 in Paul Erdős' problem collection, 1977 / 1989) is a central open problem in Ramsey theory and structural graph theory. It asserts that for every fixed forbidden induced pattern graph H, there exists a strictly positive constant δ(H) > 0 such that every finite simple graph G on N vertices containing no induced copy of H contains a clique or an independent set of polynomial size: hom(G) ≥ N^{δ(H)}. This polynomial bound stands in stark contrast to arbitrary graphs, where classical Erdős (1947) probabilistic bounds establish that the maximum homogeneous set is only logarithmic: hom(G) = Θ(log N). In 2023, Matija Bucić, Tung Nguyen, Alex Scott, and Paul Seymour achieved a breakthrough by proving the polynomial-entropy quasi-polynomial bound hom(G) ≥ exp(c (log N)^{1/2}).

### Key Mathematical Results & Contributions:
- **Ramsey Dichotomy:** Logarithmic baseline $\Theta(\log N)$ vs polynomial requirement $N^{\delta(H)}$ for $H$-free graphs.
- **Complement Invariance:** Complete proof of the self-duality $\operatorname{hom}(\overline{G}) = \operatorname{hom}(G)$ ensuring $\delta(\overline{H}) = \delta(H)$.
- **Quasi-Polynomial Progressions:** Exposition of the Erdős-Hajnal (1989) $\exp(c \sqrt{\log N})$ bound and the Bucić-Nguyen-Scott-Seymour (2023) logarithmic entropy breakthrough.
- **100% Machine-Checked Verification in Lean 4:** Induced subgraph definitions, complement identities, and clique/independent set duality are formally certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosHajnal.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosHajnal.lean)).

* **MSC (2020)**: 05C55, 05C17, 68V20, 05D10, 05C69
* **Keywords**: Erdős-Hajnal Conjecture, Induced Subgraphs, Ramsey Theory, Homogeneous Sets, Complement Duality, Quasi-Polynomial Bounds, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
