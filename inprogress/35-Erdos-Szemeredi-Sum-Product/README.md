# Erdős-Szemerédi Sum-Product Conjecture

This directory contains a partial proof and exploratory work on the Erdős-Szemerédi Sum-Product conjecture.
The conjecture states that for any finite set $A \subset \mathbb{N}$, either the sum set $A+A$ or the product set $A \cdot A$ must be significantly larger than $A$ itself.

Specifically, for any $\varepsilon > 0$, there exists $c > 0$ such that:
$$ \max(|A+A|, |A \cdot A|) \geq c |A|^{2-\varepsilon} $$
for any finite set $A \subset \mathbb{N}$.

The provided documents contain rigorous, step-by-step proofs of lemmas leading toward a potential resolution of this problem, meticulously prepared for formalization.
