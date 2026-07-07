import unittest
import sys
import os
import pytest

# Add the directory to the path so we can import the script
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_readme_fr, generate_readme_en

class TestGenerateProof(unittest.TestCase):
    def test_generate_readme_fr(self):
        content = generate_readme_fr()
        self.assertIsInstance(content, str)
        self.assertIn("# 14 - Conjecture d'Erdős", content)
        self.assertIn("## 1. Analyse et Décomposition", content)
        self.assertIn("### Définitions Axiomatiques", content)
        self.assertIn("Architecture pour l'Autoformalisation (Lean 4)", content)

    def test_generate_readme_en(self):
        content = generate_readme_en()
        self.assertIsInstance(content, str)
        self.assertIn("# 14 - Erdős Conjecture", content)
        self.assertIn("## Problem Statement", content)
        self.assertIn("## Current Status", content)

if __name__ == '__main__':
    pytest.main(['-v', __file__])
