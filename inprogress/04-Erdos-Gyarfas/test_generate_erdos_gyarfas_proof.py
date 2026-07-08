import unittest
from unittest.mock import patch, mock_open

from generate_proof import generate_tex

class TestGenerateErdosGyarfasProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        generate_tex()

        # Verify open was called correctly
        mock_file.assert_called_once_with('inprogress/04-Erdos-Gyarfas/04-Erdos-Gyarfas-Proof.tex', 'w', encoding='utf-8')

        # Verify writing logic
        handle = mock_file()
        written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

        # Verify LaTeX structure
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", written_content)
        self.assertIn(r"\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d'Erdös-Gyárfás}", written_content)
        self.assertIn(r"\begin{document}", written_content)
        self.assertIn(r"\end{document}", written_content)

        # Verify loops and generation logic
        self.assertIn(r"\subsection{Construction pour $d(G)=3$ de taille $N=4$}", written_content)
        self.assertIn(r"\subsection{Construction récursive de graphes de taille croissante}", written_content)

if __name__ == '__main__':
    unittest.main()
