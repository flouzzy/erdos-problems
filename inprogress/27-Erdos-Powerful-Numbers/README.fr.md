# 27-Erdos-Powerful-Numbers

## Aperçu du Problème

La conjecture d'Erdős sur les nombres puissants stipule qu'il n'existe pas trois nombres puissants consécutifs. Un entier strictement positif $n$ est dit puissant si, pour tout nombre premier $p$ divisant $n$, $p^2$ divise également $n$.

Bien qu'il existe des paires de nombres puissants consécutifs (par exemple, 8 et 9), il est conjecturé que les contraintes diophantiennes deviennent trop rigides pour permettre à trois d'entre eux de se suivre.

## Progrès Actuel

Ce répertoire contient une analyse diophantienne rigoureuse et une décomposition de la preuve en trois lemmes, résolvant les contraintes de parité locales et établissant l'architecture formelle pour l'autoformalisation sous Lean 4.

### Contenu :
- `27-Erdos-Powerful-Numbers.tex` / `pdf` : Document théorique exhaustif et esquisses de preuves (18 pages).
- `generate_tex.py` : Script Python utilisé pour générer le document LaTeX programmatiquement.
