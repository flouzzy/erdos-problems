import os
import PyPDF2
import pytest

def test_pdf_length():
    # Use absolute path resolution
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, "02-Erdos-Straus.pdf")

    assert os.path.exists(pdf_path), f"PDF file not found at {pdf_path}"

    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)

    assert 10 <= num_pages <= 150, f"PDF page count {num_pages} is out of bounds [10, 150]."

if __name__ == '__main__':
    pytest.main(["-v", __file__])
