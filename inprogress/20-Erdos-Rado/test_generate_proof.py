import unittest
from unittest.mock import patch
import os
import sys

# Make sure we can import the generator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import build_latex

class TestErdosRadoGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_build_latex_does_not_call_actual_pdflatex(self, mock_run):
        """Test that build_latex generates the .tex file and calls pdflatex without actually compiling"""
        # Save old contents to restore later
        tex_path = "inprogress/20-Erdos-Rado/20-proof.tex"
        old_content = None
        if os.path.exists(tex_path):
            with open(tex_path, "r", encoding="utf-8") as f:
                old_content = f.read()

        try:
            build_latex()

            # Check if the file was created
            self.assertTrue(os.path.exists(tex_path))

            # Check file content
            with open(tex_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("Erdős-Rado", content)

            # Verify subprocess was called for pdflatex
            self.assertTrue(mock_run.called)
            args = mock_run.call_args[0][0]
            self.assertEqual(args[0], "pdflatex")

        finally:
            # Clean up
            if old_content is not None:
                with open(tex_path, "w", encoding="utf-8") as f:
                    f.write(old_content)
            elif os.path.exists(tex_path):
                os.remove(tex_path)

if __name__ == "__main__":
    unittest.main()
