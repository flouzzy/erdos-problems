import os
import subprocess
import pytest

def test_pdf_generation():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_pdf = os.path.join(base_dir, "142-Erdos-Turan-Additive-Bases.pdf")
    fr_pdf = os.path.join(base_dir, "142-Erdos-Turan-Additive-Bases.fr.pdf")

    assert os.path.exists(en_pdf), f"English PDF {en_pdf} does not exist."
    assert os.path.exists(fr_pdf), f"French PDF {fr_pdf} does not exist."

    # Verify English PDF is a valid PDF via pdfinfo
    result_en = subprocess.run(['pdfinfo', en_pdf], capture_output=True, text=True)
    assert result_en.returncode == 0, "English PDF is invalid or corrupted."
    assert "Pages:" in result_en.stdout, "English PDF does not contain pages."

    # Verify French PDF is a valid PDF via pdfinfo
    result_fr = subprocess.run(['pdfinfo', fr_pdf], capture_output=True, text=True)
    assert result_fr.returncode == 0, "French PDF is invalid or corrupted."
    assert "Pages:" in result_fr.stdout, "French PDF does not contain pages."

def test_readme_existence():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    en_readme = os.path.join(base_dir, "README.md")
    fr_readme = os.path.join(base_dir, "README.fr.md")

    assert os.path.exists(en_readme), "English README.md does not exist."
    assert os.path.exists(fr_readme), "French README.fr.md does not exist."

if __name__ == "__main__":
    pytest.main([__file__])
