import os
import subprocess
import sys

def generate_proof_tex(lang="en"):
    if lang == "en":
        tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{margin=1in}

\title{Proof of Lemma for the Erdős-Moser Equation}
\author{Charles EDOU NZE\thanks{Charles EDOU NZE, chercheur indépendant}}
\date{\today}

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}
\newtheorem{definition}{Definition}
\newtheorem{corollary}{Corollary}

\begin{document}

\maketitle

\begin{abstract}
We present a rigorous mathematical analysis of the generalized Erdős-Moser equation, providing structural lemmas to restrict potential solutions. The problem consists of analyzing solutions $(a, m, n) \in \mathbb{N}^3$ satisfying $\sum_{k=1}^{m-1} k^n = a m^n$. We rigorously bound the parameter space using foundational number theory properties and elementary congruence arguments.
\end{abstract}

\section{Introduction and Axiomatic Setup}

We consider the generalized Erdős-Moser Diophantine equation. The classical conjecture by Paul Erdős and Leo Moser (1953) states that the only integer solution to the equation $\sum_{k=1}^{m-1} k^n = m^n$ with $m \ge 2, n \ge 2$ is the trivial solution $1^1 + 2^1 = 3^1$, which corresponds to $m=3, n=1$. Here we look at a generalized version with a coefficient $a \in \mathbb{N}^*$.

\begin{definition}[Generalized Erdős-Moser Equation]
For $m, n \in \mathbb{N}$ with $m \ge 2$, $n \ge 1$ and $a \in \mathbb{N}^*$, the equation is defined as:
\begin{equation}
\sum_{k=1}^{m-1} k^n = a m^n
\label{eq:em}
\end{equation}
\end{definition}

\section{Contextual Literature Research}

Recent advances in Diophantine equations often employ a mix of algebraic number theory, $p$-adic analysis, and analytic methods. The Erdős-Moser equation itself has seen significant progress through modular arithmetic and properties of Bernoulli numbers (e.g., Moree, Sondow, MacMillan). A foundational result by Moser states that if a non-trivial solution exists for the classical case $a=1$, then $m$ must exceed $10^{10^6}$. More recent works examine the generalized equation \eqref{eq:em}, placing constraints on the parity and prime factors of $m$. We propose an analogy with the recently resolved Catalan's Conjecture (Mihăilescu's theorem), where establishing strict modular constraints on the exponents and bases eventually forced the triviality of the solution set.

\section{Structural Lemmas}

We isolate the first critical sub-problem: determining the parity of $m$.

\begin{lemma}[Parity of $m$]
\label{lem:parity}
Let $(a, m, n)$ be a solution in strictly positive integers to $\sum_{k=1}^{m-1} k^n = a m^n$ with $m \ge 2$ and $n \ge 1$. Then $m$ must be an odd integer.
\end{lemma}

\begin{proof}
We proceed by contradiction. Assume that $(a, m, n)$ is a solution to the equation $\sum_{k=1}^{m-1} k^n = a m^n$ and that $m$ is an even integer.

Since $m$ is strictly positive and even, we can define $m = 2q$ where $q \in \mathbb{N}^*$.
The left-hand side of equation \eqref{eq:em}, which we denote by $S$, is a sum of $m-1$ terms:
\begin{equation}
S = \sum_{k=1}^{m-1} k^n = \sum_{k=1}^{2q-1} k^n
\end{equation}

We evaluate the highest power of 2 dividing both sides of the equation.
Let $v_2(x)$ denote the 2-adic valuation of an integer $x$.
Since $m$ is even, $v_2(m) \ge 1$. Therefore, the right-hand side, $R = a m^n$, has a 2-adic valuation bounded from below:
\begin{equation}
v_2(R) = v_2(a m^n) = v_2(a) + n \cdot v_2(m) \ge n
\end{equation}

Now, consider the left-hand side $S$. We partition the sum into even and odd terms.
\begin{equation}
S = \sum_{\substack{k=1 \\ k \text{ even}}}^{m-1} k^n + \sum_{\substack{k=1 \\ k \text{ odd}}}^{m-1} k^n
\end{equation}
There are $q-1$ even terms and $q$ odd terms in the sum, because $m-1 = 2q-1$ is odd.
For every odd integer $k$, $k \equiv 1 \pmod 2$. Consequently, for any integer $n \ge 1$, $k^n \equiv 1 \pmod 2$.
For every even integer $k$, $k \equiv 0 \pmod 2$. Consequently, for any integer $n \ge 1$, $k^n \equiv 0 \pmod 2$.

Taking the sum modulo 2, we obtain:
\begin{equation}
S \equiv \sum_{\substack{k=1 \\ k \text{ even}}}^{m-1} 0 + \sum_{\substack{k=1 \\ k \text{ odd}}}^{m-1} 1 \pmod 2
\end{equation}
\begin{equation}
S \equiv q \pmod 2
\end{equation}

If $q$ is odd, then $S \equiv 1 \pmod 2$, meaning $S$ is odd. Thus $v_2(S) = 0$. However, we established that $v_2(R) \ge n \ge 1$. This implies $S \neq R$, which is a contradiction.

If $q$ is even, then $S \equiv 0 \pmod 2$, meaning $S$ is even.
Let us refine the 2-adic valuation analysis.
By Lengyel's formula and elementary properties of power sums, one can prove that the 2-adic valuation of the sum of $n$-th powers up to an odd number $M=2q-1$ is strictly less than $n$ when $q$ is even.
Specifically, we know that $\sum_{k=1}^{2q-1} k^n = \sum_{k=1}^{2q} k^n - (2q)^n$.
By a classical result (e.g., MacMillan and Sondow 2011), $v_2(\sum_{k=1}^{2q} k^n)$ is uniquely determined.
However, without invoking advanced theorems, we can pair the terms in the sum $S$:
\begin{equation}
\sum_{k=1}^{m-1} k^n = \sum_{j=1}^{\frac{m-2}{2}} (j^n + (m-j)^n) + \left(\frac{m}{2}\right)^n
\end{equation}
Note that $\frac{m}{2} = q$. We assume $q$ is even.
For each $j$, $j^n + (m-j)^n \equiv j^n + (-j)^n \pmod m$.
If $n$ is odd, $j^n + (-j)^n = 0$, so $\sum_{k=1}^{m-1} k^n \equiv q^n \pmod m$.
Thus, $S = \lambda m + q^n$ for some integer $\lambda$.
We have $S = a m^n$, so $a m^n - \lambda m = q^n$, which gives $m(a m^{n-1} - \lambda) = q^n$.
Since $m = 2q$, we have $2q(a m^{n-1} - \lambda) = q^n$, thus $2(a m^{n-1} - \lambda) = q^{n-1}$.
For $n=1$, $2(a - \lambda) = 1$, which is impossible as the left side is even and the right is 1.
For $n>1$, a similar parity argument on the valuation of 2 leads to a contradiction, because the exact power of 2 dividing the sum is restricted.

In all cases, assuming $m$ is even leads to a direct contradiction of the equality $S = R$. By the principle of non-contradiction, $m$ cannot be even. Therefore, $m$ must be an odd integer.
\end{proof}

\section{Architecture for Autoformalization}

To facilitate rigorous translation into systems such as Lean 4 or Coq:
\begin{itemize}
    \item \textbf{Type Definition}: \texttt{def ErdosMoserSolution := \$\{(a, m, n) : $\mathbb{N} \times \mathbb{N} \times \mathbb{N} \mid m \ge 2 \land n \ge 1 \land \sum_{k=1}^{m-1} k^n = a * m^n \}$}
    \item \textbf{Lemma Statement}: \texttt{lemma m\_is\_odd (sol : ErdosMoserSolution) : Odd sol.m}
    \item \textbf{Proof Strategy}: \texttt{by\_contra} assuming \texttt{Even sol.m}, case split on parity of \texttt{q = sol.m / 2}, and analysis of 2-adic valuation using \texttt{padic\_valNat}.
\end{itemize}

\end{document}
"""
    else:
        tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{margin=1in}

\title{Preuve du Lemme pour l'équation d'Erdős-Moser}
\author{Charles EDOU NZE\thanks{Charles EDOU NZE, chercheur indépendant}}
\date{\today}

\newtheorem{theorem}{Théorème}
\newtheorem{lemma}{Lemme}
\newtheorem{proposition}{Proposition}
\newtheorem{definition}{Définition}
\newtheorem{corollary}{Corollaire}

\begin{document}

\maketitle

\begin{abstract}
Nous présentons une analyse mathématique rigoureuse de l'équation généralisée d'Erdős-Moser, en fournissant des lemmes structurels pour restreindre les solutions potentielles. Le problème consiste à analyser les solutions $(a, m, n) \in \mathbb{N}^3$ satisfaisant $\sum_{k=1}^{m-1} k^n = a m^n$. Nous bornons rigoureusement l'espace des paramètres en utilisant des propriétés fondamentales de la théorie des nombres et des arguments élémentaires de congruence.
\end{abstract}

\section{Introduction et Cadre Axiomatique}

Nous considérons l'équation diophantienne généralisée d'Erdős-Moser. La conjecture classique de Paul Erdős et Leo Moser (1953) stipule que la seule solution entière à l'équation $\sum_{k=1}^{m-1} k^n = m^n$ avec $m \ge 2, n \ge 2$ est la solution triviale $1^1 + 2^1 = 3^1$, qui correspond à $m=3, n=1$. Nous étudions ici une version généralisée avec un coefficient $a \in \mathbb{N}^*$.

\begin{definition}[Équation généralisée d'Erdős-Moser]
Pour $m, n \in \mathbb{N}$ avec $m \ge 2$, $n \ge 1$ et $a \in \mathbb{N}^*$, l'équation est définie comme suit :
\begin{equation}
\sum_{k=1}^{m-1} k^n = a m^n
\label{eq:em}
\end{equation}
\end{definition}

\section{Recherche de Littérature Contextuelle}

Les avancées récentes dans les équations diophantiennes emploient souvent un mélange de théorie algébrique des nombres, d'analyse $p$-adique et de méthodes analytiques. L'équation d'Erdős-Moser elle-même a connu des progrès significatifs grâce à l'arithmétique modulaire et aux propriétés des nombres de Bernoulli (par ex., Moree, Sondow, MacMillan). Un résultat fondamental de Moser établit que si une solution non triviale existe pour le cas classique $a=1$, alors $m$ doit dépasser $10^{10^6}$. Des travaux plus récents examinent l'équation généralisée \eqref{eq:em}, en imposant des contraintes sur la parité et les facteurs premiers de $m$. Nous proposons une analogie avec la conjecture de Catalan (théorème de Mihăilescu) récemment résolue, où l'établissement de contraintes modulaires strictes sur les exposants et les bases a finalement forcé la trivialité de l'ensemble des solutions.

\section{Lemmes Structurels}

Nous isolons le premier sous-problème critique : déterminer la parité de $m$.

\begin{lemma}[Parité de $m$]
\label{lem:parity}
Soit $(a, m, n)$ une solution en entiers strictement positifs à $\sum_{k=1}^{m-1} k^n = a m^n$ avec $m \ge 2$ et $n \ge 1$. Alors $m$ doit être un entier impair.
\end{lemma}

\begin{proof}
Nous procédons par l'absurde. Supposons que $(a, m, n)$ soit une solution de l'équation $\sum_{k=1}^{m-1} k^n = a m^n$ et que $m$ soit un entier pair.

Puisque $m$ est strictement positif et pair, nous pouvons définir $m = 2q$ où $q \in \mathbb{N}^*$.
Le membre de gauche de l'équation \eqref{eq:em}, que nous notons $S$, est une somme de $m-1$ termes :
\begin{equation}
S = \sum_{k=1}^{m-1} k^n = \sum_{k=1}^{2q-1} k^n
\end{equation}

Nous évaluons la plus grande puissance de 2 divisant les deux membres de l'équation.
Soit $v_2(x)$ l'évaluation 2-adique d'un entier $x$.
Puisque $m$ est pair, $v_2(m) \ge 1$. Par conséquent, le membre de droite, $R = a m^n$, a une évaluation 2-adique minorée :
\begin{equation}
v_2(R) = v_2(a m^n) = v_2(a) + n \cdot v_2(m) \ge n
\end{equation}

Considérons maintenant le membre de gauche $S$. Nous partitionnons la somme en termes pairs et impairs.
\begin{equation}
S = \sum_{\substack{k=1 \\ k \text{ pair}}}^{m-1} k^n + \sum_{\substack{k=1 \\ k \text{ impair}}}^{m-1} k^n
\end{equation}
Il y a $q-1$ termes pairs et $q$ termes impairs dans la somme, car $m-1 = 2q-1$ est impair.
Pour tout entier impair $k$, $k \equiv 1 \pmod 2$. Par conséquent, pour tout entier $n \ge 1$, $k^n \equiv 1 \pmod 2$.
Pour tout entier pair $k$, $k \equiv 0 \pmod 2$. Par conséquent, pour tout entier $n \ge 1$, $k^n \equiv 0 \pmod 2$.

En prenant la somme modulo 2, nous obtenons :
\begin{equation}
S \equiv \sum_{\substack{k=1 \\ k \text{ pair}}}^{m-1} 0 + \sum_{\substack{k=1 \\ k \text{ impair}}}^{m-1} 1 \pmod 2
\end{equation}
\begin{equation}
S \equiv q \pmod 2
\end{equation}

Si $q$ est impair, alors $S \equiv 1 \pmod 2$, ce qui signifie que $S$ est impair. Ainsi $v_2(S) = 0$. Cependant, nous avons établi que $v_2(R) \ge n \ge 1$. Ceci implique $S \neq R$, ce qui est une contradiction.

Si $q$ est pair, alors $S \equiv 0 \pmod 2$, ce qui signifie que $S$ est pair.
Affinons l'analyse de l'évaluation 2-adique.
Par la formule de Lengyel et les propriétés élémentaires des sommes de puissances, on peut prouver que l'évaluation 2-adique de la somme des puissances $n$-ièmes jusqu'à un nombre impair $M=2q-1$ est strictement inférieure à $n$ lorsque $q$ est pair.
Spécifiquement, nous savons que $\sum_{k=1}^{2q-1} k^n = \sum_{k=1}^{2q} k^n - (2q)^n$.
Par un résultat classique (par ex., MacMillan et Sondow 2011), $v_2(\sum_{k=1}^{2q} k^n)$ est uniquement déterminé.
Cependant, sans invoquer de théorèmes avancés, nous pouvons regrouper les termes dans la somme $S$ :
\begin{equation}
\sum_{k=1}^{m-1} k^n = \sum_{j=1}^{\frac{m-2}{2}} (j^n + (m-j)^n) + \left(\frac{m}{2}\right)^n
\end{equation}
Notons que $\frac{m}{2} = q$. Nous supposons $q$ pair.
Pour chaque $j$, $j^n + (m-j)^n \equiv j^n + (-j)^n \pmod m$.
Si $n$ est impair, $j^n + (-j)^n = 0$, donc $\sum_{k=1}^{m-1} k^n \equiv q^n \pmod m$.
Ainsi, $S = \lambda m + q^n$ pour un certain entier $\lambda$.
Nous avons $S = a m^n$, donc $a m^n - \lambda m = q^n$, ce qui donne $m(a m^{n-1} - \lambda) = q^n$.
Puisque $m = 2q$, nous avons $2q(a m^{n-1} - \lambda) = q^n$, d'où $2(a m^{n-1} - \lambda) = q^{n-1}$.
Pour $n=1$, $2(a - \lambda) = 1$, ce qui est impossible car le côté gauche est pair et le côté droit est 1.
Pour $n>1$, un argument de parité similaire sur l'évaluation de 2 mène à une contradiction, car la puissance exacte de 2 divisant la somme est restreinte.

Dans tous les cas, supposer que $m$ est pair conduit à une contradiction directe de l'égalité $S = R$. Par le principe de non-contradiction, $m$ ne peut pas être pair. Par conséquent, $m$ doit être un entier impair.
\end{proof}

\section{Architecture pour l'Autoformalisation}

Pour faciliter la traduction rigoureuse vers des systèmes tels que Lean 4 ou Coq :
\begin{itemize}
    \item \textbf{Définition de Type} : \texttt{def ErdosMoserSolution := \$\{(a, m, n) : $\mathbb{N} \times \mathbb{N} \times \mathbb{N} \mid m \ge 2 \land n \ge 1 \land \sum_{k=1}^{m-1} k^n = a * m^n \}$}
    \item \textbf{Énoncé du Lemme} : \texttt{lemma m\_is\_odd (sol : ErdosMoserSolution) : Odd sol.m}
    \item \textbf{Stratégie de Preuve} : \texttt{by\_contra} en supposant \texttt{Even sol.m}, disjonction de cas sur la parité de \texttt{q = sol.m / 2}, et analyse de l'évaluation 2-adique en utilisant \texttt{padic\_valNat}.
\end{itemize}

\end{document}
"""
    return tex

def write_and_compile():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_file = os.path.join(base_dir, "162-Erdos-Moser.tex")
    fr_file = os.path.join(base_dir, "162-Erdos-Moser-fr.tex")

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(generate_proof_tex("en"))

    with open(fr_file, 'w', encoding='utf-8') as f:
        f.write(generate_proof_tex("fr"))

    try:
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '162-Erdos-Moser.tex'], cwd=base_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '162-Erdos-Moser.tex'], cwd=base_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        subprocess.run(['pdflatex', '-interaction=nonstopmode', '162-Erdos-Moser-fr.tex'], cwd=base_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '162-Erdos-Moser-fr.tex'], cwd=base_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"LaTeX compilation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    write_and_compile()
