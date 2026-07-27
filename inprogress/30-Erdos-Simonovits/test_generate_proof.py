import os
import pytest
import sys

def test_generate_proof_exists():
    script_path = os.path.join(os.path.dirname(__file__), 'generate_proof.py')
    assert os.path.exists(script_path), "generate_proof.py is missing"

def test_pdf_exists():
    pdf_path = os.path.join(os.path.dirname(__file__), '30-proof.pdf')
    assert os.path.exists(pdf_path), "30-proof.pdf was not generated or compiled"

def test_pdf_validity():
    pdf_path = os.path.join(os.path.dirname(__file__), '30-proof.pdf')
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader(pdf_path)
        assert len(reader.pages) >= 10, "PDF must have at least 10 pages"
    except ImportError:
        pytest.skip("PyPDF2 not installed")

if __name__ == '__main__':
    pytest.main(['-v', __file__])
