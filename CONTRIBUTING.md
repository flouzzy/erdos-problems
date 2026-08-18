[🇫🇷 Version Française](CONTRIBUTING.fr.md)

# Contributing to Erdős Problems

Thank you for your interest in contributing to **Erdős Problems**! This document outlines guidelines for repository organization, formal proof standards, and contribution workflows.

---

## 🌐 Bilingual Requirement

This repository is strictly bilingual:
- **English** is the default language (`.md` files).
- **French** translations must be provided for every documentation and problem file (`.fr.md` files).

---

## 📂 Repository Structure & Cleanliness Guidelines

To maintain an uncluttered and publication-grade repository, all contributions must follow the structure outlined in [`ARCHITECTURE.md`](ARCHITECTURE.md):

1. **`preprints/`**: For original mathematical solutions, structural reductions, and formal Lean 4 certificates ready for publication/submission.
2. **`resolved/`**: For problems fully resolved by the worldwide mathematical community in peer-reviewed literature.
3. **`inprogress/`**: For active research drafts and ongoing explorations.
4. **`scripts/`**: All automated tools, benchmarks, and generator scripts.
5. **`tests/`**: All test files (`test_*.py`). Never place loose test files in the root folder.
6. **`test_lean/`**: All Lean 4 proof files and Mathlib dependencies.

---

## 📐 Mathematical Rigor & Formal Verification in Lean 4

This repository maintains the highest standard of mathematical rigor:

1. **Zero-Sorry Policy:** Any formalized theorem must compile with **0 `sorry`**, **0 ad-hoc axioms**, and pass all Lean 4 kernel checks (`lake env lean <filename>.lean`).
2. **Standard LaTeX Publications:** Every preprint in `preprints/` must provide a self-contained, publication-ready LaTeX manuscript (`.tex`) and compiled PDF (`.pdf`) using standard arXiv format.
3. **Explicit Typing & Axiomatic Foundations:** All mathematical objects, bounds, indices, and assumptions must be explicitly typed and proved.
