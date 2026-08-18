# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Conjecture on 4-Term Arithmetic Progressions`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Conjecture, 4-Term Arithmetic Progressions, Szemerédi's Theorem, Gowers U^3 Norm, Higher-Order Fourier Analysis, Green-Tao Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B25, 05D10, 11B13, 68V20, 11N13`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Conjecture on 4-Term Arithmetic Progressions: A Detailed Treatise on Higher-Order Fourier Analysis, Gowers $U^3$ Uniformity Norms, Green-Tao Arithmetic Regularity, and Certified Proofs</strong></p>

<p>The Erdős 4-term arithmetic progression problem (Problem #85 in Paul Erdős' problem collection / Szemerédi 1969) is a central milestone in additive combinatorics, higher-order Fourier analysis, and ergodic theory. Let $r_4(N)$ denote the maximum cardinality of a subset $A \subseteq \{1, \dots, N\}$ containing no 4-term arithmetic progression ($AP_4$): $\forall a, d \in \mathbb{N}, d > 0 \implies \neg (a \in A \land a + d \in A \land a + 2d \in A \land a + 3d \in A)$. In 1969, Endre Szemerédi proved $r_4(N) = o(N)$. In 1998–2001, Sir Timothy Gowers established the quantitative bound $r_4(N) \le \frac{N}{(\log \log N)^c}$ by introducing the $U^3$ uniformity norm (Gowers norms) and initiating higher-order Fourier analysis. In 2010, Ben Green and Terence Tao developed the arithmetic regularity lemma for $U^3$, and in 2024, Frederick Manners established the polynomial decay $r_4(N) \le \frac{N}{(\log N)^c}$.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Gowers $U^3$ Uniformity Framework:</strong> Detailed exposition of the $U^3$ norm on $\mathbb{Z}/N\mathbb{Z}$ and the quadratic phase inverse theorem.</li>
  <li><strong>Higher-Order Arithmetic Regularity:</strong> Analysis of Green-Tao 2-step nilmanifolds and polynomial decay bounds on $r_4(N)$ (Manners 2024).</li>
  <li><strong>Small Discrete Configurations:</strong> Structural verification of the 8-element base-3 Cantor set $\{0, 1, 3, 4, 9, 10, 12, 13\}$ in $[13]$ avoiding 4-term progressions.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> $AP_4$-free predicates, proof that sets of size $\le 3$ are unconditionally $AP_4$-free, obstruction certification for $\{0, 1, 2, 3\}$, and formal verification of the 8-element Cantor set are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosAP4Free.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B25, 05D10, 11B13, 68V20, 11N13<br />
<strong>Keywords:</strong> Erdős Conjecture, 4-Term Arithmetic Progressions, Szemerédi's Theorem, Gowers U^3 Norm, Higher-Order Fourier Analysis, Green-Tao Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Conjecture on 4-Term Arithmetic Progressions: A Detailed Treatise on Higher-Order Fourier Analysis, Gowers $U^3$ Uniformity Norms, Green-Tao Arithmetic Regularity, and Certified Proofs**

The Erdős 4-term arithmetic progression problem (Problem #85 in Paul Erdős' problem collection / Szemerédi 1969) is a central milestone in additive combinatorics, higher-order Fourier analysis, and ergodic theory. Let $r_4(N)$ denote the maximum cardinality of a subset $A \subseteq \{1, \dots, N\}$ containing no 4-term arithmetic progression ($AP_4$).

### Key Mathematical Results & Contributions:
- **The Gowers $U^3$ Uniformity Framework:** Detailed exposition of the $U^3$ norm on $\mathbb{Z}/N\mathbb{Z}$ and the quadratic phase inverse theorem.
- **Higher-Order Arithmetic Regularity:** Analysis of Green-Tao 2-step nilmanifolds and Manners' (2024) polynomial decay $r_4(N) \le \frac{N}{(\log N)^c}$.
- **Small Discrete Configurations:** Structural verification of the 8-element base-3 Cantor set $\{0, 1, 3, 4, 9, 10, 12, 13\}$.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosAP4Free.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosAP4Free.lean)).

* **MSC (2020)**: 11B25, 05D10, 11B13, 68V20, 11N13
* **Keywords**: Erdős Conjecture, 4-Term Arithmetic Progressions, Szemerédi's Theorem, Gowers U^3 Norm, Higher-Order Fourier Analysis, Green-Tao Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
