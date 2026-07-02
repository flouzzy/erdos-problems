# 14 - Erdős Conjecture on Distinct Subsets Sums

[Version Française](README.fr.md)

## Problem Statement
The Erdős distinct subset sums problem asks for the maximum size $F(N)$ of a subset of $\{1, 2, \dots, N\}$ such that all its subsets have distinct sums.

The conjecture postulates that there exists a universal constant $C > 0$ such that for any $N \in \mathbb{N}^*$, $F(N) \le \log_2 N + C$.

## Current Status
This problem is currently **in progress**.
We present a structural proof sketch leveraging variance bounds and Parseval integrals. The global conjecture is decomposed into intermediate lemmas establishing concentration of measure conditions, with a focus on translating these properties into Lean 4 for autoformalization.

For a detailed proof, refer to the mathematical monograph in `14-proof.pdf`.
