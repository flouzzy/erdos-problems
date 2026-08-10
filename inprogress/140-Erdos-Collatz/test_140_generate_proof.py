import os
import unittest
from unittest.mock import patch, mock_open
import generate_proof_en
import generate_proof_fr

class TestGenerateProofs(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_proof_en(self, mock_file):
        generate_proof_en.generate_proof_en()
        mock_file.assert_called_with('inprogress/140-Erdos-Collatz/proof.tex', 'w', encoding='utf-8')
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.mock_calls)
        self.assertIn(r"Charles EDOU NZE", written_content)
        self.assertIn(r"\begin{verbatim}", written_content)
        self.assertIn(r"has_finite_stopping_time", written_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_proof_fr(self, mock_file):
        generate_proof_fr.generate_proof_fr()
        mock_file.assert_called_with('inprogress/140-Erdos-Collatz/proof.fr.tex', 'w', encoding='utf-8')
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.mock_calls)
        self.assertIn(r"Charles EDOU NZE", written_content)
        self.assertIn(r"\begin{verbatim}", written_content)
        self.assertIn(r"\usepackage[french]{babel}", written_content)
        self.assertIn(r"has_finite_stopping_time", written_content)

    def test_pdf_exists(self):
        self.assertTrue(os.path.exists('inprogress/140-Erdos-Collatz/140-Erdos-Collatz.pdf'))
        self.assertTrue(os.path.exists('inprogress/140-Erdos-Collatz/140-Erdos-Collatz.fr.pdf'))

if __name__ == '__main__':
    unittest.main()
