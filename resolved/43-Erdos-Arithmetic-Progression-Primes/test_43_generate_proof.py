import os
import unittest
from unittest.mock import patch, mock_open
import importlib.util

class TestGenerateProofs(unittest.TestCase):
    def setUp(self):
        # Load the module dynamically
        spec = importlib.util.spec_from_file_location(
            "generate_proofs",
            "resolved/43-Erdos-Arithmetic-Progression-Primes/generate_proofs.py"
        )
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_proof_en(self, mock_file):
        self.module.write_proof_en()
        mock_file.assert_called_once_with('resolved/43-Erdos-Arithmetic-Progression-Primes/proof.tex', 'w', encoding='utf-8')

        # Verify content written
        handle = mock_file()
        content = "".join(call.args[0] for call in handle.write.mock_calls)

        # Check required architectural elements
        self.assertIn("Axiomatic Definitions and Type Specifications", content)
        self.assertIn("HasArithmeticProgression", content)
        self.assertIn("green_tao_theorem", content)
        self.assertIn("Charles EDOU NZE", content)
        self.assertNotIn("Comme demandé", content) # Anti-meta check

    @patch('builtins.open', new_callable=mock_open)
    def test_write_proof_fr(self, mock_file):
        self.module.write_proof_fr()
        mock_file.assert_called_once_with('resolved/43-Erdos-Arithmetic-Progression-Primes/proof.fr.tex', 'w', encoding='utf-8')

        # Verify content written
        handle = mock_file()
        content = "".join(call.args[0] for call in handle.write.mock_calls)

        # Check required architectural elements
        self.assertIn("D\\'efinitions Axiomatiques et Sp\\'ecifications de Type", content)
        self.assertIn("HasArithmeticProgression", content)
        self.assertIn("green_tao_theorem", content)
        self.assertIn("Charles EDOU NZE", content)
        self.assertNotIn("Comme demandé", content) # Anti-meta check

if __name__ == '__main__':
    unittest.main()
