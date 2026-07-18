import unittest
from unittest.mock import patch, mock_open
import os
import generate_proof

class TestGenerateProof(unittest.TestCase):
    def test_get_header(self):
        content = generate_proof.get_header()
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", content)
        self.assertIn("Erd\\H{o}s-Gy\\'arf\\'as", content)

    def test_get_lean4_architecture(self):
        content = generate_proof.get_lean4_architecture()
        self.assertIn("import Mathlib.Data.Nat.Basic", content)
        self.assertIn("erdos_gyarfas_conjecture", content)
        self.assertNotIn("∃", content) # Test for ascii chars only in Lean
        self.assertNotIn("∀", content)
        self.assertNotIn("ℕ", content)

    def test_get_extended_analysis(self):
        content = generate_proof.get_extended_analysis()
        self.assertIn("Rayleigh-Ritz", content)

    @patch('builtins.open', new_callable=mock_open)
    @patch('subprocess.run')
    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_main(self, mock_exists, mock_makedirs, mock_subprocess, mock_open_file):
        # Simulate directory does not exist
        mock_exists.return_value = False

        generate_proof.main()

        # Check directory creation
        mock_makedirs.assert_called_once()

        # Check file writing
        mock_open_file.assert_called_once()

        # Check subprocess calls (pdflatex called twice)
        self.assertEqual(mock_subprocess.call_count, 2)
        args, kwargs = mock_subprocess.call_args_list[0]
        self.assertEqual(args[0][0], "pdflatex")
        self.assertTrue(kwargs['check'])

if __name__ == '__main__':
    unittest.main()
