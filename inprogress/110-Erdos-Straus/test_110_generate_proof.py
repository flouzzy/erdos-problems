import os
import pypdf

def test_pdfs_generated_and_valid():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    en_pdf = os.path.join(dir_path, "110-Erdos-Straus_en.pdf")
    fr_pdf = os.path.join(dir_path, "110-Erdos-Straus_fr.pdf")

    assert os.path.exists(en_pdf), "English PDF not found."
    assert os.path.exists(fr_pdf), "French PDF not found."

    for pdf_path in [en_pdf, fr_pdf]:
        with open(pdf_path, "rb") as f:
            reader = pypdf.PdfReader(f)
            assert len(reader.pages) > 0, f"PDF {pdf_path} is empty."
            text = reader.pages[0].extract_text()
            assert "Charles EDOU NZE" in text, f"Signature missing in {pdf_path}"
