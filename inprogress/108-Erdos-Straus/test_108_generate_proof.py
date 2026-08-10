import unittest
from unittest.mock import patch, mock_open
from generate_proof_en import generate_proof_en
from generate_proof_fr import generate_proof_fr

class TestGenerateProof(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_proof_en(self, mock_file):
        generate_proof_en()
        mock_file.assert_called_with('inprogress/108-Erdos-Straus/proof.tex', 'w', encoding='utf-8')

        # Verify specific structural elements
        handle = mock_file()
        content = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("Erd\\H{o}s-Straus Conjecture", content)
        self.assertIn("SatisfiesErdosStraus", content)
        self.assertIn("Axiomatic Definitions", content)
        self.assertIn("Charles EDOU NZE", content)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_proof_fr(self, mock_file):
        generate_proof_fr()
        mock_file.assert_called_with('inprogress/108-Erdos-Straus/proof.fr.tex', 'w', encoding='utf-8')

        # Verify specific structural elements
        handle = mock_file()
        content = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("Conjecture d'Erd\\H{o}s-Straus", content)
        self.assertIn("SatisfiesErdosStraus", content)
        self.assertIn("Charles EDOU NZE", content)

if __name__ == '__main__':
    unittest.main()
