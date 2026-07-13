import unittest
import os
import sys
from unittest.mock import patch

# Add the directory to the path so we can import the script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_proof

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_generate_latex(self, mock_subprocess):
        # Prevent actual pdflatex compilation during test
        mock_subprocess.return_value = None

        # Determine paths relative to this test file
        test_dir = os.path.dirname(os.path.abspath(__file__))
        tex_path = os.path.join(test_dir, '22-proof.tex')

        # Ensure file doesn't exist to start
        if os.path.exists(tex_path):
            os.remove(tex_path)

        # Change current working directory to test dir to match script behavior
        old_cwd = os.getcwd()
        os.chdir(test_dir)
        try:
            # Run generator
            generate_proof.generate_latex()

            # Verify file creation
            self.assertTrue(os.path.exists('22-proof.tex'))

            # Read content and verify specific contents (Groundedness Rule)
            with open('22-proof.tex', 'r', encoding='utf-8') as f:
                content = f.read()

            self.assertIn(r'\begin{document}', content)
            self.assertIn(r'\end{document}', content)
            self.assertIn(r'Squarefree', content)
            self.assertIn(r'Kummer', content)

            # Verify that anti-meta-commentary instructions are obeyed
            # (No 'zero ellipse', 'Comme demandé', etc. explicitly requested to avoid)
            self.assertNotIn('zero ellipse', content.lower())
            self.assertNotIn('zéro ellipse', content.lower())
            self.assertNotIn('comme demandé', content.lower())

        finally:
            os.chdir(old_cwd)
            # Clean up
            if os.path.exists(tex_path):
                os.remove(tex_path)

if __name__ == '__main__':
    unittest.main()
