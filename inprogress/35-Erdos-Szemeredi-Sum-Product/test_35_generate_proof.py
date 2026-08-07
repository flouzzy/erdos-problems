import unittest
from unittest.mock import patch, mock_open
import importlib.util
import os

def load_module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class TestGenerateProofs(unittest.TestCase):
    def setUp(self):
        self.en_module = load_module_from_file(
            "generate_35_en",
            os.path.join(os.path.dirname(__file__), "generate_35_en.py")
        )
        self.fr_module = load_module_from_file(
            "generate_35_fr",
            os.path.join(os.path.dirname(__file__), "generate_35_fr.py")
        )

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_en_proof(self, mock_file):
        self.en_module.generate_proof()

        # Verify the file was opened for writing
        mock_file.assert_called_with('proof.tex', 'w')

        # Get the arguments passed to write
        handle = mock_file()
        write_args = handle.write.call_args[0][0]

        # Verify structure
        self.assertIn(r"\documentclass[12pt]{article}", write_args)
        self.assertIn("Charles EDOU NZE", write_args)
        self.assertIn("Erd\\H{o}s-Szemer\\'edi", write_args)
        self.assertIn("Lean 4", write_args)
        self.assertNotIn("As requested", write_args)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_fr_proof(self, mock_file):
        self.fr_module.generate_proof()

        # Verify the file was opened for writing
        mock_file.assert_called_with('proof.fr.tex', 'w')

        # Get the arguments passed to write
        handle = mock_file()
        write_args = handle.write.call_args[0][0]

        # Verify structure
        self.assertIn(r"\documentclass[12pt]{article}", write_args)
        self.assertIn("Charles EDOU NZE", write_args)
        self.assertIn("Erd\\H{o}s-Szemer\\'edi", write_args)
        self.assertIn("Lean 4", write_args)
        self.assertNotIn("Comme demand", write_args)

if __name__ == '__main__':
    unittest.main()
