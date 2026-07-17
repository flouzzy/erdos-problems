import Mathlib

example (m k : Nat) (hm_pos : m > 0) (h_subst : (k + 1) * m^k > m^(k + 1)) : k + 1 > m := by
  have hm_pow_pos : m^k > 0 := Nat.pos_pow_of_pos k hm_pos
  rw [pow_succ] at h_subst
  -- h_subst : (k + 1) * m ^ k > m ^ k * m
  -- actually m ^ (k + 1) is m ^ k * m
  sorry
