import Mathlib

example (m k : Nat) (hm_pos : m > 0) (h_subst : (k + 1) * m^k > m^(k + 1)) : k + 1 > m := by
  have hm_pow_pos : m^k > 0 := by
    clear h_subst
    induction k with
    | zero => simp
    | succ d hd =>
      rw [pow_succ]
      exact Nat.mul_pos hd hm_pos
  rw [pow_succ] at h_subst
  exact (Nat.mul_lt_mul_right hm_pow_pos).mp (by
    have h1 : m^k * m = m * m^k := mul_comm (m^k) m
    rw [h1] at h_subst
    exact h_subst)
