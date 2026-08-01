import os
import subprocess

def test_pdf_exists():
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "10-Erdos-Szemeredi.pdf"))
    assert os.path.exists(os.path.join(os.path.dirname(__file__), "10-Erdos-Szemeredi-FR.pdf"))

def test_pdf_pages():
    for pdf in ["10-Erdos-Szemeredi.pdf", "10-Erdos-Szemeredi-FR.pdf"]:
        pdf_path = os.path.join(os.path.dirname(__file__), pdf)
        result = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True)
        assert result.returncode == 0
        pages_line = next((line for line in result.stdout.splitlines() if line.startswith("Pages:")), None)
        assert pages_line is not None
        pages_count = int(pages_line.split(":")[1].strip())
        assert pages_count >= 1
