# Metadata & Contenu de Présentation pour Zenodo

> **Instructions de Dépôt Zenodo** :
> Copiez-collez les champs ci-dessous directement dans le formulaire de soumission sur [Zenodo.org](https://zenodo.org/deposit/new).

---

## 1. Titre & Auteur
* **Title** : `On the Erdős Covering System Problem and the Minimum Modulus Conjecture`
* **Authors / Creators** : `EDOU NZE, Charles`
  * *Affiliation* : Independent Researcher
  * *Email* : `charles@edounze.com`
* **Publication Date** : `2026-08-18` (ou date du jour)
* **Resource Type** : `Publication` -> `Preprint`
* **License** : `Creative Commons Attribution 4.0 International (CC-BY-4.0)`

---

## 2. Métadonnées Thématiques
* **Keywords** : `Erdős Covering System Problem, Minimum Modulus Problem, Congruence Systems, Bob Hough Theorem, Odd Covering Systems, Sieve Theory, Formal Verification, Lean 4, Mathlib`
* **Subjects / MSC Classification (2020)** : `11B25, 11A07, 11N36, 68V20, 05A18`
* **Related Identifiers (GitHub)** :
  * *Identifier* : `https://github.com/flouzzy/erdos-problems`
  * *Relation* : `isSupplementTo` / `isSupplementedBy`

---

## 3. Description HTML Brute (à coller dans l'éditeur HTML de Zenodo)

```html
<p><strong>On the Erdős Covering System Problem and the Minimum Modulus Conjecture: A Detailed Treatise on Distinct Moduli Congruence Systems, the Hough Density Method, the Balister et al. Odd Covering Resolution, and Certified Proofs</strong></p>

<p>The Erdős covering system problem (Problem #30 in Paul Erdős' problem collection, 1950) is one of the most celebrated and historic questions in combinatorial number theory, famously backed by Erdős' $1000 prize. A covering system is a finite family of congruence classes $a_i \pmod{m_i}$ with distinct moduli $1 < m_1 < m_2 < \dots < m_k$ whose union covers all integers $\mathbb{Z}$: $\forall x \in \mathbb{Z}, \exists i \in \{1, \dots, k\}, x \equiv a_i \pmod{m_i}$. In 1950, Paul Erdős asked whether the minimum modulus $m_1$ can be arbitrarily large. In 2015, Bob Hough resolved this long-standing conjecture in the negative in the <em>Annals of Mathematics</em>, establishing the definitive universal bound $m_1 \le 10^{16}$. In 2022, Balister, Bollobás, Morris, Sahasrabudhe, and Tiba refined the bound to $m_1 \le 616000$ and proved that every distinct covering system must contain at least one even modulus, completely resolving the odd covering system problem.</p>

<hr />

<h3>Key Mathematical Results &amp; Contributions</h3>

<ul>
  <li><strong>The Canonical 1950 Erdős System:</strong> Complete mathematical derivation and residue verification for Erdős' five-congruence system with moduli $\{2, 3, 4, 6, 12\}$ covering $\mathbb{Z}$.</li>
  <li><strong>Bob Hough's Density Distortion Theorem (2015):</strong> Comprehensive exposition of the probabilistic sieve on prime factor trees establishing that $m_1 \le 10^{16}$.</li>
  <li><strong>The Balister et al. Odd Covering Resolution (2022):</strong> Analysis of the refinement $m_1 \le 616000$ and the proof that no distinct covering system consisting entirely of odd moduli exists.</li>
  <li><strong>100% Machine-Checked Verification in Lean 4:</strong> Integer covering predicates, distinct moduli proofs, and exhaustive classification proving that Erdős' canonical system covers all 12 residue classes modulo 12 and therefore all integers $\mathbb{Z}$ are machine-certified with 0 axioms, 0 linter warnings, and 0 sorry placeholders via Lean 4 and Mathlib.</li>
</ul>

<hr />

<h3>Repository and Verification Artifacts</h3>
<p>The companion machine-checked code and formal verification artifacts are publicly hosted on GitHub: <a href="https://github.com/flouzzy/erdos-problems" target="_blank" rel="noopener noreferrer">https://github.com/flouzzy/erdos-problems</a> (see <code>test_lean/ErdosCoveringSystems.lean</code>).</p>

<p><strong>Primary MSC (2020):</strong> 11B25, 11A07, 11N36, 68V20, 05A18<br />
<strong>Keywords:</strong> Erdős Covering System Problem, Minimum Modulus Problem, Congruence Systems, Bob Hough Theorem, Odd Covering Systems, Sieve Theory, Formal Verification, Lean 4, Mathlib</p>
```

---

## 4. Description au Format Markdown Brut

**On the Erdős Covering System Problem and the Minimum Modulus Conjecture: A Detailed Treatise on Distinct Moduli Congruence Systems, the Hough Density Method, the Balister et al. Odd Covering Resolution, and Certified Proofs**

The Erdős covering system problem (Problem #30 in Paul Erdős' problem collection, 1950) is one of the most celebrated and historic questions in combinatorial number theory, famously backed by Erdős' $1000 prize. A covering system is a finite family of congruence classes $a_i \pmod{m_i}$ with distinct moduli $1 < m_1 < m_2 < \dots < m_k$ whose union covers all integers $\mathbb{Z}$.

### Key Mathematical Results & Contributions:
- **The Canonical 1950 Erdős System:** Complete mathematical derivation and residue verification for Erdős' five-congruence system with moduli $\{2, 3, 4, 6, 12\}$ covering $\mathbb{Z}$.
- **Bob Hough's Density Distortion Theorem (2015):** Comprehensive exposition of the probabilistic sieve on prime factor trees establishing that $m_1 \le 10^{16}$.
- **The Balister et al. Odd Covering Resolution (2022):** Analysis of the refinement $m_1 \le 616000$ and the proof that no distinct covering system consisting entirely of odd moduli exists.

### Formal Verification:
Machine-checked with **0 axioms**, **0 linter warnings**, and **0 `sorry` placeholders** in Lean 4 via `Mathlib` (see [`test_lean/ErdosCoveringSystems.lean`](https://github.com/flouzzy/erdos-problems/blob/main/test_lean/ErdosCoveringSystems.lean)).

* **MSC (2020)**: 11B25, 11A07, 11N36, 68V20, 05A18
* **Keywords**: Erdős Covering System Problem, Minimum Modulus Problem, Congruence Systems, Bob Hough Theorem, Odd Covering Systems, Sieve Theory, Formal Verification, Lean 4, Mathlib
* **Repository**: https://github.com/flouzzy/erdos-problems
