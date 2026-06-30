import unittest
from unittest.mock import patch, mock_open

from generate_erdos_gyarfas_proof import generate_tex

class TestGenerateErdosGyarfasProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        generate_tex()

        # Verify open was called correctly
        mock_file.assert_called_once_with('inprogress/04-Erdos-Gyarfas/04-proof.tex', 'w', encoding='utf-8')

        # Verify writing logic
        handle = mock_file()
        written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

        # Verify LaTeX structure
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", written_content)
        self.assertIn(r"\title{Analyse et Esquisse de Preuve Formelle de la Conjecture d'Erdos-Gyarfas}", written_content)
        self.assertIn(r"\begin{document}", written_content)
        self.assertIn(r"\end{document}", written_content)

        # Verify loops and generation logic
        self.assertIn(r"\subsection{Verification pour graphe 3-regulier avec $n=6$ sommets}", written_content)
        self.assertIn(r"\subsection{Verification pour graphe 3-regulier avec $n=798$ sommets}", written_content)

if __name__ == '__main__':
    unittest.main()
