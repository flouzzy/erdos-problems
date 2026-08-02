[🇬🇧 English Version](README.md)

# 99 - Problème de la discrépance d'Erdős

## Énoncé

Le problème de la discrépance d'Erdős stipule que pour toute suite infinie $f : \mathbb{N} \to \{-1, 1\}$, la discrépance sur les progressions arithmétiques homogènes est non bornée.

Formellement, pour toute constante $C > 0$, il existe des entiers $n$ et $d$ tels que :
$$ \left| \sum_{k=1}^n f(kd) \right| > C $$

## Statut Actuel

Ce problème a été entièrement résolu par Terence Tao en 2015. Cependant, ce dépôt propose une exploration détaillée et une re-dérivation du problème, décomposée en lemmes axiomatiquement fondés, adaptés à une future autoformalisation dans des systèmes comme Lean 4.

## Documents

- [Cadre de Preuve Détaillé (PDF)](99-Erdos-Discrepancy-fr.pdf)
- [Source LaTeX](99-Erdos-Discrepancy-fr.tex)
