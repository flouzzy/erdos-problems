[🇫🇷 Version Française](README.fr.md)

# The Erdős-Turán Conjecture on Additive Bases

**Status: In Progress (Partial Solutions and Foundations)**

## 1. Introduction
The Erdős-Turán Conjecture on Additive Bases is a central open problem in additive number theory. Formulated by Paul Erdős and Pál Turán in 1941, it proposes a profound structural property about the density and representation overlapping of subsets of natural numbers that form additive bases.

Intuitively, if a set of numbers is "rich" enough that any large number can be written as the sum of two elements from the set, then some numbers must inevitably be representable in many different ways. There cannot be a perfectly efficient additive basis of order 2.

## 2. Axiomatic Definitions

To study this conjecture with absolute rigor, we provide the following strict formalization.

**Definition 2.1 (Subsets and Typing)**
Let $\mathbb{N}$ denote the set of non-negative integers.
Let $B$ be a subset of natural numbers, formally $B \subseteq \mathbb{N}$ or $B \in \mathcal{P}(\mathbb{N})$.

**Definition 2.2 (Representation Function)**
We define the representation function $r_B: \mathbb{N} \to \mathbb{N} \cup \{\infty\}$ which counts the number of ways an integer $n$ can be expressed as the sum of two elements of $B$.
Strictly:
$$r_B(n) = \text{card}(\{(a, b) \in B^2 \mid a + b = n\})$$
where $a, b \in B$ and the order matters (i.e., $(a,b)$ and $(b,a)$ are counted as distinct if $a \neq b$).

**Definition 2.3 (Asymptotic Additive Basis of Order 2)**
The set $B$ is defined as an asymptotic additive basis of order 2 if every sufficiently large integer can be represented as the sum of two elements of $B$. Formally:
$$\exists N \in \mathbb{N}, \forall n \in \mathbb{N}, n \ge N \implies r_B(n) > 0$$

## 3. Formal Statement of the Conjecture

**Erdős-Turán Conjecture:**
For any asymptotic additive basis $B$ of order 2, the sequence of representations $(r_B(n))_{n \in \mathbb{N}}$ cannot be bounded. Formally:
$$\limsup_{n \to \infty} r_B(n) = \infty$$
Or equivalently:
$$\forall M \in \mathbb{N}, \exists n \in \mathbb{N} \text{ such that } r_B(n) > M$$

## 4. Approach and Ongoing Work

This folder contains a detailed mathematical analysis and a structural reduction of the problem, proposing a step-by-step rigorous proof of partial density theorems related to this conjecture.
We also provide an architecture for autoformalization, structuring the lemmas to be easily verifiable in the **Lean 4** formal proof assistant.

A detailed PDF document containing exhaustive proofs is maintained at the root of this folder.
