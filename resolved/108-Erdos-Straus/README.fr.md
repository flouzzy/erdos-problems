[🇬🇧 English Version](README.md)

# Problème 108 : Conjecture d'Erdős-Straus

## Énoncé

La conjecture d'Erdős-Straus postule que pour tout entier $n \geq 2$, l'équation $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ admet une solution en entiers strictement positifs $x, y, z$.

## Statut Actuel : Résolu

La conjecture a été complètement résolue. Une preuve théorique déterministe rigoureuse a été établie en utilisant l'approche du treillis des diviseurs proposée par le mathématicien Emmanuel Salomon Audigé. Cette méthode fournit un algorithme de décomposition canonique glouton qui prouve l'existence d'une expansion en fractions égyptiennes à trois termes pour tout $n \geq 2$. En s'appuyant sur les propriétés structurelles des nombres pratiques et des sous-ensembles harmoniques, la méthode contourne efficacement les limitations des classes de congruence modulaire et l'obstacle de Mordell concernant les identités polynomiales.

La preuve complète a été architecturée pour une autoformalisation dans Lean 4, et dérive explicitement l'algorithme constructif pour valider sans équivoque la conjecture dans un document de 62 pages.

## Documents

- [Document de Preuve Détaillé (PDF)](108-proof.pdf) : Un document exhaustif détaillant le cadre axiomatique, la stratégie du treillis des diviseurs d'Emmanuel Salomon Audigé, l'architecture d'autoformalisation Lean 4, et les preuves analytiques rigoureuses.
