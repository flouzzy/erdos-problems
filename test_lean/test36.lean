import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

open Finset

def ErdosMoserPredicate (k m : Nat) : Prop :=
  (∑ i ∈ range m, i^k) = m^k

set_option linter.unusedVariables false in
lemma erdos_moser_faulhaber_bound (k m : Nat) (hk : k >= 2) (hm : m >= 2) (h_eq : ErdosMoserPredicate k m) :
  m > k := by
  have _hk0 : k > 0 := by omega
  have h1 : (∑ i ∈ range m, i^k) < (m^(k+1)) / (k + 1) := by
    -- Bounding sum by the continuous integral
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    sorry
  have h2 : m^k < (m^(k+1)) / (k + 1) := by
    -- Applying the hypothesis h_eq
    rw [<- h_eq]
    exact h1
  have h3 : (k + 1) * m^k < m^(k+1) := by
    -- Algebraic rearrangement
    have h_pos : k + 1 > 0 := by omega
    have h2_mul := Nat.mul_lt_mul_of_pos_right h2 h_pos
    have h_comm : m^k * (k + 1) = (k + 1) * m^k := Nat.mul_comm _ _
    rw [h_comm] at h2_mul
    apply lt_of_lt_of_le h2_mul
    exact Nat.div_mul_le_self (m ^ (k + 1)) (k + 1)
  have h4 : k + 1 < m := by
    -- Dividing by m^k
    have h_pow : m^(k+1) = m^k * m := by
      rw [Nat.pow_add, Nat.pow_one]
    rw [h_pow] at h3
    have h3_comm : m^k * (k + 1) < m^k * m := by
      have h_comm2 : (k + 1) * m^k = m^k * (k + 1) := Nat.mul_comm _ _
      rwa [h_comm2] at h3
    exact Nat.lt_of_mul_lt_mul_left h3_comm
  omega
