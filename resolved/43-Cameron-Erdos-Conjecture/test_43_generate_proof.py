import os
import unittest
from unittest.mock import patch, mock_open

# We import the scripts dynamically or define paths to test
from generate_proof_en import generate_tex as generate_tex_en
from generate_proof_fr import generate_tex as generate_tex_fr

class TestCameronErdosGeneration(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex_en(self, mock_file):
        generate_tex_en()
        mock_file.assert_called_with(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proof.tex'), 'w', encoding='utf-8')
        handle = mock_file()
        content = "".join([call[0][0] for call in handle.write.call_args_list])
        self.assertIn("Cameron-Erd", content)
        self.assertIn("Charles EDOU NZE", content)
        self.assertIn("IsSumFree", content)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex_fr(self, mock_file):
        generate_tex_fr()
        mock_file.assert_called_with(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proof.fr.tex'), 'w', encoding='utf-8')
        handle = mock_file()
        content = "".join([call[0][0] for call in handle.write.call_args_list])
        self.assertIn("Cameron-Erd", content)
        self.assertIn("Charles EDOU NZE", content)
        self.assertIn("IsSumFree", content)

if __name__ == "__main__":
    unittest.main()
