import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import generate_en
import generate_fr

def test_generate_en():
    generate_en.generate_tex()
    assert os.path.exists("124-Erdos-Moser.tex")

def test_generate_fr():
    generate_fr.generate_tex()
    assert os.path.exists("124-Erdos-Moser.fr.tex")
