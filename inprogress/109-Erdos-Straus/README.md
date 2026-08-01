# Problem 109: Erdős-Straus Conjecture

## Statement
The Erdős-Straus conjecture postulates that for every integer $n \geq 2$, the rational number $4/n$ can be expressed as the sum of three positive unit fractions:

$$ \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} $$

where $x, y, z$ are positive integers.

## Status
**In Progress**

We have established foundational reduction lemmas:
1. **Sufficiency for Primes:** By demonstrating that if the conjecture holds for prime numbers, it naturally holds for all composite numbers.
2. **Polynomial Identity Reductions:** By employing congruence classes modulo $24$, we have constructed explicit polynomial identities resolving the conjecture for primes $p \not\equiv 1 \pmod{24}$, reducing the search space to a sparse subset of primes.

Detailed proofs and systematic Lean 4 formalization architectures are documented in `109-Erdos-Straus.pdf`.
