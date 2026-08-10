import unittest
from unittest.mock import patch, mock_open
import generate_en

class TestGenerateEn(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex_content(self, mock_file):
        generate_en.generate_tex()

        # Combine all written chunks to get the full string
        written_content = "".join([call.args[0] for call in mock_file().write.call_args_list])

        # Verify essential components are present
        self.assertIn("Axiomatic Definitions", written_content)
        self.assertIn("Erd\\H{o}s-Straus equation", written_content)
        self.assertIn("Contextual Literature Research", written_content)
        self.assertIn("ArXiv", written_content)
        self.assertIn("begin{lemma}", written_content)
        self.assertIn("begin{proof}", written_content)
        self.assertIn("Autoformalization Architecture", written_content)
        self.assertIn("SatisfiesErdosStraus (n : Nat) : Prop", written_content)
        self.assertIn("Charles EDOU NZE", written_content)

if __name__ == '__main__':
    unittest.main()
