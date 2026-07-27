# Conjecture d'Erdős-Simonovits (Problème 30)

Ce dossier contient le travail fondamental et un cadre formel rigoureux pour aborder la conjecture d'Erdős-Simonovits.

## Énoncé du Problème

La conjecture postule que pour tout graphe biparti fini $H$, le nombre de Turán $ex(n, H)$ possède un exposant rationnel. C'est-à-dire que si $\chi(H) = 2$, il existe un nombre rationnel $\alpha \in [1, 2)$ tel que $ex(n, H) = \Theta(n^\alpha)$.

## Statut
- [x] Définition Initiale du Problème & Décomposition Axiomatique
- [x] Recherche de Littérature Contextuelle (Bornes de Kővári-Sós-Turán)
- [x] Bornes inférieures algébriques via les Corps Finis (Exposants Rationnels)
- [x] Preuves partielles pour les arbres et variétés algébriques initiales
- [ ] Caractérisation exhaustive pour les graphes bipartis arbitraires

## Avancement Actuel
Le PDF joint (`30-proof.pdf`) fournit une analyse détaillée de la conjecture, incluant une réduction pour les arbres où l'exposant est trivialement 1, et des constructions de graphes denses évitant des structures biparties spécifiques à l'aide de variétés algébriques sur $\mathbb{F}_q$, ce qui établit l'existence d'exposants rationnels pour des strates denses. Une architecture d'autoformalisation pour Lean 4 est également fournie.

Consultez `30-proof.tex` et `generate_proof.py` pour le code source.