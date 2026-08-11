import unittest
from unittest.mock import patch, mock_open
import gen_proof_en
import gen_proof_fr

class TestErdosDiscrepancyGenerators(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_gen_proof_en(self, mock_file):
        gen_proof_en.generate_tex()
        mock_file.assert_called_with('proof.tex', 'w', encoding='utf-8')

        # Verify specific content
        written_content = "".join(call.args[0] for call in mock_file().write.call_args_list)

        self.assertIn(r"Charles EDOU NZE, chercheur ind\'ependant", written_content)
        self.assertIn("Terence Tao", written_content)
        self.assertIn("def SignSeq := Nat -> Int", written_content)
        self.assertIn("completely multiplicative", written_content)

    @patch('builtins.open', new_callable=mock_open)
    def test_gen_proof_fr(self, mock_file):
        gen_proof_fr.generate_tex()
        mock_file.assert_called_with('proof.fr.tex', 'w', encoding='utf-8')

        # Verify specific content
        written_content = "".join(call.args[0] for call in mock_file().write.call_args_list)

        self.assertIn(r"Charles EDOU NZE, chercheur ind\'ependant", written_content)
        self.assertIn("Terence Tao", written_content)
        self.assertIn("def SignSeq := Nat -> Int", written_content)
        self.assertIn("compl\\`etement multiplicative", written_content)

if __name__ == '__main__':
    unittest.main()
