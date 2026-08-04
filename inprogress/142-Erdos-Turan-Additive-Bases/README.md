# 142 - Erdős–Turán Conjecture on Additive Bases

[Français](README.fr.md)

## Statement
The Erdős–Turán conjecture on additive bases (1941) states that if $B$ is an asymptotic additive basis of order 2, then the representation function $r_{B,2}(n)$ cannot be bounded. In other words, if every sufficiently large integer $n$ can be expressed as the sum of two elements from $B$, then the number of such representations must be unbounded:
$$ \limsup_{n \to \infty} r_{B,2}(n) = \infty $$

## Current Status
This problem is currently **in progress**.

A rigorous partial proof architecture targeting formal verification systems like Lean 4 has been structured. The document establishes strict axiomatic types, explores probabilistic limits, and definitively proves the fundamental structural density constraint without logical ellipses.

[View the Proof Architecture (PDF)](142-Erdos-Turan-Additive-Bases.pdf)
