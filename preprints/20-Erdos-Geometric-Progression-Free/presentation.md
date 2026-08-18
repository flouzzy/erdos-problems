# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on Geometric Progression-Free Sets`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Geometric Progression Problem, 3-GP-Free Sets, Multiplicative Combinatorics, Rankin's Constant, Square-Free Decompositions, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B75, 05D10, 11N37, 68V20, 11B05`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on Geometric Progression-Free Sets: A Detailed Treatise on Multiplicative Ramsey Theory, Rankin's Greedy Density, McNew's Analytic Upper Bounds, and Certified Proofs</strong></p>

<p>The Erdős geometric progression problem (Problem #20 in Paul Erdős' problem collection, 1961) is a central question at the interface of multiplicative number theory, Ramsey theory, and extremal combinatorics. A subset of integers $A \subseteq \{1, \dots, n\}$ is called 3-term geometric progression-free (3-GP-free) if it contains no three distinct integers $a, b, c \in A$ satisfying $b^2 = ac$. Unlike arithmetic progressions, where Szemerédi's theorem forces $AP_k$-free sets to have asymptotic density zero, 3-GP-free sets achieve positive asymptotic density. In 1961, R. A. Rankin constructed a greedy 3-GP-free set achieving density $\gamma \approx 0.71974$. For integer common ratios, Beiglböck et al. (2010) proved the greedy set achieves density $\approx 0.816$, and Nathan McNew (2015) established the analytic upper bound $\bar{d}(A) \le 0.8184$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Multiplicative Fiber Decomposition:</strong> Rigorous partitioning of positive integers into square-free fibers $n = q \prod p_i^{\alpha_i}$ and transformation of geometric progressions into additive progression constraints on exponent lattices.</li>
  <li><strong>Rankin's Density Analysis:</strong> Detailed derivation of Rankin's greedy density constant $\gamma \approx 0.71974$ via base-3 3-AP-free exponent avoidance.</li>
  <li><strong>McNew's Analytic Upper Bounds:</strong> Comprehensive exposition of McNew's (2015) bound $\bar{d}(A) \le 0.8184$ for integer ratio progressions.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> 3-GP-free predicates, small cardinality properties ($|A| \le 2$), the certified 8-element subset $\{1, 2, 3, 5, 6, 7, 8, 10\}$ in $\{1, \dots, 10\}$, and formal obstruction proofs for $(1, 2, 4)$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosGeometricProgressionFree.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B75, 05D10, 11N37, 68V20, 11B05<br />
<strong>Keywords:</strong> Erdős Geometric Progression Problem, 3-GP-Free Sets, Multiplicative Combinatorics, Rankin's Constant, Square-Free Decompositions, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on Geometric Progression-Free Sets: A Detailed Treatise on Multiplicative Ramsey Theory, Rankin's Greedy Density, McNew's Analytic Upper Bounds, and Certified Proofs**

The Erdős geometric progression problem (Problem #20 in Paul Erdős' problem collection, 1961) is a central question at the interface of multiplicative number theory, Ramsey theory, and extremal combinatorics. A subset of integers $A \subseteq \{1, \dots, n\}$ is called 3-term geometric progression-free (3-GP-free) if it contains no three distinct integers $a, b, c \in A$ satisfying $b^2 = ac$.

### Key Mathematical Results & Contributions:
- **Multiplicative Fiber Decomposition:** Rigorous partitioning into square-free fibers $n = q \prod p_i^{\alpha_i}$ and transformation of geometric progressions into additive progression constraints.
- **Rankin's Density Analysis:** Detailed derivation of Rankin's greedy density constant $\gamma \approx 0.71974$.
- **McNew's Analytic Upper Bounds:** Comprehensive exposition of McNew's (2015) bound $\bar{d}(A) \le 0.8184$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosGeometricProgressionFree.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosGeometricProgressionFree.lean)).

* **MSC (2020)**: 11B75, 05D10, 11N37, 68V20, 11B05
* **Keywords**: Erdős Geometric Progression Problem, 3-GP-Free Sets, Multiplicative Combinatorics, Rankin's Constant, Square-Free Decompositions, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
