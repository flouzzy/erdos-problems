import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Parity
import Mathlib.Tactic.Linarith

def erdos_moser_sum (m k : ℕ) : ℕ :=
  (Finset.range m).sum (λ i => i^k)

theorem erdos_moser (m k : ℕ) (hm : m ≥ 3) (hk : k ≥ 2) :
  erdos_moser_sum m k ≠ m^k := by
  intro h
  have h_sum_gt : erdos_moser_sum m k > m^k := by
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    sorry
  have h_false : erdos_moser_sum m k > erdos_moser_sum m k := by
    calc erdos_moser_sum m k > m^k := h_sum_gt
         _ = erdos_moser_sum m k := h.symm
  exact lt_irrefl _ h_false
