import unittest
from unittest.mock import patch, mock_open
import os
import gen_proof_en
import gen_proof_fr

class TestGenerateProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_gen_proof_en(self, mock_file):
        gen_proof_en.generate_latex()
        mock_file.assert_called_with('proof.tex', 'w', encoding='utf-8')

        # Check that the write was called and collect all written content
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)

        self.assertIn("Erd\\H{o}s-Szemer\\'edi", written_content)
        self.assertIn("Charles EDOU NZE", written_content)
        self.assertIn("\\begin{verbatim}", written_content)
        self.assertIn("def Sumset", written_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_gen_proof_fr(self, mock_file):
        gen_proof_fr.generate_latex()
        mock_file.assert_called_with('proof.fr.tex', 'w', encoding='utf-8')

        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)

        self.assertIn("Erd\\H{o}s-Szemer\\'edi", written_content)
        self.assertIn("Charles EDOU NZE", written_content)
        self.assertIn("Th\\'eor\\`eme", written_content)
        self.assertIn("\\begin{verbatim}", written_content)
        self.assertIn("def Sumset", written_content)

    def test_pdfs_exist(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.assertTrue(os.path.exists(os.path.join(base_dir, "35-Erdos-Szemeredi-Sum-Product.pdf")))
        self.assertTrue(os.path.exists(os.path.join(base_dir, "35-Erdos-Szemeredi-Sum-Product.fr.pdf")))

if __name__ == '__main__':
    unittest.main()
