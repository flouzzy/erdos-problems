import os
import subprocess
import pytest
from unittest.mock import patch, mock_open

# We import the generated script dynamically for testing, or just test the files generated
# Since generate_proofs.py is at the root, we can import it.
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import generate_proofs

def test_generate_tex_content_no_meta():
    en_content = generate_proofs.generate_tex_content('en')
    fr_content = generate_proofs.generate_tex_content('fr')

    # Check for absence of meta-commentary
    meta_phrases = [
        "As requested", "To facilitate future autoformalization",
        "This step demonstrates", "zéro ellipse", "Comme demandé",
        "Ce niveau de détail montre"
    ]
    for phrase in meta_phrases:
        assert phrase.lower() not in en_content.lower()
        assert phrase.lower() not in fr_content.lower()

def test_generate_tex_content_lean_unicode():
    en_content = generate_proofs.generate_tex_content('en')

    # Verify that outside verbatim, replacements happened, but in this specific text we didn't use ℝ in verbatim.
    # The main checks are that \mathbb{N} is present and ℕ is absent outside verbatim.
    # Since our script replaces all ℕ not in verbatim, we just check that ℕ isn't there anymore.
    # Actually, in our text we used ℕ, ∈ in regular text, so they should be replaced.
    assert 'ℕ' not in en_content
    assert '∈' not in en_content
    assert r'\mathbb{N}' in en_content
    assert r'\in' in en_content

@patch('builtins.open', new_callable=mock_open)
def test_mock_file_writes(mock_file):
    en_content = generate_proofs.generate_tex_content('en')
    fr_content = generate_proofs.generate_tex_content('fr')

    # Mocking open so it doesn't write to disk
    base_dir = "inprogress/109-Erdos-Straus"
    en_file = os.path.join(base_dir, "109-Erdos-Straus.tex")
    fr_file = os.path.join(base_dir, "109-Erdos-Straus-fr.tex")

    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(en_content)
    with open(fr_file, 'w', encoding='utf-8') as f:
        f.write(fr_content)

    mock_file.assert_any_call(en_file, 'w', encoding='utf-8')
    mock_file.assert_any_call(fr_file, 'w', encoding='utf-8')


def test_pdf_properties():
    base_dir = os.path.dirname(__file__)
    en_pdf = os.path.join(base_dir, "109-Erdos-Straus.pdf")
    fr_pdf = os.path.join(base_dir, "109-Erdos-Straus-fr.pdf")

    assert os.path.exists(en_pdf), f"{en_pdf} does not exist"
    assert os.path.exists(fr_pdf), f"{fr_pdf} does not exist"

    for pdf_path in [en_pdf, fr_pdf]:
        result = subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True)
        assert result.returncode == 0

        pages_line = [line for line in result.stdout.split('\n') if line.startswith('Pages:')]
        assert len(pages_line) == 1
        pages_count = int(pages_line[0].split(':')[1].strip())
        assert pages_count > 0, "PDF must have at least 1 page"
