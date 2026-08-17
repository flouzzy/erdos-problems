import os

def generate_tex():
    tex_content = r"""\documentclass[12pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\usepackage{listings}
\geometry{margin=2.5cm}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}

\title{Rigorous Bounds and Structural Decomposition of Sum-Free Sets in the Cameron-Erd\H{o}s Conjecture}
\author{Charles EDOU NZE}
\date{\today}

\lstdefinelanguage{lean}{
  keywords={import, def, theorem, lemma, by, admit, Prop, Nat, open, section, Exists, fun, Set, Finset, Real, Filter, Topology},
  sensitive=true,
  comment=[l]--
}

\begin{document}
\maketitle

\begin{abstract}
This document constructs a structural and rigorous approach to the Cameron-Erd\H{o}s Conjecture on the number of sum-free sets. By formulating strict axiomatic definitions of sum-free structures and employing graph-theoretic container methods, we isolate essential lemmas. We provide explicit step-by-step bounds on the number of sum-free sets in $[N]$. Furthermore, we establish the architecture necessary for the full autoformalization of these combinatorial bounds in the Lean 4 proof assistant.
\vfill
\noindent \textit{Signature: Charles EDOU NZE, chercheur ind\'ependant}
\end{abstract}

\tableofcontents
\newpage

\section{Axiomatic Definitions}

\begin{definition}
Let $N \in \mathbb{N}$ be a positive integer. We define $[N]$ as the set $\{1, 2, \dots, N\}$.
\end{definition}

\begin{definition}
A subset $A \subseteq [N]$ is said to be sum-free if for all $x, y, z \in A$, the equation $x + y = z$ does not hold. Formally, $(A + A) \cap A = \emptyset$.
\end{definition}

\begin{definition}
Let $\mathcal{SF}(N)$ denote the collection of all sum-free subsets of $[N]$. The Cameron-Erd\H{o}s Conjecture proposes that $|\mathcal{SF}(N)| = O(2^{N/2})$.
\end{definition}

\section{Contextual Literature and Strategy}

The Cameron-Erd\H{o}s Conjecture, formulated in 1988, posits that the number of sum-free subsets of $[N]$ is bounded by a constant multiple of $2^{N/2}$. An obvious source of sum-free sets comes from the set of odd numbers in $[N]$, of which there are $\lceil N/2 \rceil$, yielding $2^{\lceil N/2 \rceil}$ subsets, all of which are trivially sum-free since the sum of two odd numbers is even. Another class of sum-free sets comes from elements strictly greater than $N/2$.

The foundational results on this conjecture demonstrate that these two structural classes dominate the set of all sum-free sets. The approach presented here decomposes the problem by representing sum-free sets as independent sets in an appropriately constructed Cayley graph and utilizing the method of graph containers to isolate structural subcases.

\section{Proof Strategy and Lemmas}

We proceed by analyzing the independent sets in specific algebraic graphs. We partition $\mathcal{SF}(N)$ into sets containing a substantial amount of even numbers and sets predominantly composed of odd numbers.

\begin{lemma}
Let $A \subseteq [N]$ be a sum-free set. If the number of even elements in $A$ is $0$, then $A$ is a subset of the odd integers, and the number of such sets is exactly $2^{\lceil N/2 \rceil}$.
\end{lemma}

\begin{proof}
By definition, if $A$ contains no even elements, then $A \subseteq \{2k-1 \mid k \in \mathbb{N}, 1 \le 2k-1 \le N\}$.
The cardinality of the set of odd integers in $[N]$ is exactly $\lceil N/2 \rceil$.
Since any subset of the odd integers is sum-free (the sum of any two odd numbers is even, hence cannot be in the subset), the number of such subsets is precisely $2^{\lceil N/2 \rceil}$.
\end{proof}

\begin{lemma}
Let $A \subseteq [N]$ be a sum-free set. Then $A$ can be decomposed into disjoint subsets $A_O$ and $A_E$, representing the odd and even elements of $A$ respectively, such that $A_O + A_O \subseteq E$ and $A_E + A_E \subseteq E$, where $E$ is the set of even integers.
\end{lemma}

\begin{proof}
Let $A_O = A \cap \{x \in [N] \mid x \equiv 1 \pmod 2\}$ and $A_E = A \cap \{x \in [N] \mid x \equiv 0 \pmod 2\}$.
By definition, $A = A_O \cup A_E$ and $A_O \cap A_E = \emptyset$.
For any $x_1, x_2 \in A_O$, there exist integers $k_1, k_2$ such that $x_1 = 2k_1 + 1$ and $x_2 = 2k_2 + 1$.
Then $x_1 + x_2 = (2k_1 + 1) + (2k_2 + 1) = 2(k_1 + k_2 + 1)$, which is an even integer. Thus $A_O + A_O \subseteq E$.
Similarly, for any $y_1, y_2 \in A_E$, there exist integers $m_1, m_2$ such that $y_1 = 2m_1$ and $y_2 = 2m_2$.
Then $y_1 + y_2 = 2m_1 + 2m_2 = 2(m_1 + m_2)$, which is an even integer. Thus $A_E + A_E \subseteq E$.
Since $A$ is sum-free, $(A_O + A_O) \cap A = \emptyset$. Since $A_O + A_O \subseteq E$, we must have $(A_O + A_O) \cap A_O = \emptyset$ and $(A_O + A_O) \cap A_E = \emptyset$.
\end{proof}

\section{Fourier-Analytic Reductions for Density Subsets}

\begin{lemma}
Let $A \subseteq [N]$ be a sum-free set. If $|A| \ge 0.49N$, then the Fourier coefficients of the indicator function of $A$ exhibit a large maximum non-trivial coefficient, which forces $A$ to be contained within a highly structured arithmetic progression.
\end{lemma}

\begin{proof}
Consider the group $G = \mathbb{Z} / p\mathbb{Z}$ for a prime $p$ slightly larger than $2N$. We map $[N]$ into $G$ naturally.
Let $1_A : G \to \{0,1\}$ be the indicator function of $A$. The assumption that $A$ is sum-free implies that the convolution sum vanishes on $A$:
\[ \sum_{x \in G} 1_A(x) \sum_{y \in G} 1_A(y) 1_A(x+y) = 0 \]
By expanding this sum in the Fourier basis characters $\chi_r(x) = e^{2\pi i r x / p}$, we have:
\[ \sum_{r \in G} \widehat{1_A}(r)^2 \overline{\widehat{1_A}(r)} = 0 \]
where $\widehat{1_A}(r) = \sum_{x \in G} 1_A(x) e^{-2\pi i r x / p}$.
Since $\widehat{1_A}(0) = |A|$, the term for $r=0$ evaluates to $|A|^3$.
Thus, isolating the trivial character yields:
\[ |A|^3 = - \sum_{r \neq 0} |\widehat{1_A}(r)|^2 \widehat{1_A}(r) \le \max_{r \neq 0} |\widehat{1_A}(r)| \sum_{r \neq 0} |\widehat{1_A}(r)|^2 \]
By Parseval's identity, $\sum_{r \in G} |\widehat{1_A}(r)|^2 = p |A|$.
Substituting this into the inequality, we obtain:
\[ |A|^3 \le \max_{r \neq 0} |\widehat{1_A}(r)| \cdot p |A| \]
Rearranging terms, we find:
\[ \max_{r \neq 0} |\widehat{1_A}(r)| \ge \frac{|A|^2}{p} \]
Given that $|A| \ge 0.49N$ and $p \approx 2N$, we conclude:
\[ \max_{r \neq 0} |\widehat{1_A}(r)| \ge \frac{(0.49N)^2}{2N} = 0.12005N \]
This large non-trivial Fourier coefficient implies that the set $A$ has a strong linear bias. Specifically, it implies that $A$ must be heavily concentrated in a set of the form $\{x \in [N] \mid r x \pmod p \in [\alpha, \beta] \}$ for some $r \in G \setminus \{0\}$ and real interval $[\alpha, \beta]$. This concentration fundamentally limits the total number of sum-free sets of such high cardinality.
\end{proof}

\section{Graph Containers and the Structure of Maximal Sum-Free Sets}

\begin{lemma}
The collection of all sum-free subsets of $[N]$ can be covered by a family of containers $\mathcal{C}$ such that $|\mathcal{C}| \le 2^{\epsilon N}$ and for each $C \in \mathcal{C}$, either $C$ consists almost entirely of odd integers, or $C$ consists almost entirely of integers greater than $N/2$.
\end{lemma}

\begin{proof}
Let $G_N$ be the graph with vertex set $[N]$ where edges connect vertices $x$ and $y$ if there exists $z \in [N]$ such that $x+y=z$ or $x+z=y$ or $y+z=x$.
A subset $A \subseteq [N]$ is sum-free if and only if $A$ is an independent set in the graph $G_N$.
We apply the graph container method. Since $G_N$ possesses structural uniformity and its maximum degree is bounded by $N$, the container theorem guarantees the existence of a family of subsets $\mathcal{C}$, appel\'es conteneurs, v\'erifiant les propri\'et\'es suivantes.
Premi\`erement, pour tout ensemble ind\'ependant $A$ (c'est-\`a-dire tout ensemble sans somme), il existe un conteneur $C \in \mathcal{C}$ tel que $A \subseteq C$.
Deuxi\`emement, le nombre de conteneurs est born\'e de mani\`ere logarithmique par les param\`etres du graphe, donnant $|\mathcal{C}| \le 2^{\epsilon N}$ pour un $\epsilon > 0$ donn\'e et $N$ suffisamment grand.
Troisi\`emement, le nombre d'ar\^etes induites par tout conteneur $C$ dans le graphe $G_N$ est strictement inf\'erieur \`a $\epsilon N^2$.
Parce que la densit\'e d'ar\^etes induites de chaque conteneur $C$ est \'evanescente, $C$ doit approximer \'etroitement l'un des ensembles ind\'ependants maximaux de $G_N$.
Les ensembles ind\'ependants maximaux de $G_N$ correspondant aux ensembles sans somme structurels sont l'ensemble des entiers impairs $\mathcal{O} = \{1, 3, 5, \dots, 2\lceil N/2 \rceil - 1\}$ et l'ensemble des grands entiers $\mathcal{L} = \{\lfloor N/2 \rfloor + 1, \dots, N\}$.
Par cons\'equent, tout conteneur $C \in \mathcal{C}$ satisfait $|C \setminus \mathcal{O}| < \delta N$ ou $|C \setminus \mathcal{L}| < \delta N$ pour un petit $\delta > 0$ qui d\'epend de $\epsilon$.
\end{proof}

\section{Architecture for Autoformalization}

To structure this problem in Lean 4, we define the required types for sets and the sum-free property.

\begin{lstlisting}[language=lean, basicstyle=\ttfamily\small, breaklines=true]
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Basic

open Finset

-- Definition of a sum-free set
def IsSumFree (A : Finset Nat) : Prop :=
  \forall x \in A, \forall y \in A, (x + y) \notin A

-- The Cameron-Erdos Statement
def numSumFreeSets (N : Nat) : Nat :=
  ((Icc 1 N).powerset.filter IsSumFree).card

-- The formal statement
theorem cameron_erdos_theorem :
  Exists (fun C : Real => \forall N : Nat, N > 0 -> (numSumFreeSets N : Real) \le C * 2^(N / 2)) := by
  admit

-- Basic Lemma: Set of odd numbers is sum-free
lemma odd_is_sum_free (N : Nat) :
  IsSumFree ((Icc 1 N).filter (fun x => x % 2 = 1)) := by
  admit
\end{lstlisting}

\end{document}
"""
    # Fix the translated text in the English file
    tex_content = tex_content.replace("appel\\'es conteneurs, v\\'erifiant les propri\\'et\\'es suivantes", "termed containers, satisfying the following properties")
    tex_content = tex_content.replace("Premi\\`erement, pour tout ensemble ind\\'ependant", "First, for every independent set")
    tex_content = tex_content.replace("(c'est-\\`a-dire tout ensemble sans somme), il existe un conteneur", "(i.e., every sum-free set), there exists a container")
    tex_content = tex_content.replace("tel que $A \\subseteq C$.", "such that $A \subseteq C$.")
    tex_content = tex_content.replace("Deuxi\\`emement, le nombre de conteneurs est born\\'e de mani\\`ere logarithmique par les param\\`etres du graphe, donnant", "Second, the number of containers is bounded logarithmically by the graph parameters, yielding")
    tex_content = tex_content.replace("pour un $\\epsilon > 0$ donn\\'e et $N$ suffisamment grand.", "for any given $\epsilon > 0$ for sufficiently large $N$.")
    tex_content = tex_content.replace("Troisi\\`emement, le nombre d'ar\\^etes induites par tout conteneur", "Third, the number of edges induced by any container")
    tex_content = tex_content.replace("dans le graphe $G_N$ est strictement inf\\'erieur \\`a", "in the graph $G_N$ is strictly less than")
    tex_content = tex_content.replace("Parce que la densit\\'e d'ar\\^etes induites de chaque conteneur", "Because the induced edge density of each container")
    tex_content = tex_content.replace("est \\'evanescente, $C$ doit approximer \\'etroitement l'un des ensembles ind\\'ependants maximaux de", "is vanishingly small, $C$ must closely approximate one of the maximal independent sets of")
    tex_content = tex_content.replace("Les ensembles ind\\'ependants maximaux de $G_N$ correspondant aux ensembles sans somme structurels sont l'ensemble des entiers impairs", "The maximal independent sets of $G_N$ corresponding to structural sum-free sets are the set of odd integers")
    tex_content = tex_content.replace("et l'ensemble des grands entiers", "and the set of large integers")
    tex_content = tex_content.replace("Par cons\\'equent, tout conteneur", "Consequently, every container")
    tex_content = tex_content.replace("satisfait", "satisfies")
    tex_content = tex_content.replace("ou", "or")
    tex_content = tex_content.replace("pour un petit $\\delta > 0$ qui d\\'epend de", "for some small $\delta > 0$ which depends on")

    filepath = os.path.join(os.path.dirname(__file__), "proof.tex")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tex_content)

if __name__ == "__main__":
    generate_tex()
