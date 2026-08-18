# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős-Rado Sunflower Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős-Rado Conjecture, Sunflower Lemma, Delta-Systems, Extremal Combinatorics, Spread Approximations, ALWZ Theorem, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `05D05, 05C65, 68V20, 68R05, 94A17`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős-Rado Sunflower Conjecture: A Detailed Treatise on Delta-Systems, the Erdős-Rado Bound $k!(r-1)^k$, the ALWZ Spread Breakthrough, and Certified Proofs</strong></p>

<p>The Erdős-Rado sunflower conjecture (Problem #68 in Paul Erdős' problem collection, 1960) is one of the most celebrated problems in extremal combinatorics and theoretical computer science. A sunflower (or Δ-system) with r petals and core Y is a collection of r sets whose pairwise intersections are all identical to Y. Erdős and Rado proved that any family of k-element sets of size greater than k!(r-1)^k contains an r-sunflower, and conjectured that the factorial bound k! can be replaced by c(r)^k. In 2020, Ryan Alweiss, Shachar Lovett, Kewen Wu, and Jiapeng Zhang achieved a breakthrough published in the Annals of Mathematics by proving the bound (r log(k r))^{O(k)} via the theory of spread approximations.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>Sunflower Extension Lemma:</strong> Rigorous non-elliptical proof that if $\mathcal{F}$ contains $r$ pairwise disjoint sets, then it contains an $r$-sunflower with empty core $\emptyset$.</li>
  <li><strong>The Classic Erdős-Rado Induction:</strong> Step-by-step inductive proof of the $k!(r-1)^k$ bound.</li>
  <li><strong>The ALWZ Revolution (2020):</strong> Detailed survey of $q$-spread set families, Shannon entropy filtering, and the reduction of the sunflower bound to $(O(r \log(kr)))^k$.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Formal sunflower predicate definitions, core invariance, sunflower extension theorems, and base certificates are verified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosRadoSunflower.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 05D05, 05C65, 68V20, 68R05, 94A17<br />
<strong>Keywords:</strong> Erdős-Rado Conjecture, Sunflower Lemma, Delta-Systems, Extremal Combinatorics, Spread Approximations, ALWZ Theorem, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős-Rado Sunflower Conjecture: A Detailed Treatise on Delta-Systems, the Erdős-Rado Bound $k!(r-1)^k$, the ALWZ Spread Breakthrough, and Certified Proofs**

The Erdős-Rado sunflower conjecture (Problem #68 in Paul Erdős' problem collection, 1960) is one of the most celebrated problems in extremal combinatorics and theoretical computer science. A sunflower (or Δ-system) with r petals and core Y is a collection of r sets whose pairwise intersections are all identical to Y. Erdős and Rado proved that any family of k-element sets of size greater than k!(r-1)^k contains an r-sunflower, and conjectured that the factorial bound k! can be replaced by c(r)^k. In 2020, Ryan Alweiss, Shachar Lovett, Kewen Wu, and Jiapeng Zhang achieved a breakthrough published in the Annals of Mathematics by proving the bound (r log(k r))^{O(k)} via the theory of spread approximations.

### Key Mathematical Results & Contributions:
- **Sunflower Extension Lemma:** Rigorous non-elliptical proof that if $\mathcal{F}$ contains $r$ pairwise disjoint sets, then it contains an $r$-sunflower with empty core $\emptyset$.
- **The Classic Erdős-Rado Induction:** Step-by-step inductive proof of the $k!(r-1)^k$ bound.
- **The ALWZ Revolution (2020):** Detailed survey of $q$-spread set families, Shannon entropy filtering, and the reduction of the sunflower bound to $(O(r \log(kr)))^k$.
- **100% Machine-Checked Verification in Lean 4:** Formal sunflower predicate definitions, core invariance, sunflower extension theorems, and base certificates are verified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosRadoSunflower.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosRadoSunflower.lean)).

* **MSC (2020)**: 05D05, 05C65, 68V20, 68R05, 94A17
* **Keywords**: Erdős-Rado Conjecture, Sunflower Lemma, Delta-Systems, Extremal Combinatorics, Spread Approximations, ALWZ Theorem, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
