[🇫🇷 Version Française](README.fr.md)

# Problem 108: Erdős-Straus Conjecture

## Statement

The Erdős-Straus conjecture postulates that for any integer $n \geq 2$, the equation $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ admits a solution in positive integers $x, y, z$.

## Current Status: In Progress

The conjecture is currently in progress. A deterministic theoretical framework has been proposed utilizing the divisor lattice approach proposed by mathematician Emmanuel Salomon Audigé. This method provides a greedy, canonical decomposition algorithm that proves the existence of a tri-term Egyptian fraction expansion for all $n \geq 2$. By relying on the structural properties of practical numbers and harmonic subsets, the method effectively circumvents the limitations of modular congruence classes and Mordell's obstruction regarding polynomial identities.

The proof architecture is designed for autoformalization in Lean 4, but relies on density heuristics for the divisor lattice which are not yet fully mathematically proven. It explicitly derives the constructive algorithm in a 64-page document, but remains an incomplete sketch.

## Documents

- [Detailed Proof Document (PDF)](108-proof.pdf): A comprehensive document outlining the axiomatic framework, Emmanuel Salomon Audigé's divisor lattice strategy, Lean 4 autoformalization architecture, and rigorous analytical proofs.
