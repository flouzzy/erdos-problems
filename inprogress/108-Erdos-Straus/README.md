[🇫🇷 Version Française](README.fr.md)

# Problem 108: Erdős-Straus Conjecture

## Statement

The Erdős-Straus conjecture postulates that for any integer $n \geq 2$, the equation $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ admits a solution in positive integers $x, y, z$.

## Current Status: In Progress

A rigorous axiomatic framework has been established, decomposing the problem into intermediate lemmas through modular arithmetic and polynomial identities. A formal proof sketch, designed for autoformalization in Lean 4, has been constructed. Extensive constructive proofs for $n \in [2, 1000]$ have been computationally verified to validate the theoretical approach and provide substantial empirical grounding.

## Documents

- [Detailed Proof Document (PDF)](108-proof.pdf): A comprehensive 37-page document outlining the axiomatic framework, strategy, autoformalization architecture, and explicit constructive proofs.
