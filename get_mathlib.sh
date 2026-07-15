#!/bin/bash
cd test_lean
sed -i '/def package/a \  dependencies := #[{ name := `mathlib, url := "https://github.com/leanprover-community/mathlib4", rev := "v4.11.0" }]' lakefile.lean
lake update
lake exe cache get
lake env lean test_simpl.lean
