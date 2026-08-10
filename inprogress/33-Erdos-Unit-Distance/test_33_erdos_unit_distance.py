import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex_header, generate_analytical_derivations, generate_tex

class TestGenerateProof(unittest.TestCase):
    def test_generate_tex_header_en(self):
        header = generate_tex_header("en")
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", header)
        self.assertIn("Formal Analysis of the Erd\\H{o}s Unit Distance Problem", header)

    def test_generate_tex_header_fr(self):
        header = generate_tex_header("fr")
        self.assertIn(r"\usepackage[french]{babel}", header)
        self.assertIn("Analyse et Formalisation du Problème des Distances Unités d'Erd\\H{o}s", header)

    def test_generate_analytical_derivations(self):
        derivations = generate_analytical_derivations("en")
        self.assertIn(r"\section{Fourier Analytic Derivation and Zero-Ellipse Lemmas}", derivations)

        derivations_fr = generate_analytical_derivations("fr")
        self.assertIn(r"\section{Dérivation par Analyse de Fourier et Lemmes Analytiques}", derivations_fr)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mocked_file):
        generate_tex("en")
        filepath = os.path.join("inprogress", "33-Erdos-Unit-Distance", "proof.tex")
        mocked_file.assert_called_with(filepath, "w", encoding="utf-8")
        handle = mocked_file()
        self.assertTrue(handle.write.called)
        content = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("Formal Analysis of the Erd\\H{o}s Unit Distance Problem", content)

        generate_tex("fr")
        filepath_fr = os.path.join("inprogress", "33-Erdos-Unit-Distance", "proof.fr.tex")
        mocked_file.assert_called_with(filepath_fr, "w", encoding="utf-8")
        handle = mocked_file()
        self.assertTrue(handle.write.called)

if __name__ == '__main__':
    unittest.main()
