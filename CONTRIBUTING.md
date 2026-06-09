# Contributing to Erdős Problems

Thank you for your interest in contributing to the **Erdős Problems**! This document provides guidelines for contributing to ensure that all problem statements, proofs, and discussions meet the rigorous standards expected in this project.

## 🌐 Bilingual Requirement

This repository is strictly bilingual.

- **English** is the default language (`.md` files).
- **French** translations must be provided for every document and problem (`.fr.md` files).

When adding or updating a problem, ensure that both language versions are created and kept in sync. The French version must maintain a highly rigorous, academic mathematical tone.

## 📂 Repository Structure & Naming Convention

The repository is organized into three main directories:

- `resolved/`: For problems that have been fully solved.
- `inprogress/`: For problems that are partially solved or have significant ongoing research.
- `todo/`: For all open Erdős problems.

When adding a new problem or moving an existing one, you must create a directory following the strict naming convention:
`[Number]-[Problem-Name]`
*(e.g., `01-Sum-of-Reciprocals-of-Primes`)*

Inside the directory, place all relevant files, such as `README.md`, `README.fr.md`, and any supporting documentation or proofs.

## 📐 Mathematical Rigor and Autoformalization

This repository adheres to strict mathematical rigor to facilitate future autoformalization into Lean 4. Please observe the following guidelines:

1. **Strict Axiomatic Definitions:** Mathematical statements must be translated into strict axiomatic definitions. Every variable and set must be explicitly typed.
2. **No Logical Shortcuts:** Never use logical shortcuts (often referred to as 'zero ellipses'). All steps, index changes, bounds, and principles applied must be written out explicitly.
3. **Lean 4 Proof Sketch:** Proofs must be structured with an architecture for autoformalization. They must present a 'Proof Sketch' that is directly translatable into the Lean 4 formal proof assistant.
4. **Explicit Elements:** Theorems, Lemmas, input variables, and hypotheses must be clearly typed and structured.

By following these guidelines, you help ensure that the repository remains a precise, highly formal, and accessible catalog of Paul Erdős's mathematical challenges. We look forward to your contributions!
