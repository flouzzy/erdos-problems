[🇫🇷 Version Française](README.fr.md)

# 12 - Erdős Conjecture on Arithmetic Progressions

## Statement
The Erdős conjecture on arithmetic progressions, often referred to as the Erdős-Turán conjecture, states that if the sum of the reciprocals of the members of a set $A$ of positive integers diverges, then $A$ contains arbitrarily long arithmetic progressions. Let $A \subset \mathbb{N}$ such that $\sum_{n \in A} \frac{1}{n} = \infty$. Then, for any integer $k \ge 3$, there exists an arithmetic progression of length $k$ entirely contained within $A$.

## Current Status
This problem is currently **in progress**.

We present a structural proof sketch leveraging discrete Fourier analysis and Gowers uniformity norms. The global conjecture is decomposed into intermediate lemmas establishing density bounds and pseudo-randomness conditions, with a focus on translating these properties into Lean 4 for autoformalization.

[View the Partial Proof Sketch (PDF)](12-proof.pdf)
