# Problème 109 : Conjecture d'Erdős-Straus

## Énoncé
La conjecture d'Erdős-Straus postule que pour tout entier $n \geq 2$, le nombre rationnel $4/n$ peut être exprimé comme la somme de trois fractions unitaires positives :

$$ \frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} $$

où $x, y, z$ sont des entiers positifs.

## Statut
**En Cours**

Nous avons établi des lemmes de réduction fondamentaux :
1. **Suffisance pour les Nombres Premiers :** En démontrant que si la conjecture est vérifiée pour les nombres premiers, elle l'est naturellement pour tous les nombres composés.
2. **Réductions par Identités Polynomiales :** En employant des classes de congruence modulo $24$, nous avons construit des identités polynomiales explicites résolvant la conjecture pour les nombres premiers $p \not\equiv 1 \pmod{24}$, réduisant l'espace de recherche à un sous-ensemble épars de nombres premiers.

Les preuves détaillées et l'architecture de formalisation systématique sous Lean 4 sont documentées dans `109-Erdos-Straus-FR.pdf`.
