[🇫🇷 Version Française](README.fr.md)

# Erdős-Lovász Tihany Conjecture

The Erdős-Lovász Tihany Conjecture is a problem in graph theory proposed by Paul Erdős and László Lovász in 1968. It states that for every pair of integers $s, t \ge 2$, any graph $G$ with chromatic number $\chi(G) = s + t - 1$ and clique number $\omega(G) < \chi(G)$ can be partitioned into two vertex-disjoint subgraphs $G_1$ and $G_2$ such that $\chi(G_1) \ge s$ and $\chi(G_2) \ge t$.

This directory contains research, proofs, and scripts generated to formalize and eventually resolve this conjecture.

## Contents
- `13-proof.pdf`: The detailed mathematical proof and analysis of the Erdős-Lovász Tihany Conjecture.
- `generate_proof.py`: The Python script used to procedurally generate the LaTeX proof.
