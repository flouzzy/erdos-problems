import os
import pytest
from pypdf import PdfReader

def normalize_text(text):
    if not text:
        return ""
    text = text.replace('\n', ' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace(" ", "")
    return text.strip()

def check_pdf_content(pdf_path, expected_strings):
    assert os.path.exists(pdf_path), f"File {pdf_path} not found."
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + " "

    normalized_text = normalize_text(full_text)

    for string in expected_strings:
        assert string.replace(" ", "") in normalized_text, f"Expected string '{string}' not found in {pdf_path}"

def test_english_pdf_content():
    pdf_path = "12-Erdos-Ulam-en.pdf"
    expected_strings = [
        "Charles EDOU NZE",
        "chercheur",
        "Bombieri-Lang",
        "DistanceSurface"
    ]
    check_pdf_content(pdf_path, expected_strings)

def test_french_pdf_content():
    pdf_path = "12-Erdos-Ulam-fr.pdf"
    expected_strings = [
        "Charles EDOU NZE",
        "chercheur",
        "Bombieri-Lang",
        "DistanceSurface"
    ]
    check_pdf_content(pdf_path, expected_strings)

if __name__ == '__main__':
    pytest.main(['-v', __file__])
