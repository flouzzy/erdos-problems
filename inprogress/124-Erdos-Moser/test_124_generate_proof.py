import os
import PyPDF2

def test_pdfs_generated():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_pdf = os.path.join(base_dir, "124-Erdos-Moser.pdf")
    fr_pdf = os.path.join(base_dir, "124-Erdos-Moser-fr.pdf")

    assert os.path.exists(en_pdf), f"English PDF not found at {en_pdf}"
    assert os.path.exists(fr_pdf), f"French PDF not found at {fr_pdf}"

    assert os.path.getsize(en_pdf) > 0, "English PDF is empty"
    assert os.path.getsize(fr_pdf) > 0, "French PDF is empty"

def test_pdf_content_readable():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_pdf = os.path.join(base_dir, "124-Erdos-Moser.pdf")

    with open(en_pdf, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        assert len(reader.pages) > 0, "English PDF has no pages"
        text = reader.pages[0].extract_text()
        assert len(text) > 50, "English PDF has insufficient text"
        assert "Erdős" in text or "Erdos" in text or "Charles EDOU NZE" in text, "Missing signature or keyword"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", __file__])
