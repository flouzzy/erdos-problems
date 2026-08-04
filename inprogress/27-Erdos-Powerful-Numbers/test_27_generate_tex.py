import unittest
from unittest.mock import patch, mock_open
import generate_tex
import os

class TestGenerateTex(unittest.TestCase):
    def test_generate_latex_file(self):
        with patch('builtins.open', new_callable=mock_open) as mock_file:
            generate_tex.generate_latex_file()

            mock_file.assert_called_once_with("inprogress/27-Erdos-Powerful-Numbers/27-Erdos-Powerful-Numbers.tex", "w", encoding="utf-8")

            # The file is written to. Let's get all the written content.
            handle = mock_file()
            written_content = "".join(call_args.args[0] for call_args in handle.write.call_args_list)

            self.assertIn(r"\documentclass[11pt,a4paper]{article}", written_content)
            self.assertIn(r"\title{Sur l'Inexistence de Trois Nombres Puissants Consécutifs : \\ Une Analyse Diophantienne Rigoureuse et Architecture d'Autoformalisation}", written_content)
            self.assertIn(r"\begin{document}", written_content)
            self.assertIn(r"\end{document}", written_content)
            self.assertIn(r"theorem erdos_powerful_conjecture", written_content)

if __name__ == '__main__':
    unittest.main()
