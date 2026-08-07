import unittest
from unittest.mock import patch, mock_open
import os
import subprocess
from generate_proof import generate_proof
from generate_proof_fr import generate_proof as generate_proof_fr

class TestGenerateProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('subprocess.run')
    @patch('os.rename')
    def test_generate_proof_en(self, mock_rename, mock_subprocess, mock_open_func):
        generate_proof()

        # Verify open was called
        mock_open_func.assert_called_with("proof.tex", "w")

        # Get what was written
        handle = mock_open_func()
        write_calls = handle.write.call_args_list
        content = "".join([call[0][0] for call in write_calls])

        # Verify content
        self.assertIn("Erdős-Straus", content)
        self.assertIn(r"\begin{proof}", content)

        # Verify subprocess calls
        self.assertEqual(mock_subprocess.call_count, 2)
        mock_subprocess.assert_called_with(["pdflatex", "-interaction=nonstopmode", "proof.tex"])

        # Verify rename call
        mock_rename.assert_called_once_with("proof.pdf", "109-Erdos-Straus.pdf")

    @patch('builtins.open', new_callable=mock_open)
    @patch('subprocess.run')
    @patch('os.rename')
    def test_generate_proof_fr(self, mock_rename, mock_subprocess, mock_open_func):
        generate_proof_fr()

        # Verify open was called
        mock_open_func.assert_called_with("proof.fr.tex", "w")

        # Get what was written
        handle = mock_open_func()
        write_calls = handle.write.call_args_list
        content = "".join([call[0][0] for call in write_calls])

        # Verify content
        self.assertIn("Erdős-Straus", content)
        self.assertIn(r"\begin{proof}", content)

        # Verify subprocess calls
        self.assertEqual(mock_subprocess.call_count, 2)
        mock_subprocess.assert_called_with(["pdflatex", "-interaction=nonstopmode", "proof.fr.tex"])

        # Verify rename call
        mock_rename.assert_called_once_with("proof.fr.pdf", "109-Erdos-Straus.fr.pdf")

if __name__ == '__main__':
    unittest.main()
