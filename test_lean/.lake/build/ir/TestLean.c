// Lean compiler output
// Module: TestLean
// Imports: public import Init public meta import Init public import Mathlib.Data.Nat.Prime.Basic public import Mathlib.Algebra.BigOperators.Group.Finset.Basic public import Mathlib
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lean_nat_pow(lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
lean_object* lp_mathlib_Finset_sum___at___00Fin_accumulate_spec__0___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum___lam__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum___lam__0___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum___lam__0(lean_object* v_k_1_, lean_object* v_i_2_){
_start:
{
lean_object* v___x_3_;
v___x_3_ = lean_nat_pow(v_i_2_, v_k_1_);
return v___x_3_;
}
}
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum___lam__0___boxed(lean_object* v_k_4_, lean_object* v_i_5_){
_start:
{
lean_object* v_res_6_;
v_res_6_ = lp_test__lean_erdos__moser__sum___lam__0(v_k_4_, v_i_5_);
lean_dec(v_i_5_);
lean_dec(v_k_4_);
return v_res_6_;
}
}
LEAN_EXPORT lean_object* lp_test__lean_erdos__moser__sum(lean_object* v_m_7_, lean_object* v_k_8_){
_start:
{
lean_object* v___f_9_; lean_object* v___x_10_; lean_object* v___x_11_;
v___f_9_ = lean_alloc_closure((void*)(lp_test__lean_erdos__moser__sum___lam__0___boxed), 2, 1);
lean_closure_set(v___f_9_, 0, v_k_8_);
v___x_10_ = l_List_range(v_m_7_);
v___x_11_ = lp_mathlib_Finset_sum___at___00Fin_accumulate_spec__0___redArg(v___x_10_, v___f_9_);
return v___x_11_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib_Algebra_BigOperators_Group_Finset_Basic(uint8_t builtin);
lean_object* initialize_mathlib_Mathlib(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_test__lean_TestLean(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Data_Nat_Prime_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib_Algebra_BigOperators_Group_Finset_Basic(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_mathlib_Mathlib(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
