import unittest
import sys
import os

# Add current directory to path so generate_proof can be imported
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from generate_proof import generate_latex

class TestGenerateProof(unittest.TestCase):
    def test_generate_latex(self):
        tex = generate_latex()

        # Verify it returns a string
        self.assertIsInstance(tex, str)

        # Verify essential LaTeX components
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", tex)
        self.assertIn(r"\begin{document}", tex)
        self.assertIn(r"\end{document}", tex)
        self.assertIn(r"\author{Charles EDOU NZE\thanks{Chercheur indépendant / Independent Researcher}}", tex)

        # Verify the generated text has substantial content
        self.assertTrue(len(tex) > 1000)

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', __file__])
