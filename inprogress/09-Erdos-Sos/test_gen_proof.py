import unittest
from unittest.mock import patch, mock_open
import gen_proof_en
import gen_proof_fr

class TestGenerateProof(unittest.TestCase):
    def test_gen_proof_en(self):
        m = mock_open()
        with patch('builtins.open', m):
            gen_proof_en.generate_tex()

        handle = m()
        written = "".join(call.args[0] for call in handle.write.mock_calls)

        self.assertIn("Charles EDOU NZE, chercheur", written)
        self.assertNotIn("Comme demand", written)
        self.assertNotIn("AI", written)
        self.assertNotIn("meta-commentary", written)
        self.assertIn("Lean 4", written)
        self.assertIn("HasEmbedding", written)

    def test_gen_proof_fr(self):
        m = mock_open()
        with patch('builtins.open', m):
            gen_proof_fr.generate_tex()

        handle = m()
        written = "".join(call.args[0] for call in handle.write.mock_calls)

        self.assertIn("Charles EDOU NZE, chercheur", written)
        self.assertNotIn("Comme demand", written)
        self.assertNotIn("AI", written)
        self.assertNotIn("meta-commentary", written)
        self.assertIn("Lean 4", written)
        self.assertIn("HasEmbedding", written)
        self.assertIn("usepackage[french]{babel}", written)

if __name__ == '__main__':
    unittest.main()
