import os
import subprocess
import pytest
from pypdf import PdfReader

def test_english_pdf_exists():
    assert os.path.exists("inprogress/999-Erdos-Gyarfas/999-Erdos-Gyarfas_EN.pdf")

def test_french_pdf_exists():
    assert os.path.exists("inprogress/999-Erdos-Gyarfas/999-Erdos-Gyarfas_FR.pdf")

def test_pdf_contains_author():
    for lang in ["EN", "FR"]:
        pdf_path = f"inprogress/999-Erdos-Gyarfas/999-Erdos-Gyarfas_{lang}.pdf"
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        assert "Charles EDOU NZE" in text

def test_pdf_page_count():
    for lang in ["EN", "FR"]:
        pdf_path = f"inprogress/999-Erdos-Gyarfas/999-Erdos-Gyarfas_{lang}.pdf"
        reader = PdfReader(pdf_path)
        assert len(reader.pages) >= 1
