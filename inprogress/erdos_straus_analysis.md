# Analyse de la Conjecture d'Erdős-Straus

## 1. Analyse et Décomposition Axiomatique

**Traduction de l'énoncé :**
La conjecture postule que pour tout entier $n \ge 2$, la fraction $\frac{4}{n}$ peut s'écrire comme la somme de trois fractions unitaires (fractions dont le numérateur est 1).

**Typage strict et Définitions Axiomatiques :**
* Soit $\mathbb{N}^*$ l'ensemble des entiers naturels non nuls.
* Soit $n \in \mathbb{N}, n \ge 2$ notre variable d'entrée.
* Soit le triplet solution $(x, y, z) \in (\mathbb{N}^*)^3$.
* L'équation rationnelle s'écrit : $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$
* Pour éviter les singularités liées aux pôles (division par zéro) et travailler dans un anneau, nous multiplions l'équation par le dénominateur commun $n \cdot x \cdot y \cdot z$, ce qui nous donne l'**Hypersurface Diophantienne Axiomatique** $\mathcal{H}_n$ :
  $$P(n, x, y, z) \iff 4xyz = n(xy + yz + zx)$$

**Structures sous-jacentes :**
D'un point de vue de la géométrie algébrique abstraite, pour un $n$ fixé, $\mathcal{H}_n$ définit une *variété de Fano cubique* projective. Le problème revient à prouver que cette variété possède toujours au moins un point rationnel dans le domaine positif strict. Nous allons utiliser l'algèbre modulaire (anneaux $\mathbb{Z}/k\mathbb{Z}$) pour segmenter le problème.

## 2. Recherche de Littérature Contextuelle

* **Théorèmes de densité existants :** Le mathématicien Terence Tao a profondément travaillé sur une conjecture similaire. Sur Erdős-Straus, le résultat majeur est celui de Webb, Vaughan et Elsholtz : en utilisant le crible de Selberg, ils ont prouvé que le nombre de valeurs $n \in [1, N]$ pour lesquelles la conjecture *serait* fausse est borné par $O(N \exp(-c \log^2 N))$. Autrement dit, la conjecture est vraie pour presque tout entier.
* **Analogie avec un problème résolu :** Le Grand Théorème de Fermat prouvé par Andrew Wiles. Fermat a été résolu non pas en attaquant l'équation de front, mais en liant les solutions de l'équation à des objets structurels modulaires. De la même manière, notre stratégie repose sur des "revêtements polynomiaux" : nous allons construire des polynômes $x(k), y(k), z(k)$ qui paramètrent les solutions pour des classes de congruence spécifiques (modulo 4, modulo 3, etc.).

## 3. Stratégie de Preuve & Isolation de Lemmes

Pour démontrer la mécanique du problème, je vais décomposer l'attaque en deux lemmes fondamentaux. Si nous parvenons à couvrir toutes les classes modulo par de tels lemmes, la conjecture totale s'effondre et devient un Théorème.

* **Lemme 1 : Réduction aux nombres premiers.**
  * *Stratégie :* Preuve algébrique par factorisation. Nous utiliserons le Théorème Fondamental de l'Arithmétique pour prouver que si la conjecture est vraie pour les nombres premiers, alors elle est vraie pour tout entier composé.
* **Lemme 2 : Résolution de la classe modulaire $n \equiv 3 \pmod 4$.**
  * *Stratégie :* Preuve par construction explicite et manipulation d'identités égyptiennes. Nous utiliserons la méthode de "l'expansion de la fraction résiduelle" (un dérivé de l'algorithme glouton de Fibonacci-Sylvester).

## 4. Rédaction de la Preuve Informelle (Zéro Ellipse)

Voici la preuve intégrale, pas-à-pas, accessible à un étudiant de première année de Licence.

### Démonstration du Lemme 1 (Réduction aux nombres premiers)
**Énoncé :** Si pour tout nombre premier $p \ge 2$, l'équation admet une solution dans $(\mathbb{N}^*)^3$, alors elle admet une solution pour tout entier $n \ge 2$.

1. Soit $n \ge 2$ un entier composé (non premier).
2. Par le théorème fondamental de l'arithmétique, $n$ peut s'écrire comme le produit d'un nombre premier $p$ et d'un entier $m \ge 1$. Donc $n = p \cdot m$.
3. Supposons (par hypothèse du lemme) que la conjecture est vraie pour ce nombre premier $p$. Il existe donc trois entiers strictement positifs $x_p, y_p, z_p \in \mathbb{N}^*$ tels que :
   $$\frac{4}{p} = \frac{1}{x_p} + \frac{1}{y_p} + \frac{1}{z_p}$$
4. Divisons chaque membre de cette équation par $m$. L'égalité est conservée :
   $$\frac{1}{m} \cdot \left( \frac{4}{p} \right) = \frac{1}{m} \cdot \left( \frac{1}{x_p} + \frac{1}{y_p} + \frac{1}{z_p} \right)$$
5. En développant la multiplication des fractions, on obtient :
   $$\frac{4}{p \cdot m} = \frac{1}{m \cdot x_p} + \frac{1}{m \cdot y_p} + \frac{1}{m \cdot z_p}$$
6. Remplaçons $p \cdot m$ par $n$ (selon la définition à l'étape 2) :
   $$\frac{4}{n} = \frac{1}{m \cdot x_p} + \frac{1}{m \cdot y_p} + \frac{1}{m \cdot z_p}$$
7. Posons de nouvelles variables : $X = m \cdot x_p$, $Y = m \cdot y_p$, et $Z = m \cdot z_p$.
8. Puisque $m \ge 1$ et $x_p, y_p, z_p \ge 1$, le produit d'entiers strictement positifs reste un entier strictement positif. Donc $X, Y, Z \in \mathbb{N}^*$.
9. Nous avons ainsi trouvé une solution $\frac{4}{n} = \frac{1}{X} + \frac{1}{Y} + \frac{1}{Z}$. Le Lemme 1 est démontré. $\blacksquare$

### Démonstration du Lemme 2 (Classe $n \equiv 3 \pmod 4$)
**Énoncé :** Pour tout entier $n$ tel que $n \equiv 3 \pmod 4$, l'équation d'Erdős-Straus admet une solution avec $x, y, z$ distincts.

1. Soit $n \equiv 3 \pmod 4$. Par définition de la congruence, il existe un entier naturel $k \ge 0$ tel que $n = 4k + 3$.
2. Nous cherchons à écrire $\frac{4}{4k+3}$. Posons notre premier dénominateur $x = k+1$.
3. Calculons la différence pour voir ce qu'il reste à combler :
   $$Reste = \frac{4}{4k+3} - \frac{1}{k+1}$$
4. Mettons au même dénominateur, qui est le produit $(4k+3)(k+1)$ :
   $$Reste = \frac{4(k+1) - 1(4k+3)}{(4k+3)(k+1)}$$
5. Développons le numérateur : $4k + 4 - 4k - 3 = 1$.
6. Nous obtenons donc une égalité stricte :
   $$\frac{4}{4k+3} = \frac{1}{k+1} + \frac{1}{(4k+3)(k+1)}$$
7. Nous avons décomposé $\frac{4}{n}$ en *deux* fractions. La conjecture en exige *trois*. Il nous faut donc "casser" la deuxième fraction en deux fractions unitaires.
8. Pour tout entier $A \ge 1$, considérons l'identité algébrique stricte suivante :
   $$\frac{1}{A} = \frac{1}{A+1} + \frac{1}{A(A+1)}$$
9. Appliquons cette identité en posant $A = (4k+3)(k+1)$. Puisque $k \ge 0$, on a $(4k+3) \ge 3$ et $(k+1) \ge 1$, donc $A \ge 3$. L'entier $A$ est bien strictement positif.
10. La fraction résiduelle devient :
    $$\frac{1}{A} = \frac{1}{A+1} + \frac{1}{A(A+1)}$$
11. En réintégrant cela dans notre équation de l'étape 6, nous obtenons notre solution finale à 3 termes :
    $$\frac{4}{4k+3} = \frac{1}{k+1} + \frac{1}{A+1} + \frac{1}{A(A+1)}$$
    Où $A = (4k+3)(k+1)$.
12. **Vérification de la positivité et distinction :**
    Posons $x = k+1$, $y = A+1$, $z = A(A+1)$.
    Puisque $A \ge 3$, on a $x < A < A+1$, donc $x < y$.
    De même, $A \ge 3 \implies A(A+1) > A+1$, donc $y < z$.
    Les trois entiers $x, y, z$ sont dans $\mathbb{N}^*$, strictement ordonnés ($x < y < z$), donc distincts. Le Lemme 2 est irréfutablement démontré. $\blacksquare$

## 5. Architecture pour l'Autoformalisation (Lean 4)

Afin d'armer un système de preuve formelle interactif comme **Lean 4** (ou un agent d'IA formelle type Aristotle), voici le Squelette de Preuve (*Proof Sketch*) typé explicitement. J'isole les prédicats pour éviter l'enfer des coercitions de types entre rationnels et entiers naturels.

```lean
import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Prime

-- 1. Définition Axiomatique du prédicat (évite la division rationnelle)
def ErdosStrausEq (n x y z : ℕ) : Prop :=
  4 * x * y * z = n * (x * y + y * z + z * x)

-- 2. Définition de la validité pour un entier donné
def HasErdosStrausSolution (n : ℕ) : Prop :=
  ∃ x y z : ℕ, x > 0 ∧ y > 0 ∧ z > 0 ∧ ErdosStrausEq n x y z

-- 3. Cible globale de la conjecture
def ErdosStrausConjecture : Prop :=
  ∀ n : ℕ, n ≥ 2 → HasErdosStrausSolution n

-- 4. Autoformalisation du Lemme 1 : Réduction multiplicative
lemma erdos_straus_reduction (p m : ℕ) (hp : HasErdosStrausSolution p) (hm : m > 0) :
  HasErdosStrausSolution (p * m) :=
by
  -- Le squelette attend ici l'extraction de x_p, y_p, z_p depuis hp
  -- Et l'instanciation exacte avec ⟨m * x_p, m * y_p, m * z_p⟩
  sorry

-- 5. Autoformalisation du Lemme 2 : Paramétrisation pour 3 modulo 4
lemma erdos_straus_mod4_3 (k : ℕ) :
  HasErdosStrausSolution (4 * k + 3) :=
by
  -- Instanciation explicite tirée de notre preuve (Zéro Ellipse)
  let x := k + 1
  let A := (4 * k + 3) * (k + 1)
  let y := A + 1
  let z := A * (A + 1)
  use x, y, z
  -- La preuve se termine par la tactique `omega` ou `ring`
  -- pour résoudre l'algèbre polynomiale sur ℕ
  sorry
```
