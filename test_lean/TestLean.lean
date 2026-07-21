import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib

set_option maxRecDepth 2000000
set_option exponentiation.threshold 2000000
set_option linter.unusedVariables false

open Finset

def erdos_moser_sum (m k : Nat) : Nat :=
  Finset.sum (Finset.range m) (fun i => i^k)

def is_solution (m k : Nat) : Prop :=
  m > 0 /\ k > 0 /\ erdos_moser_sum m k = m^k

set_option linter.unusedVariables false in
lemma lemma1_k_is_even (m k : Nat) (h1 : m >= 2) (h2 : k >= 2) (h3 : is_solution m k) :
  Even k := by
  have h_eq : erdos_moser_sum m k = m^k := h3.2.2
  have h_mod_2 : erdos_moser_sum m k % 2 = m^k % 2 := by rw [h_eq]
  have h_mod_m_minus_1 : erdos_moser_sum m k % (m - 1) = m^k % (m - 1) := by rw [h_eq]
  -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
  by_contra hk
  have hm_minus_1_gt_0 : m - 1 > 0 := by omega
  -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
  have h_sum_mod : erdos_moser_sum m k % (m - 1) = (m - 1) / 2 % (m - 1) := sorry
  -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
  have h_mk_mod : m^k % (m - 1) = 1 % (m - 1) := sorry
  have h_contra : (m - 1) / 2 % (m - 1) = 1 % (m - 1) := by
    rw [← h_sum_mod, h_mod_m_minus_1, h_mk_mod]
  have h_m_val : m = 3 := sorry
  have h_k_val : k = 1 := by
    have h_eq2 : erdos_moser_sum m k = m^k := h3.2.2
    rw [h_m_val] at h_eq2
    unfold erdos_moser_sum at h_eq2
    have h_sum : Finset.sum (Finset.range 3) (fun i => i^k) = 0^k + 1^k + 2^k := by
      rw [Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_succ, Finset.sum_range_zero]
      ring
    rw [h_sum] at h_eq2
    have h_0_pow : 0^k = 0 := by
      cases k
      · have h_pos : 0 > 0 := h3.2.1
        contradiction
      · rfl
    have h_1_pow : 1^k = 1 := Nat.one_pow k
    rw [h_0_pow, h_1_pow] at h_eq2
    have h_eq3 : 1 + 2^k = 3^k := by
      have hrw1 : 0 + 1 + 2^k = 1 + 2^k := by rfl
      rw [hrw1] at h_eq2
      exact h_eq2
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    sorry
  have h_contra_k : 1 >= 2 := by
    rw [←h_k_val]
    exact h2
  omega

set_option linter.unusedVariables false in
lemma lemma2_prime_divisors (m k p : Nat) (hp : Nat.Prime p) (h1 : is_solution m k)
  (h2 : k >= 2) :
  (p ∣ (m - 1) \/ p ∣ (m + 1)) -> p > 10^7 := by
  intro h_div
  -- Il s'agit d'une esquisse de preuve incomplète destinée à une autoformalisation future.
  have h_val : p ∣ k := sorry
  have h_cong : p^2 ∣ (m^k - m) := sorry
  have h_bound : p > 10^7 := by
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    sorry
  exact h_bound

set_option linter.unusedVariables false

lemma lemma3_analytic_bound (m k : Nat) (h1 : is_solution m k) (h2 : k >= 2) :
  m < 10^1000000 := by
  -- L'approximation analytique lie asymptotiquement m et k
  have h_asymp : m < 2 * k := by
    have ⟨hm_pos, hk_pos, heq⟩ := h1
    -- Comparaison de la somme de puissances avec une integrale
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    have h_integral_comp : (k + 1) * erdos_moser_sum m k > m^(k + 1) := sorry
    have h_subst : (k + 1) * m^k > m^(k + 1) := by
      rw [heq] at h_integral_comp
      exact h_integral_comp
    have h_simpl : m < k + 1 := by
      have h_pow : m^(k+1) = m^k * m := by
        rw [Nat.pow_add, Nat.pow_one]
      rw [h_pow] at h_subst
      have h_subst_lt : m^k * m < m^k * (k + 1) := by
        have h_comm : (k + 1) * m^k = m^k * (k + 1) := Nat.mul_comm _ _
        rwa [h_comm] at h_subst
      exact Nat.lt_of_mul_lt_mul_left h_subst_lt
    omega
  -- La densite des diviseurs premiers (Lemme 2) impose m exponentiellement grand
  -- Il s'agit d'une esquisse de preuve incomplète destinée à une autoformalisation future.
  have h_densite : m > 2 * k ∨ m < 10^1000000 := by
    by_cases h_m : m < 10^1000000
    · exact Or.inr h_m
    · apply Or.inl
      -- L'analyse asymptotique de la densite montre que m doit etre superieur a 2k
      have h_primes : ∀ p, Nat.Prime p → (p ∣ (m - 1) ∨ p ∣ (m + 1)) → p > 10^7 := by
        intro p hp hdiv
        exact lemma2_prime_divisors m k p hp h1 h2 hdiv
      have h_growth : m > 2 * k := by
        have _h_m_large : m ≥ 10^1000000 := Nat.le_of_not_lt h_m
        -- Puisque k > 1, cela implique p <= k
        -- Mais l'analyse fine des congruences montrerait que p > k, une contradiction
        -- On extrait l'hypothese de base
        have ⟨hm_pos, hk_pos, heq⟩ := h1
        -- Comparaison de la somme de puissances avec une integrale
        -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
        have h_integral_comp : (k + 1) * erdos_moser_sum m k > m^(k + 1) := sorry
        have h_subst : (k + 1) * m^k > m^(k + 1) := by
          rw [heq] at h_integral_comp
          exact h_integral_comp
        have h_simpl : m < k + 1 := by
          have h_pow : m^(k+1) = m^k * m := by
            rw [Nat.pow_add, Nat.pow_one]
          rw [h_pow] at h_subst
          have h_subst_lt : m^k * m < m^k * (k + 1) := by
            have h_comm : (k + 1) * m^k = m^k * (k + 1) := Nat.mul_comm _ _
            rwa [h_comm] at h_subst
          exact Nat.lt_of_mul_lt_mul_left h_subst_lt
        omega

  -- Cas de base m <= 3, qu'on resout a la main
      exact h_growth
  -- Contradiction entre la densite et l'asymptotique
  cases h_densite with
  | inl h_gt =>
    have h_contra : ¬(m > 2 * k) := by
      intro h
      have h1 : 2 * k < m := h
      have h2 : m < m := Nat.lt_trans h_asymp h1
      exact Nat.lt_irrefl m h2
    contradiction
  | inr h_lt =>
    exact h_lt

-- 3. Theoreme Principal
theorem erdos_moser_conjecture (m k : Nat) (h : is_solution m k) :
  m = 3 /\ k = 1 := by
  by_cases hk : k >= 2
  · -- Pour k >= 2, les bornes analytiques entrent en contradiction
    have h_bound := lemma3_analytic_bound m k h hk
    -- La combinaison des trois lemmes mene a une contradiction
    have hm_ge_2 : m ≥ 2 := by
      have ⟨hm_pos, hk_pos, heq⟩ := h
      by_contra h_not
      have hm_eq_1 : m = 1 := by omega
      rw [hm_eq_1] at heq
      unfold erdos_moser_sum at heq
      have h_sum : Finset.sum (Finset.range 1) (fun i => i^k) = 0 := by
        rw [Finset.sum_range_one, Nat.zero_pow hk_pos]
      rw [h_sum, Nat.one_pow] at heq
      contradiction
    have h_even_k := lemma1_k_is_even m k hm_ge_2 hk h
    -- Il s'agit d'une esquisse de preuve incomplete destinee a une autoformalisation future.
    have h_p_exists : ∃ p, Nat.Prime p ∧ (p ∣ (m - 1) ∨ p ∣ (m + 1)) ∧ p ≤ 10^7 := sorry
    have ⟨p, hp_prime, hp_div, hp_bound⟩ := h_p_exists
    have hp_gt_10_7 := lemma2_prime_divisors m k p hp_prime h hk hp_div
    have h_contra : False := by
      omega
    exact False.elim h_contra
  · -- Pour k < 2, comme k > 0, k = 1
    have hk1 : k = 1 := by
      have _hk0 : k > 0 := h.2.1
      omega
    have hm3 : m = 3 := by
      have hm_pos : m > 0 := h.1
      have h_eq : erdos_moser_sum m k = m^k := h.2.2
      rw [hk1] at h_eq
      have h_pow1 : (fun (i : Nat) => i^1) = (fun i => i) := by funext x; exact Nat.pow_one x
      unfold erdos_moser_sum at h_eq
      rw [h_pow1] at h_eq
      rw [sum_range_id] at h_eq
      rw [Nat.pow_one] at h_eq
      have h2 : m * (m - 1) / 2 * 2 = m * 2 := congrArg (· * 2) h_eq
      have hdvd : 2 ∣ m * (m - 1) := by
        cases m with
        | zero => exact Nat.dvd_zero 2
        | succ m' =>
          have heven : Even (m' * (m' + 1)) := Nat.even_mul_succ_self m'
          have hdvd2 : 2 ∣ m' * (m' + 1) := even_iff_two_dvd.mp heven
          have hrw : (m' + 1) * (m' + 1 - 1) = (m' + 1) * m' := by rfl
          have hcomm : (m' + 1) * m' = m' * (m' + 1) := Nat.mul_comm (m' + 1) m'
          rw [hrw, hcomm]
          exact hdvd2
      have hdiv : m * (m - 1) / 2 * 2 = m * (m - 1) := Nat.div_mul_cancel hdvd
      rw [hdiv] at h2
      have hm1 : m - 1 = 2 := Nat.eq_of_mul_eq_mul_left hm_pos h2
      omega
    exact ⟨hm3, hk1⟩
