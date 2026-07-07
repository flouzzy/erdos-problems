import os
import pytest
import sys

# Add the directory to the path so we can import generate_proof
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from generate_proof import generate_latex

def test_generate_latex():
    # Call the function to generate the LaTeX string
    tex_output = generate_latex()

    # Verify the output is a string
    assert isinstance(tex_output, str)

    # Verify key components of the LaTeX document are present
    assert r"\documentclass[11pt,a4paper]{article}" in tex_output
    assert r"\begin{document}" in tex_output
    assert r"\end{document}" in tex_output
    assert r"Charles EDOU NZE" in tex_output

    # Verify the presence of the required abstract and math concepts
    assert r"\begin{abstract}" in tex_output
    assert r"Erdős-Turán" in tex_output

    # Make sure we're getting a decent length document
    assert len(tex_output) > 1000

if __name__ == '__main__':
    pytest.main(['-v', __file__])
