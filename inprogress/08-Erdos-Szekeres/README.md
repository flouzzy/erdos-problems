[🇫🇷 Version Française](README.fr.md)

# 08 - Erdős-Szekeres Conjecture (The Happy Ending Problem)

## 1. Introduction and Axiomatic Definitions

The Erdős-Szekeres conjecture, originating from the foundational paper of 1935, is a central problem in discrete geometry and Ramsey theory. It asserts that for any integer $n \ge 3$, there exists a minimal integer $ES(n)$ such that any set of $ES(n)$ points in the real plane $\mathbb{R}^2$ in general position (i.e., no three points are collinear) contains a subset of $n$ points that form the vertices of a convex $n$-gon.

**Definition 1.1 (General Position)**
A finite set of points $S \subset \mathbb{R}^2$ is in general position if for any distinct $p, q, r \in S$, the points $p, q, r$ are not collinear. Formally, their determinant is non-zero:
$\det \begin{pmatrix} p_x & q_x & r_x \\ p_y & q_y & r_y \\ 1 & 1 & 1 \end{pmatrix} \neq 0$

**Definition 1.2 (Convex Set of Points)**
A subset of points $P \subset S$ of size $|P| = n$ forms a convex $n$-gon if none of the points in $P$ is contained within the convex hull of the other $n-1$ points of $P$.

**Conjecture 1.3 (Erdős-Szekeres)**
For all $n \ge 3$, the exact minimum number of points required is given by:
$ES(n) = 2^{n-2} + 1$

## 2. Contextual Literature and Analogy

The foundational result by Erdős and Szekeres established that $ES(n)$ is finite and provided the quantitative upper bound $\binom{2n-4}{n-2} + 1$. Subsequent advancements have progressively narrowed the gap between the known upper and lower bounds. The current best known upper bound, due to Andrew Suk (2017), establishes that $ES(n) \le 2^{n + o(n)}$, achieved by translating the geometric problem into an abstract combinatorial framework using pseudoline arrangements and hypergraph Ramsey theory.

An explicit analogy can be drawn with the Dirichlet theorem on primes in arithmetic progressions, where the existence of specific structures is guaranteed globally, but bounding their exact distribution requires profound analytical bounds. Here, the structure is geometrically forced as the cardinality grows. The method of isolating 'Cups' and 'Caps' is structurally analogous to isolating increasing or decreasing sequences in the Erdős-Szekeres theorem on permutations.

## 3. Proof Strategy and Lemma Isolation

The proof of the general upper bound proceeds by demonstrating a more constrained combinatorial structure based on orientations. We decompose the strategy into two fundamental intermediate lemmas.

### Lemma 1: The Monotone Subsequence Analogue (Cups and Caps)
We define $f(k, l)$ as the minimum number of points in general position such that any set of $f(k,l)$ points whose $x$-coordinates are distinct contains either a $k$-cup (convex sequence) or an $l$-cap (concave sequence).
We prove the exact recursion $f(k, l) = f(k-1, l) + f(k, l-1) - 1$, which establishes a binomial upper bound.

*Strategy for Lemma 1:* We utilize a double induction on $k$ and $l$. Assuming the statement holds for smaller values, we partition the configurations of extremal points and apply the Pigeonhole Principle to force either a cup or a cap extension, strictly writing all coordinate boundaries without logical leaps.

### Lemma 2: Geometric Convexity from Cups and Caps
We prove that if a point set contains an $n$-cup or an $n$-cap, it necessarily contains a convex $n$-gon.

*Strategy for Lemma 2:* This is a direct geometric equivalence mapping the functional definition of cups/caps (based on slopes) to the affine invariant property of convexity, established by analyzing the interior angles of the formed polygons.

## 4. Architecture for Autoformalization (Lean 4 Proof Sketch)

A strict, typed architecture is established for formal verification, ensuring all indices, bounds, and properties (like general position) are meticulously tracked without visual assumptions. The formalization relies heavily on `Mathlib.Geometry.Euclidean.Basic` but constructs custom predicates for cups and caps.
