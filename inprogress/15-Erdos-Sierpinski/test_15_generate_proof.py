import os
import pytest
from pypdf import PdfReader

def normalize_text(text):
    return text.replace('\n', ' ').replace('’', "'").replace('  ', ' ')

def test_english_pdf_exists_and_contains_text():
    pdf_path = os.path.join(os.path.dirname(__file__), '15-Erdos-Sierpinski.pdf')
    assert os.path.exists(pdf_path), "English PDF does not exist."

    reader = PdfReader(pdf_path)
    assert len(reader.pages) > 0, "PDF has no pages."

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    text = normalize_text(text)

    assert "Charles EDOU NZE" in text
    assert "Erdős-Sierpiński conjecture" in text or "Erdos-Sierpiński conjecture" in text or "Erdős-Sierpi\\'nski conjecture" in text or "Erdős-Sierpinski" in text or "Erdos-Sierpinski" in text or "Erdos-Sierpi\\'nski" in text or "Erdős-Sierpi\\'nski" in text or "Erdős-Sierpi" in text or "Erdos-Sierpi" in text
    assert "Lean 4" in text

def test_french_pdf_exists_and_contains_text():
    pdf_path = os.path.join(os.path.dirname(__file__), '15-Erdos-Sierpinski.fr.pdf')
    assert os.path.exists(pdf_path), "French PDF does not exist."

    reader = PdfReader(pdf_path)
    assert len(reader.pages) > 0, "PDF has no pages."

    text = ""
    for page in reader.pages:
        text += page.extract_text()

    text = normalize_text(text)

    assert "Charles EDOU NZE" in text
    assert "Lean 4" in text

if __name__ == "__main__":
    pytest.main([__file__])
