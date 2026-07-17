import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unittest
from unittest.mock import patch, mock_open
import subprocess

from generate_proof import main

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_main_runs_pdflatex(self, mock_file, mock_run):
        # We mock subprocess.run to avoid compiling latex during unit tests
        main()

        # Verify that subprocess.run is called with the expected arguments, including check=True
        expected_directory = os.path.dirname(os.path.abspath(sys.modules['generate_proof'].__file__))
        expected_filepath = os.path.join(expected_directory, "108-Erdos-Straus-Proof.tex")
        expected_call = unittest.mock.call(["pdflatex", "-interaction=nonstopmode", "-output-directory", expected_directory, expected_filepath], capture_output=True, text=True, check=True)

        self.assertEqual(mock_run.call_count, 2)
        mock_run.assert_has_calls([expected_call, expected_call])

if __name__ == '__main__':
    unittest.main()
