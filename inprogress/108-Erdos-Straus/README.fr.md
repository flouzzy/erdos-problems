[🇬🇧 English Version](README.md)

# Problème 108 : Conjecture d'Erdős-Straus

## Énoncé

La conjecture d'Erdős-Straus postule que pour tout entier $n \geq 2$, l'équation $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ admet une solution en entiers strictement positifs $x, y, z$.

## Statut Actuel : En Cours

Un cadre axiomatique rigoureux a été établi, décomposant le problème en lemmes intermédiaires via l'arithmétique modulaire et des identités polynomiales. Une esquisse de preuve formelle, conçue pour l'autoformalisation dans Lean 4, a été construite. Des preuves constructives explicites pour $n \in [2, 1000]$ ont été vérifiées informatiquement pour valider l'approche théorique et fournir un ancrage empirique substantiel.

## Documents

- [Document de Preuve Détaillé (PDF)](108-proof.pdf) : Un document exhaustif de 37 pages détaillant le cadre axiomatique, la stratégie, l'architecture d'autoformalisation, et les preuves constructives explicites.
