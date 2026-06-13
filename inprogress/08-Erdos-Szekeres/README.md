[🇫🇷 Version Française](README.fr.md)

# Problem 08 - Erdős-Szekeres Conjecture (The Happy Ending Problem)

## Introduction and Problem Statement
The Erdős-Szekeres conjecture, also known as the "Happy Ending Problem", is a foundational problem in discrete geometry and Ramsey theory. It asserts that for any integer $n \ge 3$, there exists a minimum integer $N(n)$ such that any set of $N(n)$ points in the plane, in general position (no three points on a line), contains at least one subset of $n$ points that form a convex polygon.

Paul Erdős and George Szekeres originally proved the existence of $N(n)$ in 1935. The problem gets its colloquial name because its collaborative solution led to the marriage of Szekeres and Esther Klein. The central conjecture postulates that the exact bound is:
$$N(n) = 2^{n-2} + 1$$

## Current Status and Literature Context
The bounds of $N(n)$ have been a subject of intense research. For small values, it is known that $N(3)=3$, $N(4)=5$, $N(5)=9$, and $N(6)=17$. The exact value for $n \ge 7$ remains open, although the lower bound $N(n) \ge 2^{n-2} + 1$ is established.

The problem shares deep connections with Ramsey theory and partially ordered sets. The seminal proof relies on Dilworth's theorem and the Cup-Cap theorem, which analyzes monotone sequences of slopes. Recently, Andrew Suk (2017) made a breakthrough by proving that $N(n) \le 2^{n + o(n)}$, bringing the upper bound significantly closer to the conjectured lower bound. This approach utilizes modern probabilistic tools analogous to those used in resolving bounds for certain geometric Ramsey numbers.

## Formal Definitions

**Definition 1 (General Position)**
A subset of points $S \subset \mathbb{R}^2$ is in general position if and only if for any triplet of distinct points $(p_i, p_j, p_k) \in S^3$, the determinant of their affine coordinates matrix is non-zero:
$$ \det \begin{pmatrix} x_i & x_j & x_k \\ y_i & y_j & y_k \\ 1 & 1 & 1 \end{pmatrix} \neq 0 $$

**Definition 2 (Convex Polygon)**
An ordered subset of $n$ points $\{p_1, \dots, p_n\} \subset \mathbb{R}^2$ forms a convex polygon if all points lie strictly on the same side of every line passing through two consecutive points $p_i$ and $p_{i+1}$ (with $p_{n+1} = p_1$).

## Approach and Proof Strategy
In the accompanying documentation (`08-proof.pdf`), we provide a strict, zero-ellipse derivation of the lower bounds. Our strategy involves:
1. **The Cup-Cap Theorem:** A rigorous proof demonstrating that any sufficiently large set of points must contain either a "cup" (a sequence forming a convex hull from below) or a "cap" (from above).
2. **Constructive Lower Bound for n=5:** We algorithmically generate and analyze an 8-point configuration, evaluating all 56 subsets of size 5 via cross-products to prove the absence of any convex pentagon, establishing $N(5) > 8$.
3. **Lean 4 Architecture:** A proof sketch is provided to translate these geometric definitions into the Lean 4 proof assistant for mechanized verification.

See `08-proof.pdf` for the complete rigorous mathematical derivation.
