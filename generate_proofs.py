import os
import subprocess

def replace_unicode(text):
    replacements = {
        'ℝ': r'\mathbb{R}',
        'ℕ': r'\mathbb{N}',
        '∃': r'\exists',
        '∀': r'\forall',
        '∈': r'\in',
        '≠': r'\neq'
    }

    parts = text.split(r'\begin{verbatim}')
    result = parts[0]
    for part in parts[1:]:
        subparts = part.split(r'\end{verbatim}')
        if len(subparts) == 2:
            lean_block = subparts[0]
            rest = subparts[1]
            lean_block = lean_block.replace('∣', r'\|') # replace standard divides unicode inside Lean block

            for k, v in replacements.items():
                rest = rest.replace(k, v)

            result += r'\begin{verbatim}' + lean_block + r'\end{verbatim}' + rest
        else:
            result += r'\begin{verbatim}' + part

    for k, v in replacements.items():
        result = result.replace(k, v)

    return result

def generate_tex_content(lang='en'):
    if lang == 'en':
        content = r"""\documentclass[11pt, a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{hyperref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{definition}[theorem]{Definition}

\title{Analysis and Partial Results on the Erd\H{o}s-Straus Conjecture}
\author{Charles EDOU NZE\thanks{Charles EDOU NZE, chercheur indépendant}}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
The Erd\H{o}s-Straus conjecture postulates that for every integer $n \geq 2$, there exist positive integers $x, y, z$ such that $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$. In this document, we present an in-depth analysis of the conjecture, decomposing it into modular arithmetic lemmas, accompanied by a literature review, and outlining a structured proof strategy suitable for autoformalization in systems such as Lean 4.
\end{abstract}

\section{Introduction and Formal Statement}

The problem, formulated by Paul Erd\H{o}s and Ernst G. Straus in 1948, is a central question in the additive theory of numbers, specifically concerning representations by unit fractions (Egyptian fractions).

\begin{conjecture}[Erd\H{o}s-Straus]
For all integers $n \geq 2$, there exist positive integers $x, y, z$ such that
\begin{equation}
\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}
\end{equation}
\end{conjecture}

Multiplying both sides by the product $nxyz$, we obtain the equivalent Diophantine equation:
\begin{equation}
4xyz = n(xy + yz + zx)
\end{equation}

\section{Contextual Literature Search}

The asymptotic bounds on the number of solutions to the Erd\H{o}s-Straus equation have been extensively studied. A foundational result by Vaughan (1970) provides a lower bound on the number of $n \leq N$ for which the conjecture holds, demonstrating that the exceptional set is of density zero. Recent advancements have focused on bounding the exceptional set further. Elsholtz and Tao (2013) established sophisticated bounds using sieve methods, proving that the number of counterexamples up to $N$ is $O(N \exp(-c \log N / \log \log N))$.

This problem bears significant structural analogies to the weak Goldbach conjecture (resolved by Helfgott in 2013), where additive decomposition over primes was handled via the Hardy-Littlewood circle method and rigorous computational bounds. The tools developed for sieving and characterizing dense subsets in Goldbach's problem share deep theoretical connections with the modular restrictions defining the Erd\H{o}s-Straus conjecture, suggesting that advanced sieves combined with algebraic geometry over finite fields may eventually yield a complete resolution.

\section{Methodology and Algebraic Structure}

The standard approach to the Erd\H{o}s-Straus conjecture is to analyze the equation modulo various integers. If a solution exists for some integer $n$, and if $m$ divides $n$, then by substitution, a solution also exists for $m$. Therefore, it suffices to prove the conjecture for prime numbers $p$. We partition the primes into residue classes modulo $q$ for specific small integers $q$ (e.g., $q=24$) and construct explicit rational functions for each class.

Let us define the type for a solution: a tuple $(x, y, z) ∈ (ℕ^*)^3$.

\subsection{Lemma 1: Solutions for primes $p \equiv 3 \pmod 4$}

\begin{lemma}
For any prime $p$, if $p \equiv 3 \pmod 4$, then there exist positive integers $x, y, z$ such that $\frac{4}{p} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$.
\end{lemma}

\begin{proof}
Let $p$ be a prime such that $p \equiv 3 \pmod 4$. By the definition of congruences, there exists an integer $k ∈ ℕ^*$ such that $p = 4k - 1$.
Consequently, $p + 1 = 4k$. We construct an explicit parameterization by setting the variables $x, y, z$ as follows:
\begin{align}
x &= 2k = \frac{p+1}{2} \\
y &= 2k = \frac{p+1}{2} \\
z &= k(4k-1) = \frac{p+1}{4}p
\end{align}
We now verify the sum of the unit fractions strictly:
\begin{equation}
\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \frac{1}{2k} + \frac{1}{2k} + \frac{1}{k(4k-1)}
\end{equation}
Combining the first two terms yields:
\begin{equation}
\frac{1}{2k} + \frac{1}{2k} = \frac{2}{2k} = \frac{1}{k}
\end{equation}
Substituting this back into the sum, we obtain:
\begin{equation}
\frac{1}{k} + \frac{1}{k(4k-1)}
\end{equation}
To add these fractions, we find a common denominator, which is $k(4k-1)$:
\begin{equation}
\frac{1}{k} = \frac{4k-1}{k(4k-1)}
\end{equation}
Therefore, the sum becomes:
\begin{equation}
\frac{4k-1}{k(4k-1)} + \frac{1}{k(4k-1)} = \frac{4k - 1 + 1}{k(4k-1)}
\end{equation}
Simplifying the numerator:
\begin{equation}
\frac{4k}{k(4k-1)}
\end{equation}
Since $k ∈ ℕ^*$, $k ≠ 0$, we can divide the numerator and denominator by $k$:
\begin{equation}
\frac{4}{4k-1}
\end{equation}
Recalling our initial substitution $p = 4k-1$, we conclude:
\begin{equation}
\frac{4}{4k-1} = \frac{4}{p}
\end{equation}
This explicitly constructs the solution for all primes $p \equiv 3 \pmod 4$.
\end{proof}

\section{Architecture for Autoformalization}

To facilitate formal verification in Lean 4, we define the following structure:

\begin{verbatim}
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Prime
import Mathlib.Algebra.Order.Ring.Defs

def ErdosStrausProperty (n : \mathbb{N}) : Prop :=
  \exists x y z : \mathbb{N}, x > 0 \land y > 0 \land z > 0 \land 4 * x * y * z = n * (x * y + y * z + z * x)

lemma erdos_straus_mod_4_eq_3 (k : \mathbb{N}) (hk : k > 0) : ErdosStrausProperty (4 * k - 1) := by
  sorry
\end{verbatim}

\end{document}
"""
    else:
        content = r"""\documentclass[11pt, a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[french]{babel}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{geometry}
\geometry{margin=2.5cm}
\usepackage{hyperref}

\newtheorem{theoreme}{Théorème}[section]
\newtheorem{lemme}[theoreme]{Lemme}
\newtheorem{conjecture}[theoreme]{Conjecture}
\newtheorem{definition}[theoreme]{Définition}

\title{Analyse et Résultats Partiels sur la Conjecture d'Erd\H{o}s-Straus}
\author{Charles EDOU NZE\thanks{Charles EDOU NZE, chercheur indépendant}}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
La conjecture d'Erd\H{o}s-Straus postule que pour tout entier $n \geq 2$, il existe des entiers strictement positifs $x, y, z$ tels que $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$. Dans ce document, nous présentons une analyse approfondie de la conjecture, en la décomposant en lemmes d'arithmétique modulaire, accompagnée d'une revue de littérature, et en esquissant une stratégie de preuve structurée adaptée à l'autoformalisation dans des systèmes tels que Lean 4.
\end{abstract}

\section{Introduction et Énoncé Formel}

Le problème, formulé par Paul Erd\H{o}s et Ernst G. Straus en 1948, est une question centrale en théorie additive des nombres, concernant spécifiquement les représentations par fractions unitaires (fractions égyptiennes).

\begin{conjecture}[Erd\H{o}s-Straus]
Pour tout entier $n \geq 2$, il existe des entiers strictement positifs $x, y, z$ tels que
\begin{equation}
\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}
\end{equation}
\end{conjecture}

En multipliant les deux côtés par le produit $nxyz$, nous obtenons l'équation diophantienne équivalente :
\begin{equation}
4xyz = n(xy + yz + zx)
\end{equation}

\section{Recherche de Littérature Contextuelle}

Les bornes asymptotiques sur le nombre de solutions à l'équation d'Erd\H{o}s-Straus ont été largement étudiées. Un résultat fondamental de Vaughan (1970) fournit une borne inférieure sur le nombre de $n \leq N$ pour lesquels la conjecture est vérifiée, démontrant que l'ensemble exceptionnel est de densité nulle. Les avancées récentes se sont concentrées sur la majoration supplémentaire de l'ensemble exceptionnel. Elsholtz et Tao (2013) ont établi des bornes sophistiquées utilisant des méthodes de crible, prouvant que le nombre de contre-exemples jusqu'à $N$ est un $O(N \exp(-c \log N / \log \log N))$.

Ce problème présente d'importantes analogies structurelles avec la conjecture faible de Goldbach (résolue par Helfgott en 2013), où la décomposition additive sur les nombres premiers a été traitée via la méthode du cercle de Hardy-Littlewood et des bornes computationnelles rigoureuses. Les outils développés pour le criblage et la caractérisation des sous-ensembles denses dans le problème de Goldbach partagent de profondes connexions théoriques avec les restrictions modulaires définissant la conjecture d'Erd\H{o}s-Straus, suggérant que des cribles avancés combinés à la géométrie algébrique sur les corps finis pourraient éventuellement conduire à une résolution complète.

\section{Méthodologie et Structure Algébrique}

L'approche standard pour la conjecture d'Erd\H{o}s-Straus consiste à analyser l'équation modulo différents entiers. Si une solution existe pour un entier $n$, et si $m$ divise $n$, alors par substitution, une solution existe également pour $m$. Par conséquent, il suffit de prouver la conjecture pour les nombres premiers $p$. Nous partitionnons les nombres premiers en classes de résidus modulo $q$ pour de petits entiers spécifiques $q$ (par exemple, $q=24$) et construisons des fonctions rationnelles explicites pour chaque classe.

Définissons le type pour une solution : un uplet $(x, y, z) ∈ (ℕ^*)^3$.

\subsection{Lemme 1 : Solutions pour les premiers $p \equiv 3 \pmod 4$}

\begin{lemme}
Pour tout nombre premier $p$, si $p \equiv 3 \pmod 4$, alors il existe des entiers strictement positifs $x, y, z$ tels que $\frac{4}{p} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$.
\end{lemme}

\begin{proof}
Soit $p$ un nombre premier tel que $p \equiv 3 \pmod 4$. Par la définition des congruences, il existe un entier $k ∈ ℕ^*$ tel que $p = 4k - 1$.
Par conséquent, $p + 1 = 4k$. Nous construisons un paramétrage explicite en fixant les variables $x, y, z$ comme suit :
\begin{align}
x &= 2k = \frac{p+1}{2} \\
y &= 2k = \frac{p+1}{2} \\
z &= k(4k-1) = \frac{p+1}{4}p
\end{align}
Nous vérifions maintenant strictement la somme des fractions unitaires :
\begin{equation}
\frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \frac{1}{2k} + \frac{1}{2k} + \frac{1}{k(4k-1)}
\end{equation}
La combinaison des deux premiers termes donne :
\begin{equation}
\frac{1}{2k} + \frac{1}{2k} = \frac{2}{2k} = \frac{1}{k}
\end{equation}
En substituant ce résultat dans la somme, nous obtenons :
\begin{equation}
\frac{1}{k} + \frac{1}{k(4k-1)}
\end{equation}
Pour additionner ces fractions, nous trouvons un dénominateur commun, qui est $k(4k-1)$ :
\begin{equation}
\frac{1}{k} = \frac{4k-1}{k(4k-1)}
\end{equation}
Ainsi, la somme devient :
\begin{equation}
\frac{4k-1}{k(4k-1)} + \frac{1}{k(4k-1)} = \frac{4k - 1 + 1}{k(4k-1)}
\end{equation}
Simplification du numérateur :
\begin{equation}
\frac{4k}{k(4k-1)}
\end{equation}
Puisque $k ∈ ℕ^*$, $k ≠ 0$, nous pouvons diviser le numérateur et le dénominateur par $k$ :
\begin{equation}
\frac{4}{4k-1}
\end{equation}
Rappelant notre substitution initiale $p = 4k-1$, nous concluons :
\begin{equation}
\frac{4}{4k-1} = \frac{4}{p}
\end{equation}
Ceci construit explicitement la solution pour tous les nombres premiers $p \equiv 3 \pmod 4$.
\end{proof}

\section{Architecture pour l'Autoformalisation}

Pour faciliter la vérification formelle dans Lean 4, nous définissons la structure suivante :

\begin{verbatim}
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Prime
import Mathlib.Algebra.Order.Ring.Defs

def ErdosStrausProperty (n : \mathbb{N}) : Prop :=
  \exists x y z : \mathbb{N}, x > 0 \land y > 0 \land z > 0 \land 4 * x * y * z = n * (x * y + y * z + z * x)

lemma erdos_straus_mod_4_eq_3 (k : \mathbb{N}) (hk : k > 0) : ErdosStrausProperty (4 * k - 1) := by
  sorry
\end{verbatim}

\end{document}
"""
    return replace_unicode(content)

def main():
    base_dir = "inprogress/109-Erdos-Straus"
    en_file = os.path.join(base_dir, "109-Erdos-Straus.tex")
    fr_file = os.path.join(base_dir, "109-Erdos-Straus-fr.tex")

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(generate_tex_content('en'))

    with open(fr_file, 'w', encoding='utf-8') as f:
        f.write(generate_tex_content('fr'))

    # Compile EN
    for _ in range(2):
        subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', base_dir, en_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

    # Compile FR
    for _ in range(2):
        subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-output-directory', base_dir, fr_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

if __name__ == '__main__':
    main()
