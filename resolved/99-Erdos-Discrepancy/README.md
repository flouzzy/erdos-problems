[🇫🇷 Version Française](README.fr.md)

# 99 - Erdős Discrepancy Problem

## Statement

The Erdős Discrepancy Problem states that for any infinite sequence $f : \mathbb{N} \to \{-1, 1\}$, the discrepancy on homogeneous arithmetic progressions is unbounded.

Formally, for any constant $C > 0$, there exist integers $n$ and $d$ such that:
$$ \left| \sum_{k=1}^n f(kd) \right| > C $$

## Current Status

This problem has been fully resolved by Terence Tao in 2015. However, this repository provides a detailed exploration and re-derivation of the problem, decomposed into axiomatically sound lemmas suitable for future autoformalization in systems like Lean 4.

## Documents

- [Detailed Proof Framework (PDF)](99-Erdos-Discrepancy.pdf)
- [LaTeX Source](99-Erdos-Discrepancy.tex)
