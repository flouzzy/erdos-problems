import os
import pytest
from pypdf import PdfReader

def test_pdf_generation():
    dir_path = os.path.dirname(__file__)
    en_pdf_path = os.path.join(dir_path, "92-Erdos-Turan-Additive-Bases.pdf")
    fr_pdf_path = os.path.join(dir_path, "92-Erdos-Turan-Additive-Bases.fr.pdf")

    assert os.path.exists(en_pdf_path), "English PDF was not generated."
    assert os.path.exists(fr_pdf_path), "French PDF was not generated."

    with open(en_pdf_path, 'rb') as f:
        reader = PdfReader(f)
        assert len(reader.pages) > 0, "English PDF is empty."

    with open(fr_pdf_path, 'rb') as f:
        reader = PdfReader(f)
        assert len(reader.pages) > 0, "French PDF is empty."
