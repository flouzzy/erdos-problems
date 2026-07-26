# 27-Erdos-Powerful-Numbers

## Problem Overview

The Erdős conjecture on powerful numbers states that there do not exist three consecutive powerful numbers. A positive integer $n$ is called powerful if, for every prime $p$ dividing $n$, $p^2$ also divides $n$.

While there exist pairs of consecutive powerful numbers (e.g., 8 and 9), it is hypothesized that the diophantine constraints become too rigid to allow for three in a row.

## Current Progress

This directory contains a rigorous diophantine analysis and a partial proof breakdown of the problem into three lemmas, resolving local parity constraints and setting up the formal architecture for Lean 4 autoformalization.

### Contents:
- `27-Erdos-Powerful-Numbers.tex` / `pdf`: Extensive theoretical document and proof sketches (18 pages).
- `generate_tex.py`: Python script used to programmatically generate the LaTeX document.
