import unittest
import os
import sys

# Add the directory containing the module to the python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from generate_proof import generate_latex

class TestGenerateProof(unittest.TestCase):
    def test_generate_latex(self):
        latex_content = generate_latex()

        # Verify it returns a string
        self.assertIsInstance(latex_content, str)

        # Verify it contains essential LaTeX keywords
        self.assertIn(r"\documentclass", latex_content)
        self.assertIn(r"\begin{document}", latex_content)
        self.assertIn(r"\end{document}", latex_content)
        self.assertIn(r"\usepackage", latex_content)

if __name__ == '__main__':
    unittest.main()
