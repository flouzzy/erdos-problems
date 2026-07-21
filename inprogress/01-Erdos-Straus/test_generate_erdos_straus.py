import os
import sys
import unittest
import subprocess
from unittest.mock import patch, mock_open

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_erdos_straus import main

class TestGenerateErdosStraus(unittest.TestCase):
    @patch('subprocess.run')
    def test_main(self, mock_run):
        # Mock file operations to test generation without writing to disk
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            main()

            # Check if correct file path was used
            script_dir = os.path.dirname(os.path.abspath(sys.modules['generate_erdos_straus'].__file__))
            filepath = os.path.join(script_dir, "Erdos_Problem_01_Straus.tex")
            mocked_file.assert_called_with(filepath, 'w', encoding='utf-8')

            # Ensure something was written
            handle = mocked_file()
            self.assertTrue(handle.write.called)

            # Retrieve all written content
            content = "".join(call.args[0] for call in handle.write.call_args_list)

            # Verify key sections
            self.assertIn(r"\section{Proof Strategy and Lemma Isolation}", content)
            self.assertIn(r"\title{Rigorous Analysis and Partial Resolution Strategies for the Erd\H{o}s-Straus Conjecture}", content)
            self.assertIn(r"\documentclass[12pt, a4paper]{article}", content)
            self.assertIn(r"\begin{document}", content)
            self.assertIn(r"\end{document}", content)

            # Verify pdflatex was called
            mock_run.assert_called_once()
            args, kwargs = mock_run.call_args
            self.assertEqual(args[0], ["pdflatex", "-interaction=nonstopmode", "Erdos_Problem_01_Straus.tex"])
            self.assertEqual(kwargs['cwd'], script_dir)
            self.assertTrue(kwargs['check'])

    @patch('subprocess.run')
    def test_main_subprocess_error(self, mock_run):
        # Simulate pdflatex failing
        mock_run.side_effect = subprocess.CalledProcessError(1, 'pdflatex')

        with patch('builtins.open', new_callable=mock_open):
            with self.assertRaises(subprocess.CalledProcessError):
                main()

if __name__ == '__main__':
    unittest.main()
