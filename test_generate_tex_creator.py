import unittest
from unittest.mock import patch, mock_open, call
import generate_tex_creator

class TestGenerateTexCreator(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        generate_tex_creator.generate_tex()

        # Verify open was called correctly
        mock_file.assert_called_once_with('inprogress/01-Erdos-Straus/generate_tex_creator.py', 'w', encoding='utf-8')

        # Verify writing logic
        handle = mock_file()

        # We need to collect all written parts to check the content
        written_content = ""
        for call_args in handle.write.call_args_list:
            written_content += call_args.args[0]

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

if __name__ == '__main__':
    unittest.main()
