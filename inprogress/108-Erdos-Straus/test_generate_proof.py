import os
import sys
import io
import unittest
import subprocess
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_latex, main

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_main(self, mock_run):
        # Mock file operations to test generation without writing to disk
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            with patch('os.makedirs') as mocked_makedirs:
                main()

                # Check if correct file path was used
                directory = os.path.dirname(os.path.abspath(sys.modules['generate_proof'].__file__))
                filepath = os.path.join(directory, "108-Erdos-Straus-Proof.tex")
                mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

                # Ensure something was written
                handle = mocked_file()
                self.assertTrue(handle.write.called)

                # Retrieve all written content
                content = "".join(call.args[0] for call in handle.write.call_args_list)

                # Verify key sections
                self.assertIn("erdos_straus_predicate", content)
                self.assertIn("Architecture de Formalisation dans Lean 4", content)

                # Verify pdflatex was called twice
                self.assertEqual(mock_run.call_count, 2)

    @patch('subprocess.run')
    def test_subprocess_error(self, mock_run):
        # Simulate pdflatex failing
        mock_run.side_effect = subprocess.CalledProcessError(1, 'pdflatex')

        with patch('builtins.open', new_callable=mock_open):
            with patch('os.makedirs'):
                with self.assertRaises(subprocess.CalledProcessError):
                    main()

if __name__ == '__main__':
    unittest.main()
