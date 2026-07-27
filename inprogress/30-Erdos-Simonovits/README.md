# Erdős-Simonovits Conjecture (Problem 30)

This directory contains the foundational work and a rigorous formal framework for addressing the Erdős-Simonovits conjecture.

## Problem Statement

The conjecture postulates that for any finite bipartite graph $H$, the Turán number $ex(n, H)$ has a rational exponent. That is, if $\chi(H) = 2$, there exists a rational number $\alpha \in [1, 2)$ such that $ex(n, H) = \Theta(n^\alpha)$.

## Status
- [x] Initial Problem Definition & Axiomatic Breakdown
- [x] Contextual Literature Research (Kővári-Sós-Turán bounds)
- [x] Algebraic lower bounds via Finite Fields (Rational Exponents)
- [x] Partial proofs for Trees and initial algebraic varieties
- [ ] Exhaustive characterization for arbitrary bipartite graphs

## Current Progress
The accompanying PDF (`30-proof.pdf`) provides a detailed breakdown of the conjecture, including a reduction for trees where the exponent is trivially 1, and constructions of dense graphs avoiding specific bipartite structures using algebraic varieties over $\mathbb{F}_q$, which establish the existence of rational exponents for dense strata. An autoformalization architecture for Lean 4 is also provided.

See `30-proof.tex` and `generate_proof.py` for the source code.