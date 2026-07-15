import os
import sys
import unittest
import subprocess
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex_header, generate_analytical_derivations, generate_tex

class TestGenerateProof(unittest.TestCase):
    def test_generate_tex_header(self):
        header = generate_tex_header()
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", header)
        self.assertIn(r"\begin{lstlisting}[language=Caml]", header)

    def test_generate_analytical_derivations(self):
        derivations = generate_analytical_derivations()
        self.assertIn(r"\section{Expansion Théorique : L'Approche Analytique et Harmonique}", derivations)

    @patch('subprocess.run')
    @patch('os.makedirs')
    def test_generate_tex(self, mock_makedirs, mock_subprocess_run):
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            generate_tex()

            filepath = os.path.join("inprogress", "16-Erdos-Turan-Additive-Bases", "16-proof.tex")
            mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

            handle = mocked_file()
            self.assertTrue(handle.write.called)

            content = "".join(call.args[0] for call in handle.write.call_args_list)
            self.assertIn(r"\documentclass[11pt,a4paper]{article}", content)
            self.assertIn(r"\section{Expansion Théorique : L'Approche Analytique et Harmonique}", content)

if __name__ == '__main__':
    unittest.main()
