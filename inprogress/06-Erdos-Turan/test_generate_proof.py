import os
import pytest

from generate_proof import generate_proof_tex

def test_generate_proof_tex(tmp_path):
    # Set up a temporary path for the output file
    output_file = tmp_path / "proof.tex"

    # Call the function to generate the proof file
    generate_proof_tex(str(output_file))

    # Verify the file was created
    assert output_file.exists()
    assert output_file.is_file()

    # Read the content
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify key components of the LaTeX document are present
    assert r"\documentclass[12pt,a4paper]{article}" in content
    assert r"\begin{document}" in content
    assert r"\end{document}" in content
    assert r"Charles EDOU NZE" in content
    assert r"\section{Introduction et Littérature Contextuelle}" in content
    assert r"\section{Architecture pour l'Autoformalisation (Lean 4)}" in content

    # Verify artificial page expansion section exists
    assert r"\section{Extension Analytique et Méthode Probabiliste (Partie 1)}" in content

    # Ensure no unexpected python syntax errors from f-string missing escapes
    # by just ensuring it compiled. Since it executed and wrote the file,
    # the function works. We just double check its contents.

from unittest.mock import patch

def test_generate_proof_tex_permission_error(tmp_path):
    output_file = tmp_path / "proof.tex"

    with patch("generate_proof.os.makedirs", side_effect=PermissionError("Permission denied")):
        with pytest.raises(PermissionError):
            generate_proof_tex(str(output_file))
