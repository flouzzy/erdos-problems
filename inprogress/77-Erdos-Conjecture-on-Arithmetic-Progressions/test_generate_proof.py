import os
import sys
import unittest
import subprocess
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof_en import generate_tex as generate_tex_en
from generate_proof_fr import generate_tex as generate_tex_fr

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_generate_tex_en(self, mock_run):
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            generate_tex_en()

            filepath = "77-Erdos-Conjecture-on-Arithmetic-Progressions.tex"
            mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

            handle = mocked_file()
            self.assertTrue(handle.write.called)
            content = "".join(call.args[0] for call in handle.write.call_args_list)

            self.assertIn(r"\title{On the Erd\H{o}s Conjecture on Arithmetic Progressions: Formal Structures and Structural Decompositions}", content)
            self.assertIn("A relative Szemer\\'edi theorem", content)
            self.assertIn("theorem erdos_ap_conjecture", content)
            self.assertIn("Charles EDOU NZE, chercheur ind\\'ependant", content)

    @patch('subprocess.run')
    def test_generate_tex_fr(self, mock_run):
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            generate_tex_fr()

            filepath = "77-Erdos-Conjecture-on-Arithmetic-Progressions.fr.tex"
            mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

            handle = mocked_file()
            self.assertTrue(handle.write.called)
            content = "".join(call.args[0] for call in handle.write.call_args_list)

            self.assertIn(r"\title{Sur la Conjecture d'Erd\H{o}s sur les Progressions Arithm\'etiques : Structures Formelles et D\'ecompositions Structurelles}", content)
            self.assertIn(r"\usepackage[french]{babel}", content)
            self.assertIn("theorem erdos_ap_conjecture", content)
            self.assertIn("Charles EDOU NZE, chercheur ind\\'ependant", content)

if __name__ == '__main__':
    unittest.main()
