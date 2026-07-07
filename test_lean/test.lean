import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

def erdos_moser_sum (m k : Nat) : Nat :=
  Finset.sum (Finset.range m) (fun i => i^k)

def is_solution (m k : Nat) : Prop :=
  m > 0 /\ k > 0 /\ erdos_moser_sum m k = m^k

lemma test_lemma (m k : Nat) (h1 : is_solution m k) (h2 : k >= 2) :
  m < 2 * k := by
  by_contra h_ge
  have h_ge_2k : m ≥ 2 * k := Nat.le_of_not_lt h_ge
  have h_sum_eq : erdos_moser_sum m k = m^k := h1.2.2
  have h_sum_gt : erdos_moser_sum m k > m^k := sorry
  omega
