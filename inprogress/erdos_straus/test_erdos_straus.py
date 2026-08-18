import pytest
from pypdf import PdfReader
import re

def normalize_text(text):
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('’', "'")
    return text.strip()

def test_english_pdf_content():
    reader = PdfReader("erdos_straus_proof_en.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    text = normalize_text(text)

    assert "Charles EDOU NZE" in text
    assert "Erdős-Straus conjecture" in text or "Erd˝os-Straus Conjecture" in text or "Erdos-Straus" in text or "Erd ̋os-Straus" in text
    assert "Lean 4" in text

def test_french_pdf_content():
    reader = PdfReader("erdos_straus_proof_fr.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    text = normalize_text(text)

    assert "Charles EDOU NZE" in text
    assert "Erdős-Straus" in text or "Erd˝os-Straus" in text or "Erdos-Straus" in text or "Erd ̋os-Straus" in text
    assert "Lean 4" in text
