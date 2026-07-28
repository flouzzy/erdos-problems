import unittest
from unittest.mock import patch, mock_open, MagicMock
import generate_tex_creator
import os
from fractions import Fraction

class TestGenerateTexCreator(unittest.TestCase):
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

    def test_generate_tex(self):
        mock_file_handles = {}

        def mock_open_impl(filename, mode='r', **kwargs):
            m = mock_open()
            if 'w' in mode:
                mock_file_handles[filename] = m()
                return m(filename, mode, **kwargs)
            else:
                m_read = mock_open(read_data='\\documentclass[11pt,a4paper]{article}\n\\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d\'Erd\\H{o}s-Straus}\n\\begin{document}\n\\end{document}\n')
                return m_read(filename, mode, **kwargs)

        with patch('builtins.open', side_effect=mock_open_impl) as mock_file:
            generate_tex_creator.generate_tex()

            # Find the written file handle
            write_filename = 'inprogress/01-Erdos-Straus/generate_tex_creator.py'
            self.assertIn(write_filename, mock_file_handles)

            handle = mock_file_handles[write_filename]

            # We need to collect all written parts to check the content
            written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

            # Verify python script components are present
            self.assertIn("import os\n", written_content)
            self.assertIn("tex_content = r\"\"\"", written_content)
            self.assertIn("with open('inprogress/01-Erdos-Straus/01-proof.tex', 'w', encoding='utf-8') as f:", written_content)
            self.assertIn("f.write(tex_content)", written_content)

            # Verify LaTeX structure
            self.assertIn("\\documentclass[11pt,a4paper]{article}", written_content)
            self.assertIn("\\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d\'Erd\\H{o}s-Straus}", written_content)
            self.assertIn("\\begin{document}", written_content)
            self.assertIn("\\end{document}", written_content)

            # Verify some generated proof logic
            self.assertIn("\\subsection{Démonstration pour $n = 2$}", written_content)
            self.assertIn("\\subsection{Démonstration pour $n = 300$}", written_content)

            # Verify the file closes with proper multi-line string termination
            self.assertIn("\"\"\"\nwith open", written_content)

if __name__ == '__main__':
    unittest.main()
