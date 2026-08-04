import os
import pypdf
import pytest
import unittest.mock
from generate_proof import generate_proof_tex, write_and_compile

def test_generate_proof_tex():
    tex_en = generate_proof_tex("en")
    assert "Charles EDOU NZE" in tex_en
    assert "abstract" in tex_en
    assert "lemma" in tex_en

    tex_fr = generate_proof_tex("fr")
    assert "Charles EDOU NZE" in tex_fr
    assert "abstract" in tex_fr
    assert "Lemme" in tex_fr

def test_pdf_generation():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_pdf = os.path.join(base_dir, "162-Erdos-Moser.pdf")
    fr_pdf = os.path.join(base_dir, "162-Erdos-Moser-fr.pdf")

    assert os.path.exists(en_pdf), f"PDF file not found at {en_pdf}"
    assert os.path.exists(fr_pdf), f"PDF file not found at {fr_pdf}"

    with open(en_pdf, 'rb') as f:
        reader = pypdf.PdfReader(f)
        num_pages = len(reader.pages)
        assert 1 <= num_pages <= 150, f"English PDF page count {num_pages} is out of bounds."

    with open(fr_pdf, 'rb') as f:
        reader = pypdf.PdfReader(f)
        num_pages = len(reader.pages)
        assert 1 <= num_pages <= 150, f"French PDF page count {num_pages} is out of bounds."

if __name__ == '__main__':
    pytest.main(["-v", __file__])
