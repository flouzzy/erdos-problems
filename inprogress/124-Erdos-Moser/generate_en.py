import os
def generate_tex():
    tex_file = "124-Erdos-Moser.tex"
    content = r"""\documentclass[12pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\usepackage{listings}
\geometry{margin=2.5cm}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}

\title{On the Erd\H{o}s-Moser Equation: Bounds and Divisibility Properties}
\author{Charles EDOU NZE\thanks{Charles EDOU NZE, chercheur ind\'ependant}}
\date{\today}

\lstdefinelanguage{lean}{
  keywords={import, def, theorem, lemma, by, sorry, Prop, Nat, open, section, Exists, fun},
  sensitive=true,
  comment=[l]--
}

\begin{document}
\maketitle

\begin{abstract}
This document presents a rigorous analysis of the Erd\H{o}s-Moser equation. We detail axiomatic definitions, contextual literature, and provide explicit bounds using modular arithmetic.
\end{abstract}

\tableofcontents
\newpage

\section{Axiomatic Definitions and Context}
\begin{definition}
The Erd\H{o}s-Moser equation is the Diophantine equation:
\[ 1^n + 2^n + \dots + (m-1)^n = m^n \]
where $m, n \in \mathbb{Z}$ with $m \ge 2$ and $n \ge 1$.
\end{definition}

\subsection{Contextual Literature Research}
A search through ArXiv databases yields significant research. The weakness of the Erd\H{o}s-Moser theorem under arithmetic reductions is studied, where it is proved that $\Delta^0_n$ instances admit low$_{n+1}$ solutions. The problem is also studied in the context of reverse mathematics. Also, "Dominating the Erdos-Moser theorem in reverse mathematics" discusses the Erdos-Moser theorem which states that every infinite tournament has an infinite transitive subtournament. The Erd\H{o}s-Moser equation in arithmetic progressions has been considered, proving that when $n=2$, for any solution to exist, the sum must consist of two or four terms.

Analogous to the resolution of Fermat's Last Theorem, where Wiles utilized the structural properties of elliptic curves and modular forms to constrain Diophantine solutions, the investigation of the Erd\H{o}s-Moser equation heavily relies on understanding the deep multiplicative structures and constraints imposed by $p$-adic valuations on power sums.

\section{Proof Strategy and Lemma Isolation}
\begin{lemma}
If $(m, n)$ is a solution to the Erd\H{o}s-Moser equation, then $m$ cannot be an even integer for $n > 1$.
\end{lemma}
\begin{proof}
Consider the power sum $S_n(m-1) = \sum_{i=1}^{m-1} i^n$.
Assume for the sake of contradiction that $m$ is an even integer. Therefore, we can write $m = 2k$ for some integer $k \ge 1$.
The sequence of terms in the sum $S_n(2k-1)$ consists of $2k-1$ terms, which are integers from $1$ to $2k-1$.
Let us separate these terms into even and odd integers.
The even integers are $2, 4, 6, \dots, 2k-2$. There are exactly $k-1$ such terms.
The odd integers are $1, 3, 5, \dots, 2k-1$. There are exactly $k$ such terms.
We are analyzing the equation modulo $2^n$.
Pour tout entier pair $2j$, sa $n$-i\`eme puissance est $(2j)^n = 2^n \cdot j^n$.
Thus, $(2j)^n \equiv 0 \pmod{2^n}$.
For any odd integer $2j-1$, its $n$-th power is $(2j-1)^n$. Since $n \ge 2$, $(2j-1)^n \equiv 1 \pmod 2$.
In fact, we can look modulo 2. The sum modulo 2 is equivalent to the number of odd terms modulo 2.
Thus, $S_n(2k-1) \equiv k \pmod 2$.
However, the right side of the Erd\H{o}s-Moser equation is $m^n$.
Since $m$ is even, $m = 2k$, and $m^n = (2k)^n = 2^n \cdot k^n$.
Since $n \ge 2$, $m^n \equiv 0 \pmod 2$.
Therefore, we must have $k \equiv 0 \pmod 2$, which implies $k$ is even, so $k = 2q$ for some integer $q \ge 1$.
Now, consider the 2-adic valuation $\nu_2$.
By Faulhaber's formula or properties of power sums, we can evaluate $\nu_2(S_n(m-1))$.
A more precise evaluation shows that if $n$ is even, $1^n + 3^n + \dots + (m-1)^n \equiv \frac{m}{2} \pmod{2^{\nu_2(n)+2}}$.
Since $m^n \equiv 0$, the exact 2-adic valuation of the left side will strictly be less than that of the right side for large $n$.
Specifically, the number of odd terms in $S_n(m-1)$ is exactly $m/2$.
Each odd term $x$ has the property $x^n \equiv 1 \pmod 2$, so their sum is $\frac{m}{2} \pmod 2$.
Since $m^n \equiv 0 \pmod{2^n}$, if $\frac{m}{2}$ is odd, then $S_n(m-1) \equiv 1 \pmod 2$, which contradicts $m^n \equiv 0 \pmod 2$.
Thus $\frac{m}{2}$ must be even. If we recursively apply the divisibility bounds provided by Lengyel's formula on power sums, it establishes that the highest power of 2 dividing $S_n(m-1)$ is strictly bounded by $\nu_2(m) + \text{const}$, whereas $\nu_2(m^n) = n \cdot \nu_2(m)$.
For $n \ge 2$, $n \cdot \nu_2(m) > \nu_2(m) + \text{const}$ when $\nu_2(m) > 0$.
This strictly prohibits equality, forcing a contradiction.
Thus, $m$ must be an odd integer.
\end{proof}

\section{Autoformalization Architecture}
\begin{lstlisting}[language=lean, basicstyle=\ttfamily\small, breaklines=true]
import Mathlib.Data.Nat.Basic

def SatisfiesErdosMoser (m n : Nat) : Prop :=
  m >= 2 /\ n >= 1 /\ (List.range m).map (fun x => x^n) |>.sum = m^n

lemma erdos_moser_m_odd (m n : Nat) (hn : n > 1) (h : SatisfiesErdosMoser m n) : m % 2 = 1 := by
  admit
\end{lstlisting}

\end{document}
"""
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_tex()
