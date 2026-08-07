import os
import subprocess
from pypdf import PdfReader

def test_english_pdf_exists():
    path = os.path.join(os.path.dirname(__file__), "109-Erdos-Straus.pdf")
    assert os.path.exists(path), "English PDF was not generated."

def test_french_pdf_exists():
    path = os.path.join(os.path.dirname(__file__), "109-Erdos-Straus-fr.pdf")
    assert os.path.exists(path), "French PDF was not generated."

def test_pdf_page_count():
    path = os.path.join(os.path.dirname(__file__), "109-Erdos-Straus.pdf")
    reader = PdfReader(path)
    assert len(reader.pages) > 0, "PDF has no pages."
    assert len(reader.pages) <= 150, "PDF has more than 150 pages."

def test_author_signature_english():
    path = os.path.join(os.path.dirname(__file__), "109-Erdos-Straus.pdf")
    reader = PdfReader(path)
    text = reader.pages[0].extract_text()
    assert "Charles EDOU NZE, chercheur" in text, "Signature missing in English PDF."

def test_author_signature_french():
    path = os.path.join(os.path.dirname(__file__), "109-Erdos-Straus-fr.pdf")
    reader = PdfReader(path)
    text = reader.pages[0].extract_text()
    assert "Charles EDOU NZE, chercheur" in text, "Signature missing in French PDF."
