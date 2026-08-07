import os
import subprocess
import pytest

def test_pdf_exists_and_length():
    # PDF should remain in the inprogress directory because the proof uses 'sorry' and is unresolved
    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Erdos_Problem_1.pdf")

    # 1. Verify existence
    assert os.path.exists(pdf_path), f"PDF not found at {pdf_path}"

    # 2. Verify page count using pdfinfo
    try:
        result = subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True, check=True)
        pages_line = [line for line in result.stdout.split('\n') if line.startswith('Pages:')]
        assert len(pages_line) == 1, "Could not find 'Pages:' in pdfinfo output"

        pages_count = int(pages_line[0].split(':')[1].strip())
        assert 10 <= pages_count <= 150, f"PDF page count ({pages_count}) is not between 10 and 150"

    except subprocess.CalledProcessError as e:
        pytest.fail(f"pdfinfo command failed: {e.stderr}")
    except FileNotFoundError:
        pytest.fail("pdfinfo command not found. Ensure poppler-utils is installed.")

if __name__ == '__main__':
    pytest.main(["-v", __file__])
