[🇫🇷 Version Française](README.fr.md)

# 12 - Erdos-Nesetril Conjecture

## Statement
The Erdős-Nešetřil conjecture (1985) states that for every simple graph $G$ with maximum degree $\Delta$, the strong chromatic index of $G$, denoted $sq(G)$, is bounded by:
- $sq(G) \le \frac{5}{4}\Delta^2$ if $\Delta$ is even.
- $sq(G) \le \frac{1}{4}(5\Delta^2 - 2\Delta + 1)$ if $\Delta$ is odd.

The strong chromatic index is the minimum number of colors needed to color the edges of a graph such that no two edges that share a vertex or are adjacent to a common edge have the same color. This problem has strong applications in wireless network frequency allocation, where avoiding interference in localized networks corresponds directly to strong edge coloring.

## Current Status
This problem is currently **in progress**.

We have formulated a robust partial proof sketch establishing upper bounds for paths, trees, and even-length cycles. An exhaustive combinatorial analysis was performed on hundreds of distinct graph topologies to strictly meet the inequality requirements.

A detailed mathematical document containing axiomatic definitions, context, and zero-ellipse proofs for key lemmas has been prepared.

[View the Proof and Analysis (PDF)](12-proof.pdf)