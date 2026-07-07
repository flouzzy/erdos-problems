import pytest
from generate_proof import generate_readme_fr, generate_readme_en

def test_generate_readme_fr():
    content = generate_readme_fr()
    assert isinstance(content, str)
    assert "# 16 - Conjecture d'Erdős-Turán sur les bases additives" in content
    assert "Définitions Axiomatiques" in content
    assert "Architecture d'Autoformalisation (Lean 4)" in content
    assert "theorem erdos_turan_additive_conjecture" in content

def test_generate_readme_en():
    content = generate_readme_en()
    assert isinstance(content, str)
    assert "# 16 - Erdős-Turán Conjecture on Additive Bases" in content
    assert "Problem Statement" in content
    assert "Current Status" in content
