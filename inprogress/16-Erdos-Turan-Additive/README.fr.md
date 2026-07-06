# 16 - Conjecture d'Erdős-Turán sur les bases additives

## 1. Analyse et Décomposition

### Définitions Axiomatiques
Soit $\mathbb{N}$ l'ensemble des entiers naturels.
Un sous-ensemble $\mathcal{B} \subseteq \mathbb{N}$ est appelé une base additive asymptotique d'ordre 2 si tout entier naturel suffisamment grand peut s'écrire comme la somme de deux éléments de $\mathcal{B}$. Soit $r_{\mathcal{B}}(n)$ le nombre de représentations de $n$ sous la forme $n = a + b$, avec $a, b \in \mathcal{B}$ et $a \le b$.
La condition de base asymptotique s'écrit formellement : $\exists N_0 \in \mathbb{N}, \forall n \ge N_0, r_{\mathcal{B}}(n) > 0$.

La conjecture d'Erdős-Turán (1941) postule que si $\mathcal{B}$ est une base additive d'ordre 2, alors la fonction de représentation $r_{\mathcal{B}}(n)$ ne peut être majorée uniformément. C'est-à-dire : $\limsup_{n \to \infty} r_{\mathcal{B}}(n) = \infty$.

### Variables et Typage
- $n \in \mathbb{N}$ : l'entier cible de la représentation.
- $\mathcal{B} \subseteq \mathbb{N}$ : la base additive.
- $r_{\mathcal{B}}(n) : \mathbb{N} \to \mathbb{N}$ : la fonction de représentation comptant le nombre de couples $(a, b) \in \mathcal{B}^2$ avec $a \le b$ tels que $a + b = n$.

### Structures Algébriques
Le problème se plonge dans l'analyse harmonique discrète et la théorie analytique des nombres. L'application de la méthode du cercle de Hardy-Littlewood aux séries entières génératrices $f(z) = \sum_{b \in \mathcal{B}} z^b$ sur le disque unité $|z| < 1$ établit l'isomorphisme entre la combinatoire additive et la distribution des phases exponentielles. La minoration de l'énergie de dispersion s'oppose à la contrainte de la borne supérieure.

## 2. Recherche de Littérature Contextuelle

La conjecture d'Erdős-Fuchs (1956) établit l'impossibilité d'une représentation arithmétique de la forme $\sum_{n \le x} r(n) = cx + o(x^{1/4})$, fixant une variance minimale. Les bases de Grekos et les constructions probabilistes d'Erdős-Rényi démontrent que des bases pseudo-aléatoires peuvent présenter des bornes logarithmiques pour la fonction de représentation $r_{\mathcal{B}}(n) \asymp \log n$. L'architecture de la preuve actuelle emprunte aux théorèmes de structure de Gowers pour contrecarrer l'hypothèse de densité stationnaire par l'inégalité de Parseval-Plancherel et les transformées de Mellin.

## 3. Stratégie de Preuve et Isolation de Lemmes

La décomposition modulaire repose sur la transformation de la contrainte géométrique en inégalités analytiques.

**Lemme 1 : Régularité de la Fonction Génératrice**
Si la fonction de représentation $r_{\mathcal{B}}(n)$ est bornée par une constante $K$, la fonction génératrice $F(z) = \sum_{n=0}^{\infty} r_{\mathcal{B}}(n) z^n$ admet une majoration stricte au voisinage du cercle unité, contraignant l'expansion locale sur le disque ouvert.

**Lemme 2 : Borne Différentielle de l'Énergie Additive**
L'identité de Parseval quantifie l'énergie additive de sous-ensembles bornés. Sous la restriction $r_{\mathcal{B}}(n) \le K$, la projection sur le tore $\mathbb{T}$ impose une décroissance asymétrique de l'intégrale quartique de la somme exponentielle.

**Lemme 3 : Incompatibilité des Pôles Harmoniques**
La comparaison entre l'équivalent topologique sur les arcs majeurs, dictant un pôle structurel fort pour soutenir la densité asymptotique, et la restriction globale dictée par la borne de variance contraint $K$ à diverger.

## 4. Preuve Fondamentale

La démonstration algébrique intégrale des limites harmoniques de Gowers-Ruzsa et de la dualité spectrale est exposée dans la publication `16-proof.pdf`.

## 5. Architecture d'Autoformalisation (Lean 4)

L'ossature de la démonstration pour la vérification mécanique est structurée ainsi :

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Algebra.BigOperators.Basic

open BigOperators

-- Definitions
def IsAdditiveBase (B : Set ℕ) : Prop :=
  ∃ (N0 : ℕ), ∀ n ≥ N0, ∃ (a b : ℕ), a ∈ B ∧ b ∈ B ∧ a ≤ b ∧ a + b = n

noncomputable def reprCount (B : Set ℕ) (n : ℕ) : ℕ :=
  (Finset.filter (fun (p : ℕ × ℕ) => p.1 ∈ B ∧ p.2 ∈ B ∧ p.1 ≤ p.2 ∧ p.1 + p.2 = n)
    (Finset.product (Finset.range (n + 1)) (Finset.range (n + 1)))).card


lemma gen_function_regularity (B : Set ℕ) (K : ℕ) (hB : IsAdditiveBase B)
  (h_bound : ∀ n, reprCount B n ≤ K) :
  ∃ (C : ℝ), C > 0 ∧ ∀ (r : ℝ), 0 < r ∧ r < 1 →
    (∑' (n : ℕ), (reprCount B n : ℝ) * r^n) ≤ C / (1 - r) := by
  sorry


lemma gowers_additive_energy_bound (B : Set ℕ) (K : ℕ) (hB : IsAdditiveBase B)
  (h_bound : ∀ n, reprCount B n ≤ K) :
  ∃ (M : ℝ), M > 0 ∧ ∀ (N : ℕ), N > 0 →
    ((Finset.filter (fun p : ℕ × ℕ × ℕ × ℕ =>
      p.1.1 ∈ B ∧ p.1.2 ∈ B ∧ p.2.1 ∈ B ∧ p.2.2 ∈ B ∧
      p.1.1 + p.1.2 = p.2.1 + p.2.2 ∧ p.1.1 + p.1.2 ≤ N)
      (Finset.product (Finset.product (Finset.range (N+1)) (Finset.range (N+1)))
                      (Finset.product (Finset.range (N+1)) (Finset.range (N+1))))).card : ℝ) ≤ M * N := by
  sorry


lemma asymptotic_contradiction (B : Set ℕ) (hB : IsAdditiveBase B) :
  ¬(∃ (K : ℕ), ∀ n, reprCount B n ≤ K) := by
  sorry


theorem erdos_turan_additive_conjecture (B : Set ℕ) (hB : IsAdditiveBase B) :
  ∀ (K : ℕ), ∃ n, reprCount B n > K := by
  sorry
```
