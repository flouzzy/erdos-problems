import os
import pypdf

def test_pdfs_exist():
    assert os.path.exists('inprogress/66-Erdos-Graham/66-Erdos-Graham.pdf')
    assert os.path.exists('inprogress/66-Erdos-Graham/66-Erdos-Graham.fr.pdf')

def test_pdf_content_en():
    with open('inprogress/66-Erdos-Graham/66-Erdos-Graham.pdf', 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = " ".join([page.extract_text() for page in reader.pages]).replace('\n', ' ')
        assert "Charles EDOU NZE" in text
        assert "Axiomatic Definitions" in text
        assert "Lean 4" in text

def test_pdf_content_fr():
    with open('inprogress/66-Erdos-Graham/66-Erdos-Graham.fr.pdf', 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = " ".join([page.extract_text() for page in reader.pages]).replace('\n', ' ')
        assert "Charles EDOU NZE" in text
        assert "Lean 4" in text
