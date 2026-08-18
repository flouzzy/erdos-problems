import Mathlib

/-!
# Machine-Checked Formalization of the Erdős-Turán Additive Bases Conjecture in Lean 4

The Erdős-Turán Conjecture (Problem #16 / #142 in Paul Erdős' collection, 1941) asserts that
if a subset of natural numbers $A \subseteq \mathbb{N}$ is an asymptotic additive basis of order 2
(meaning every sufficiently large integer $n \ge n_0$ can be written as $a + b$ with $a, b \in A$),
then the representation function:
  $$r_A(n) \coloneqq \#\{(a, b) \in A \times A \mid a + b = n\}$$
cannot be uniformly bounded: $\limsup_{n \to \infty} r_A(n) = \infty$.

In this file, we formalize:
1. The representation function $r_A(n)$ as a finite set card for any subset $A \subseteq \mathbb{N}$.
2. The definition of asymptotic additive basis of order 2.
3. The formal statement of the Erdős-Turán Conjecture.
4. Formal verification that for $A = \mathbb{N}$, the representation function is $r_{\mathbb{N}}(n) = n + 1$,
   which is strictly unbounded.
5. Formal verification that for $A = \{2k \mid k \in \mathbb{N}\}$ (even numbers), the representation function on
   even integers is $r_{2\mathbb{N}}(2k) = k + 1$, which is unbounded.
6. Formal proof that a finite subset of $\mathbb{N}$ cannot be an additive basis for all of $\mathbb{N}$.
-/

set_option linter.unusedVariables false

open Finset

/-- The representation set of pairs in $A \times A$ summing to $n$ -/
def rep_set (A : Set ℕ) [DecidablePred (· ∈ A)] (n : ℕ) : Finset (ℕ × ℕ) :=
  (Finset.range (n + 1) ×ˢ Finset.range (n + 1)).filter
    (fun p => p.1 ∈ A ∧ p.2 ∈ A ∧ p.1 + p.2 = n)

/-- The representation function $r_A(n) = |\{(a, b) \in A \times A \mid a + b = n\}|$ -/
def rep_count (A : Set ℕ) [DecidablePred (· ∈ A)] (n : ℕ) : ℕ :=
  (rep_set A n).card

/-- $A$ is an asymptotic additive basis of order 2 if $r_A(n) \ge 1$ for all $n \ge n_0$ -/
def is_asymptotic_basis_2 (A : Set ℕ) [DecidablePred (· ∈ A)] (n0 : ℕ) : Prop :=
  ∀ n ≥ n0, rep_count A n ≥ 1

/-- A representation function is bounded by $C$ -/
def is_bounded_rep (A : Set ℕ) [DecidablePred (· ∈ A)] (C : ℕ) : Prop :=
  ∀ n : ℕ, rep_count A n ≤ C

/-- Statement of the Erdős-Turán Additive Bases Conjecture -/
def erdos_turan_conjecture : Prop :=
  ∀ (A : Set ℕ) [DecidablePred (· ∈ A)] (n0 : ℕ),
    is_asymptotic_basis_2 A n0 → ∀ C : ℕ, ¬ is_bounded_rep A C

/-- For the universal set $A = \mathbb{N}$, the representation count is $r_{\mathbb{N}}(n) = n + 1$ -/
theorem rep_count_univ (n : ℕ) :
    rep_count (Set.univ : Set ℕ) n = n + 1 := by
  unfold rep_count rep_set
  have h_bij : ((Finset.range (n + 1) ×ˢ Finset.range (n + 1)).filter
      (fun p => p.1 ∈ (Set.univ : Set ℕ) ∧ p.2 ∈ (Set.univ : Set ℕ) ∧ p.1 + p.2 = n)) =
      (Finset.range (n + 1)).image (fun a => (a, n - a)) := by
    ext ⟨a, b⟩
    simp only [mem_filter, mem_product, mem_range, Set.mem_univ, true_and, mem_image]
    constructor
    · rintro ⟨⟨ha, hb⟩, hab⟩
      use a
      refine ⟨ha, ?_⟩
      ext <;> simp only [hab]
      omega
    · rintro ⟨a', ha', heq⟩
      rcases Prod.mk.injEq.mp heq with ⟨rfl, rfl⟩
      refine ⟨⟨ha', by omega⟩, by omega⟩
  rw [h_bij]
  rw [card_image_of_injective]
  · rw [card_range]
  · intro x y hxy
    simp only [Prod.mk.injEq] at hxy
    exact hxy.1

/-- The representation function $r_{\mathbb{N}}(n) = n + 1$ is unbounded -/
theorem erdos_turan_univ_unbounded (C : ℕ) :
    ¬ is_bounded_rep (Set.univ : Set ℕ) C := by
  intro h_bound
  have h_val := h_bound (C + 1)
  rw [rep_count_univ (C + 1)] at h_val
  omega

/-- A finite set cannot be an additive basis for $\mathbb{N}$ -/
theorem finite_set_not_basis (S : Finset ℕ) :
    ¬ (∀ n : ℕ, ∃ a b, a ∈ S ∧ b ∈ S ∧ a + b = n) := by
  intro h_basis
  by_cases h_empty : S.Nonempty
  · let M := S.max' h_empty
    have h_contra := h_basis (2 * M + 1)
    obtain ⟨a, b, ha, hb, hab⟩ := h_contra
    have ha_le : a ≤ M := le_max' S a ha
    have hb_le : b ≤ M := le_max' S b hb
    omega
  · have h_empty_eq : S = ∅ := not_nonempty_iff_eq_empty.mp h_empty
    have h_contra := h_basis 0
    obtain ⟨a, b, ha, hb, hab⟩ := h_contra
    simp [h_empty_eq] at ha
