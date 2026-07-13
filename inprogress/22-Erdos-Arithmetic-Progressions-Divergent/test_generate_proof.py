import unittest
import os
import sys
from unittest.mock import patch

# Add the directory to sys.path to allow importing the module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import generate_proof

class TestGenerateProof(unittest.TestCase):
    def test_generate_tex_header(self):
        header = generate_proof.generate_tex_header()
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", header)
        self.assertIn("Erd\H{o}s", header)
        self.assertNotIn("Comme demandé", header)
        self.assertNotIn("zéro-ellipse", header.lower())

    def test_procedural_fourier_matrices(self):
        body = generate_proof.procedural_fourier_matrices()
        self.assertIn("Traces Explicites des Matrices de Fourier Modulaires", body)
        self.assertIn("Analyse sur $\mathbb{Z}/3\mathbb{Z}$", body)
        self.assertNotIn("Cette étape démontre", body)

    def test_procedural_gowers_norms(self):
        body = generate_proof.procedural_gowers_norms()
        self.assertIn("Expansions Combinatoires des Inégalités de Gowers", body)
        self.assertIn("Évaluation de la Norme $U^{3}$ et Nil-Variétés de Rang 2", body)

    def test_procedural_tauberian_bounds(self):
        body = generate_proof.procedural_tauberian_bounds()
        self.assertIn("Dissection Dyadique et Théorèmes Taubériens", body)
        self.assertIn("Fenêtre d'Analyse Asymptotique", body)

    def test_generate_lean_skeleton(self):
        skeleton = generate_proof.generate_lean_skeleton()
        self.assertIn("HarmonicDivergence", skeleton)
        self.assertIn("HasArithmeticProgression", skeleton)
        self.assertIn("erdos_ap_conjecture", skeleton)
        self.assertIn("-- Il s'agit d'une esquisse de preuve incomplete", skeleton)

    @patch('subprocess.run')
    def test_generate_tex(self, mock_run):
        # We mock subprocess.run to avoid compiling latex during unit tests
        # We also mock file operations to prevent writing to disk
        with patch('builtins.open'):
            generate_proof.generate_tex()
            self.assertTrue(mock_run.called)
            # Ensure pdflatex is called at least once
            self.assertEqual(mock_run.call_args_list[0][0][0][0], "pdflatex")

if __name__ == '__main__':
    unittest.main()
