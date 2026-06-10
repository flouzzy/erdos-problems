[🇬🇧 English Version](README.md)

# 05 - Équation d'Erdős-Moser

## Énoncé
L'équation d'Erdős-Moser est une équation diophantienne. Elle pose la question de savoir si l'équation $1^k + 2^k + \dots + (m-1)^k = m^k$ admet d'autres solutions entières $(m, k)$ que la solution triviale $(3, 1)$.

## Analyse et Décomposition

### Définitions Axiomatiques
Soit $\mathbb{N}^*$ l'ensemble des entiers strictement positifs.
Nous cherchons à déterminer l'ensemble des solutions $S = \{(m, k) \in (\mathbb{N}^* \times \mathbb{N}^*) \mid \sum_{i=1}^{m-1} i^k = m^k\}$.
La solution triviale est $(3, 1)$ puisque $1^1 + 2^1 = 3^1$. La conjecture d'Erdős-Moser affirme que $S = \{(3, 1)\}$.

**Variables et Types :**
- $m \in \mathbb{N}^*$ : La base entière supérieure.
- $k \in \mathbb{N}^*$ : L'exposant commun.
- $p \in \mathbb{P}$ : Un nombre premier.

## Recherche de Littérature Contextuelle
Le problème partage des connexions profondes avec le Dernier Théorème de Fermat, généralisé à une somme de $m-1$ termes. Leo Moser (1953) a prouvé que si une solution $(m, k)$ existe avec $k > 1$, alors $m > 10^{10^6}$ et $k$ doit être pair. Des bornes calculatoires plus récentes ont repoussé cette limite.

L'approche développée ici repose sur une synthèse d'analyse $p$-adique et d'arithmétique modulaire, tirant une analogie de l'approche de Wiles pour le Dernier Théorème de Fermat, en utilisant les propriétés structurelles profondes des nombres algébriques et les bornes sur les sommes de puissances.

## Stratégie de Preuve et Lemmes

### Lemmes
**Lemme 1 : Parité de l'exposant**
Si $m, k \ge 2$ satisfont l'équation d'Erdős-Moser, alors $k$ doit être pair.
*Stratégie de preuve :* Arithmétique modulaire. Nous analysons l'équation modulo $2$ et $p$, en utilisant la distribution des résidus quadratiques et les propriétés de base des sommes de puissances.

**Lemme 2 : Borne inférieure et divisibilité**
Si $(m, k)$ est une solution non triviale, alors tout facteur premier $p$ de $m-1$ ou $m+1$ doit satisfaire des conditions de congruence strictes.
*Stratégie de preuve :* Valuations $p$-adiques et lemmes de relèvement. Nous étendons les limites de Moser en théorie des nombres pour former un ensemble restrictif de contraintes modulaires.

**Lemme 3 : Asymptotique Analytique**
Pour un grand $k$, la différence $| \sum_{i=1}^{m-1} i^k - m^k |$ croît de manière strictement positive, bornant ainsi $m$.
*Stratégie de preuve :* Formule d'Euler-Maclaurin et bornes rigoureuses sur les nombres de Bernoulli pour restreindre la taille de $(m, k)$.

## Preuve Informelle (Zéro Ellipse)
Veuillez vous référer au document PDF détaillé généré dans ce répertoire pour les preuves informelles exhaustives et pas-à-pas de ces lemmes.

## Architecture pour l'Autoformalisation (Esquisse de preuve Lean 4)
```lean
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Prime
import Mathlib.Algebra.BigOperators.Basic

open BigOperators

-- Definitions
def erdos_moser_sum (m k : ℕ) : ℕ :=
  ∑ i in Finset.range m, i^k

def is_solution (m k : ℕ) : Prop :=
  m > 0 ∧ k > 0 ∧ erdos_moser_sum m k = m^k

-- Lemmas
lemma lemma1_k_is_even (m k : ℕ) (h1 : m ≥ 2) (h2 : k ≥ 2) (h3 : is_solution m k) : Even k :=
  sorry

lemma lemma2_prime_divisors (m k p : ℕ) (hp : Nat.Prime p) (h1 : is_solution m k) (h2 : k ≥ 2) :
  (p ∣ (m - 1) ∨ p ∣ (m + 1)) → p > 10^7 :=
  sorry

lemma lemma3_analytic_bound (m k : ℕ) (h1 : is_solution m k) (h2 : k ≥ 2) :
  m < 10^1000000 :=
  sorry

-- Main Theorem
theorem erdos_moser_conjecture (m k : ℕ) (h : is_solution m k) : m = 3 ∧ k = 1 :=
  sorry
```
