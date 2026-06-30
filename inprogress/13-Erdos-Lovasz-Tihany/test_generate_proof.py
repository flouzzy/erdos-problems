import unittest
from unittest.mock import patch, mock_open, call
import sys
import os
import pytest

# Add the directory to the path so we can import the script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex

class TestGenerateProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        generate_tex()

        # Verify open was called correctly
        mock_file.assert_called_once_with('13-proof.tex', 'w', encoding='utf-8')

        # Verify writing logic
        handle = mock_file()

        # We need to collect all written parts to check the content
        written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

        # Verify LaTeX structure and expected strings
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", written_content)
        self.assertIn("Charles EDOU NZE", written_content)
        self.assertIn(r"\begin{document}", written_content)
        self.assertIn(r"\end{document}", written_content)
        self.assertIn(r"\subsection{Démonstration Exacte pour $s=2$ et $t=2$}", written_content)

if __name__ == '__main__':
    pytest.main(['-v', __file__])
