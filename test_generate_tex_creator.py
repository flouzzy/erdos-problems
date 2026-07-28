import unittest
from unittest.mock import patch, mock_open
import generate_tex_creator

from fractions import Fraction

class TestGenerateTexCreator(unittest.TestCase):
    def test_generate_tex_header(self):
        header = generate_tex_creator.generate_tex_header()
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", header)
        self.assertIn(r"\begin{document}", header)
        self.assertIn(r"\usepackage[utf8]{inputenc}", header)
        self.assertIn(r"\usepackage{amsmath, amssymb, amsthm}", header)
        self.assertIn(r"\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d'Erd\H{o}s-Straus}", header)
        self.assertIn(r"\author{Charles EDOU NZE\thanks{Chercheur indépendant / Independent Researcher}}", header)

    def test_find_solution(self):
        # Valid cases
        cases = [
            (2, (1, 2, 2)),
            (3, (1, 4, 12)),
            (4, (2, 3, 6))
        ]
        for n, expected in cases:
            with self.subTest(n=n):
                sol = generate_tex_creator.find_solution(n)
                self.assertEqual(sol, expected)
                if sol:
                    x, y, z = sol
                    self.assertEqual(Fraction(4, n), Fraction(1, x) + Fraction(1, y) + Fraction(1, z))

        # Invalid cases (no solution or invalid input)
        for n in [1, 0, -1]:
            with self.subTest(n=n):
                self.assertIsNone(generate_tex_creator.find_solution(n))


    def test_generate_tex_proof_section(self):
        # Test for n=2, x=1, y=2, z=2
        # LCM(1, 2) = 2, LCM(2, 2) = 2 -> lcm_xyz = 2
        # num_x = 2, num_y = 1, num_z = 1 -> sum = 4
        # GCD(4, 2) = 2, simp_num = 2, simp_den = 1
        output_2 = generate_tex_creator.generate_tex_proof_section(2, 1, 2, 2)

        self.assertIn("\\subsection{Démonstration pour $n = 2$}", output_2)
        self.assertIn("Posons $x = 1$, $y = 2$, $z = 2$.", output_2)
        self.assertIn("Le PPCM des dénominateurs est $\\text{PPCM}(1, 2, 2) = 2$.", output_2)
        self.assertIn("\\frac{1}{1} = \\frac{2}{2}", output_2)
        self.assertIn("\\frac{1}{2} = \\frac{1}{2}", output_2)
        self.assertIn("\\frac{1}{2} = \\frac{1}{2}", output_2)
        self.assertIn("\\frac{1}{1} + \\frac{1}{2} + \\frac{1}{2} = \\frac{2 + 1 + 1}{2} = \\frac{4}{2}", output_2)
        self.assertIn("Le PGCD du numérateur et du dénominateur est $\\text{PGCD}(4, 2) = 2$.", output_2)
        self.assertIn("\\frac{4}{2} = \\frac{4 \\div 2}{2 \\div 2} = \\frac{2}{1}", output_2)

        # Test for n=3, x=1, y=4, z=12
        # LCM(1, 4) = 4, LCM(4, 12) = 12 -> lcm_xyz = 12
        # num_x = 12, num_y = 3, num_z = 1 -> sum = 16
        # GCD(16, 12) = 4, simp_num = 4, simp_den = 3
        output_3 = generate_tex_creator.generate_tex_proof_section(3, 1, 4, 12)

        self.assertIn("\\subsection{Démonstration pour $n = 3$}", output_3)
        self.assertIn("Posons $x = 1$, $y = 4$, $z = 12$.", output_3)
        self.assertIn("Le PPCM des dénominateurs est $\\text{PPCM}(1, 4, 12) = 12$.", output_3)
        self.assertIn("\\frac{1}{1} = \\frac{12}{12}", output_3)
        self.assertIn("\\frac{1}{4} = \\frac{3}{12}", output_3)
        self.assertIn("\\frac{1}{12} = \\frac{1}{12}", output_3)
        self.assertIn("\\frac{1}{1} + \\frac{1}{4} + \\frac{1}{12} = \\frac{12 + 3 + 1}{12} = \\frac{16}{12}", output_3)
        self.assertIn("Le PGCD du numérateur et du dénominateur est $\\text{PGCD}(16, 12) = 4$.", output_3)
        self.assertIn("\\frac{16}{12} = \\frac{16 \\div 4}{12 \\div 4} = \\frac{4}{3}", output_3)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        generate_tex_creator.generate_tex()

        # Verify open was called correctly
        mock_file.assert_called_once_with('inprogress/01-Erdos-Straus/generate_tex_creator.py', 'w', encoding='utf-8')

        # Verify writing logic
        handle = mock_file()

        # We need to collect all written parts to check the content
        written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

        # Verify python script components are present
        self.assertIn("import os\n", written_content)
        self.assertIn("tex_content = r\"\"\"", written_content)
        self.assertIn("with open('inprogress/01-Erdos-Straus/01-proof.tex', 'w', encoding='utf-8') as f:", written_content)
        self.assertIn("f.write(tex_content)", written_content)

        # Verify LaTeX structure
        self.assertIn("\\documentclass[11pt,a4paper]{article}", written_content)
        self.assertIn("\\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d'Erd\\H{o}s-Straus}", written_content)
        self.assertIn("\\begin{document}", written_content)
        self.assertIn("\\end{document}", written_content)

        # Verify some generated proof logic
        # For n=2: 4/2 = 1/x + 1/y + 1/z -> e.g. x=1, y=2, z=2 ? Let's see what the generation yields for n=2
        # We can just assert that \subsection{Démonstration pour $n = 2$} exists
        self.assertIn("\\subsection{Démonstration pour $n = 2$}", written_content)
        self.assertIn("\\subsection{Démonstration pour $n = 300$}", written_content)

        # Verify the file closes with proper multi-line string termination
        self.assertIn("\"\"\"\nwith open", written_content)


    def test_generate_tex_conclusion(self):
        result = generate_tex_creator.generate_tex_conclusion()
        self.assertIn(r"\section{Conclusion}", result)
        self.assertIn("Cette documentation présente", result)
        self.assertIn(r"\end{document}", result)

if __name__ == '__main__':
    unittest.main()
