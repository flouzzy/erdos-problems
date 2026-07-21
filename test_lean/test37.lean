import Mathlib

open Finset

def ErdosMoserPredicate (k m : Nat) : Prop :=
  (∑ i ∈ range m, i^k) = m^k

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

def erdos_moser_sum (m k : ℕ) : ℕ :=
  (Finset.range m).sum (λ i => i^k)

lemma sum_ik_mod_p_zmod (p k : ℕ) (hp : Nat.Prime p) (hk : ¬ (p - 1 ∣ k)) :
  (∑ i ∈ Finset.range p, (i : ZMod p)^k) = 0 := by
  haveI : Fact (Nat.Prime p) := ⟨hp⟩
  by_cases hk0 : k = 0
  · subst hk0
    simp only [pow_zero, sum_const, card_range, nsmul_eq_mul, mul_one]
    exact ZMod.natCast_self p
  · obtain ⟨g, hg⟩ := IsCyclic.exists_generator (α := (ZMod p)ˣ)
    have h_generator : (g ^ k : ZMod p) ≠ 1 := by
      intro h_contra
      have h_contra_unit : g ^ k = 1 := Units.ext h_contra
      have h_div : orderOf g ∣ k := orderOf_dvd_of_pow_eq_one h_contra_unit
      have h_ord : orderOf g = p - 1 := by
        have h_card : Nat.card (ZMod p)ˣ = p - 1 := by
          rw [Nat.card_eq_fintype_card]
          exact ZMod.card_units p
        rw [← h_card]
        exact orderOf_eq_card_of_forall_mem_zpowers hg
      rw [h_ord] at h_div
      exact hk h_div
    have h_sum_equiv : ∑ i ∈ Finset.range p, (i : ZMod p)^k = ∑ i : ZMod p, i^k := by
      refine sum_bij (fun a _ => (a : ZMod p)) ?_ ?_ ?_ ?_
      · intro a _
        exact mem_univ _
      · intro a₁ h1 a₂ h2 h
        have h1' : (a₁ : ZMod p).val = a₁ := ZMod.val_natCast_of_lt (mem_range.mp h1)
        have h2' : (a₂ : ZMod p).val = a₂ := ZMod.val_natCast_of_lt (mem_range.mp h2)
        rw [← h1', ← h2', h]
      · intro b _
        exact ⟨b.val, mem_range.mpr (ZMod.val_lt b), ZMod.natCast_zmod_val b⟩
      · intro a _
        rfl
    have h_sum_mul : (g ^ k : ZMod p) * (∑ i : ZMod p, i^k) = ∑ i : ZMod p, i^k := by
      rw [mul_sum]
      have h_reindex : (∑ i : ZMod p, (g ^ k : ZMod p) * i^k) = ∑ i : ZMod p, ((g : ZMod p) * i)^k := by
        apply sum_congr rfl
        intro x _
        rw [mul_pow]
      rw [h_reindex]
      exact Equiv.sum_comp (Equiv.mulLeft₀ (g : ZMod p) (Units.ne_zero g)) (fun x => x^k)
    have h_sub : (1 - (g ^ k : ZMod p)) * (∑ i : ZMod p, i^k) = 0 := by
      calc (1 - (g ^ k : ZMod p)) * (∑ i : ZMod p, i^k)
        _ = 1 * (∑ i : ZMod p, i^k) - (g ^ k : ZMod p) * (∑ i : ZMod p, i^k) := by rw [sub_mul]
        _ = (∑ i : ZMod p, i^k) - (∑ i : ZMod p, i^k) := by rw [one_mul, h_sum_mul]
        _ = 0 := sub_self _
    have h_1_sub_ne_0 : 1 - (g ^ k : ZMod p) ≠ 0 := by
      intro h_eq
      have h_eq2 : (g ^ k : ZMod p) = 1 := by
        calc (g ^ k : ZMod p)
          _ = 1 - (1 - (g ^ k : ZMod p)) := by ring
          _ = 1 - 0 := by rw [h_eq]
          _ = 1 := sub_zero 1
      exact h_generator h_eq2
    have h_sum_0 : (∑ i : ZMod p, i^k) = 0 := by
      exact eq_zero_of_ne_zero_of_mul_left_eq_zero h_1_sub_ne_0 h_sub
    rw [h_sum_equiv, h_sum_0]

lemma sum_ik_mod_p (p k : ℕ) (hp : Nat.Prime p) (hk : ¬ (p - 1 ∣ k)) :
  (∑ i ∈ Finset.range p, i^k) ≡ 0 [MOD p] := by
  have H := sum_ik_mod_p_zmod p k hp hk
  have H2 : ((∑ i ∈ Finset.range p, i^k : ℕ) : ZMod p) = 0 := by
    rw [Nat.cast_sum]
    have h_pow : ∑ i ∈ Finset.range p, ((i^k : ℕ) : ZMod p) = ∑ i ∈ Finset.range p, (i : ZMod p)^k := by
      apply sum_congr rfl
      intro x _
      exact Nat.cast_pow x k
    rw [h_pow]
    exact H
  have H3 : p ∣ (∑ i ∈ Finset.range p, i^k : ℕ) := by
    haveI : Fact (Nat.Prime p) := ⟨hp⟩
    rw [← ZMod.natCast_eq_zero_iff]
    exact H2
  exact Nat.modEq_zero_iff_dvd.mpr H3

-- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
theorem erdos_moser (m k : ℕ) (hm : m > 3) (hk : k ≥ 2) (h_k_even : Even k) :
  erdos_moser_sum m k ≠ m^k := by
  intro h
  have h_sum_bounds : erdos_moser_sum m k < (m-1)^(k+1) / (k+1) + (m-1)^k := by
    sorry
  sorry
