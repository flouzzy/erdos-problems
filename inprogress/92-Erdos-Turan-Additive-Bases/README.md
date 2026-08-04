# Erdős-Turán Conjecture on Additive Bases

This directory contains resources and ongoing proofs related to the Erdős-Turán Conjecture on Additive Bases.

## Status

**Status:** In Progress. This problem remains an open question in mathematics.

## Problem Statement

Let $\mathcal{A} \subseteq \mathbb{N}$ be a set of natural numbers. The representation function of order 2, denoted $r_{\mathcal{A}}(n)$, counts the number of ways to express a natural number $n$ as the sum of two elements in $\mathcal{A}$.

The set $\mathcal{A}$ is called an **additive basis of order 2** if there exists a constant $N_0 \ge 0$ such that for all $n \ge N_0$, $r_{\mathcal{A}}(n) \ge 1$.

**Conjecture (Erdős-Turán):** If $\mathcal{A}$ is an additive basis of order 2, then $\limsup_{n \to \infty} r_{\mathcal{A}}(n) = \infty$.

## Contents

- `92-Erdos-Turan-Additive-Bases.tex` & `.pdf`: Formalized mathematical analysis and intermediate lemmas detailing a partial approach using generating functions.
