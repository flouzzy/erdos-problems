import Mathlib

/-!
# Machine-Checked Formalization of the Erdős Covering Systems Problem in Lean 4

The Erdős Covering System Problem (Problem #30 in Paul Erdős' problem collection, 1950)
is one of Paul Erdős' most famous conjectures (backed by his \$1000 reward).
A *covering system* is a finite family of congruence classes $a_i \pmod{m_i}$ with distinct moduli
$1 < m_1 < m_2 < \dots < m_k$ such that every integer $x \in \mathbb{Z}$ satisfies at least one congruence:
  $$\forall x \in \mathbb{Z}, \quad \exists i \in \{1, \dots, k\}, \quad x \equiv a_i \pmod{m_i}$$

Key Mathematical Milestones:
- In 1950, Paul Erdős introduced the concept and discovered the canonical covering system with moduli $\{2, 3, 4, 6, 12\}$:
  $0 \pmod 2, \; 0 \pmod 3, \; 1 \pmod 4, \; 5 \pmod 6, \; 7 \pmod{12}$.
- Erdős asked whether the minimum modulus $m_1$ can be arbitrarily large (The Minimum Modulus Problem).
- In 2015, Bob Hough (*Annals of Mathematics*) definitively solved Erdős' \$1000 problem,
  proving that the minimum modulus of any covering system with distinct moduli is universally bounded:
  $$m_1 \le 10^{16}$$
- In 2022, Balister, Bollobás, Morris, Sahasrabudhe, and Tiba refined Hough's method to $m_1 \le 616000$
  and resolved the odd covering system problem.

In this file, we formally certify:
1. The covering system predicate for modular congruence systems in $\mathbb{Z}$.
2. The distinct moduli requirement with $m_i > 1$.
3. Machine-checked verification that Erdős' classic system $(0, 2), (0, 3), (1, 4), (5, 6), (7, 12)$
   covers all integers $\mathbb{Z}$ by complete residue classification modulo 12.
-/

set_option linter.unusedVariables false
set_option linter.unusedSimpArgs false
set_option linter.unusedSectionVars false

open scoped Classical

/-- Predicate: A collection of congruence pairs $(a_i, m_i)$ covers the integer $x$ -/
def is_covered_by (x : ℤ) (congs : List (ℤ × ℕ)) : Prop :=
  ∃ pair ∈ congs, x % (pair.2 : ℤ) = (pair.1 % (pair.2 : ℤ))

/-- Erdős' canonical 1950 covering system -/
def erdos_canonical_system : List (ℤ × ℕ) :=
  [(0, 2), (0, 3), (1, 4), (5, 6), (7, 12)]

/-- Verification that all moduli are distinct and strictly greater than 1 -/
theorem erdos_system_distinct_moduli :
    erdos_canonical_system.map Prod.snd = [2, 3, 4, 6, 12] ∧
    [2, 3, 4, 6, 12].Nodup := by
  decide

/-- Theorem: For each of the 12 residue classes $r \in \{0, \dots, 11\}$ modulo 12,
    there exists a covering pair in Erdős' system -/
theorem erdos_system_covers_residue (r : ℤ) (hr0 : 0 ≤ r) (hr12 : r < 12) :
    is_covered_by r erdos_canonical_system := by
  unfold is_covered_by erdos_canonical_system
  interval_cases r
  · use (0, 2); decide
  · use (1, 4); decide
  · use (0, 2); decide
  · use (0, 3); decide
  · use (0, 2); decide
  · use (5, 6); decide
  · use (0, 2); decide
  · use (7, 12); decide
  · use (0, 2); decide
  · use (0, 3); decide
  · use (0, 2); decide
  · use (5, 6); decide

/-- Global theorem: Erdős' canonical system covers every integer $x \in \mathbb{Z}$ -/
theorem erdos_system_covers_all (x : ℤ) :
    is_covered_by x erdos_canonical_system := by
  have h_res := erdos_system_covers_residue (x % 12) (by omega) (by omega)
  obtain ⟨pair, h_mem, h_cov⟩ := h_res
  use pair, h_mem
  rcases pair with ⟨a, m⟩
  unfold erdos_canonical_system at h_mem
  simp only [List.mem_cons, List.not_mem_nil, or_false] at h_mem
  rcases h_mem with h | h | h | h | h <;> {
    injection h with ha hm
    subst ha hm
    omega
  }
