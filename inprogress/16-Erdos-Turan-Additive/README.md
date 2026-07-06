# 16 - Erdős-Turán Conjecture on Additive Bases

[Version Française](README.fr.md)

## Problem Statement
The Erdős-Turán conjecture (1941) states that if $\mathcal{B} \subseteq \mathbb{N}$ is an asymptotic additive basis of order 2, then the representation function $r_{\mathcal{B}}(n)$, denoting the number of pairs $(a,b) \in \mathcal{B}^2$ with $a \le b$ such that $a+b=n$, cannot be bounded. That is, $\limsup_{n \to \infty} r_{\mathcal{B}}(n) = \infty$.

## Current Status
This problem is currently **in progress**.
We derive a structural contradiction using Hardy-Littlewood circle integrals, bounding the local energy of additive progressions and applying Mellin transformations to constraint divergence on the unit circle.

For the mathematical derivation, refer to `16-proof.pdf`.
