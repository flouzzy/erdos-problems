import Mathlib.Data.Nat.Basic
import Mathlib.Data.Nat.Parity
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Algebra.BigOperators.Basic

open Finset
open scoped BigOperators

set_option linter.unusedVariables false

def ErdosStrausPredicate (n : Nat) : Prop :=
  exists x y z : Nat, x > 0 /\ y > 0 /\ z > 0 /\ 4 * x * y * z = n * (x * y + y * z + z * x)

def L_n (n : Nat) : Nat :=
  Finset.lcm (Finset.range (n + 1)) id

def T_n (n : Nat) (h : n >= 2) : Nat :=
  4 * (L_n n) / n

def Divides (a b : Nat) : Prop := exists k, b = a * k

def DivisorLattice (N : Nat) (d : Nat) : Prop :=
  d > 0 /\ Divides d N

theorem audige_greedy_step (n : Nat) (hn : n >= 2) :
  exists d e f : Nat, DivisorLattice (L_n n) d /\ DivisorLattice (L_n n) e /\
  DivisorLattice (L_n n) f /\ d + e + f = T_n n hn := by
  have step1 : L_n n > 0 := by sorry
  have step2 : T_n n hn > 0 := by sorry
  sorry

theorem erdos_straus_conjecture_from_audige : forall n : Nat, n >= 2 -> ErdosStrausPredicate n := by
  intro n hn
  have h_audige := audige_greedy_step n hn
  sorry
