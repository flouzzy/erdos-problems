import os
import sys
import io
import unittest
import subprocess
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_generate_tex(self, mock_run):
        # Mock file operations to test generation without writing to disk
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            with patch('os.makedirs') as mocked_makedirs:
                generate_tex()

                # Check if correct file path was used
                filepath = "inprogress/Erdos-Straus/Erdos-Problem-Straus.tex"
                mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

                # Ensure something was written
                handle = mocked_file()
                self.assertTrue(handle.write.called)

                # Retrieve all written content
                content = "".join(call.args[0] for call in handle.write.call_args_list)

                # Verify key sections
                self.assertIn(r"\title{Sur la Conjecture d'Erdős-Straus : Analyse Algébrique et Décomposition Modulaire}", content)
                self.assertIn("def SatisfiesErdosStraus (n : Nat) : Prop :=", content)
                self.assertIn("lemma erdos_straus_mod_4_3 (k : Nat) : SatisfiesErdosStraus (4 * k + 3)", content)
                self.assertIn("theorem erdos_straus_conjecture (n : Nat) (hn : n >= 2)", content)

    @patch('subprocess.run')
    def test_generate_tex_subprocess_error(self, mock_run):
        # Simulate pdflatex failing
        mock_run.side_effect = subprocess.CalledProcessError(1, 'pdflatex')

        with patch('builtins.open', new_callable=mock_open):
            with patch('os.makedirs'):
                with patch('sys.stderr', new_callable=io.StringIO) as mock_stderr:
                    generate_tex()
                    # The script might not explicitly print error, so we just check no exception is raised
                    pass

if __name__ == '__main__':
    unittest.main()
