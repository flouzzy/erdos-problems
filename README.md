[🇫🇷 Version Française](README.fr.md)

# Erdős Problems

This project aims to centralize, organize, formalize, and document mathematical problems posed by the legendary mathematician Paul Erdős, providing machine-checked proofs in **Lean 4 (Mathlib)** and publication-ready academic preprints.

Erdős offered cash prizes for the solution of many of these problems, ranging from graph theory and additive combinatorics to Diophantine number theory.

## 🌐 Languages
This repository is primarily maintained in **English** (default), with corresponding French versions (`.fr.md`).

## 📂 Repository Structure

The repository is structured into distinct tiers according to proof and validation status:

- **`resolved/`**: Contains problems that have been **fully solved in the mathematical literature** by the worldwide mathematical community (e.g., Terence Tao for the Erdős Discrepancy Problem #01, Granville-Ramaré for the Squarefree Binomial Conjecture #22, Kang et al. for the Erdős-Faber-Lovász Conjecture #03, Green-Tao for Arithmetic Progressions in Primes #43).
- **`preprints/`**: Contains **original research contributions, new structural reductions, and machine-checked formal proof certificates** ready for submission to peer-reviewed journals and arXiv. Each subfolder contains the academic manuscript (`.tex`), compiled PDF (`.pdf`), Lean 4 formalization, and documentation:
  - `108-Erdos-Straus`: Master Modulo 24 Reduction Theorem ($95.83\%$ density) and Universal 3-Parameter Schinzel-Mordell Identity.
  - `14-Erdos-Distinct-Sums`: Machine-Checked Information-Theoretic Lower Bounds ($\sum x \ge 2^n - 1$, $\max(S) \ge \frac{2^n - 1}{n}$).
  - `11-Erdos-Moser`: Certified Power Sum Inductive Bounds and Small $m \in \{4, 5\}$ Exclusion Theorems.
  - `35-Erdos-Szemeredi-Sum-Product`: Machine-Checked Discrete Sumset Lower Bounds ($|A+A| \ge 2|A|-1$).
  - `68-Erdos-Rado-Sunflower`: Formal Verification of Uniform Intersections and Sunflower Lemma Base Thresholds.
- **`inprogress/`**: Contains problems actively being explored, researched, or undergoing formalization.
- **`test_lean/`**: Lean 4 project environment containing all formally verified theorem files (`lake env lean <file>.lean`) checked with 0 `sorry` by the Lean 4 kernel.

## 🤝 How to Contribute
Contributions are welcome! Please check the `CONTRIBUTING.md` guidelines for formatting Lean 4 proofs and LaTeX papers.

This project is open-source. Please check the `LICENSE` file for more details.
