import unittest
import os
from pypdf import PdfReader
import generate_56_proofs

class Test56GenerateProof(unittest.TestCase):
    def test_get_header(self):
        content_en = generate_56_proofs.get_header('en')
        self.assertIn("Charles EDOU NZE, chercheur ind\\'ependant", content_en)
        content_fr = generate_56_proofs.get_header('fr')
        self.assertIn("Charles EDOU NZE, chercheur ind\\'ependant", content_fr)

    def test_get_intro_and_literature(self):
        content = generate_56_proofs.get_intro_and_literature('en')
        self.assertIn("Contextual Literature Research", content)
        self.assertIn("Szemer\\'edi", content)

    def test_get_lean4(self):
        content = generate_56_proofs.get_lean4('en')
        self.assertNotIn("∃", content)
        self.assertNotIn("∀", content)
        self.assertNotIn("ℕ", content)
        self.assertIn("Exists", content)
        self.assertIn("forall", content)
        self.assertIn("lemma basis_counting_lower_bound", content)

    def test_pdf_generated(self):
        pdf_path_en = os.path.join(os.path.dirname(__file__), "56-Erdos-Turan-Additive-Bases.pdf")
        pdf_path_fr = os.path.join(os.path.dirname(__file__), "56-Erdos-Turan-Additive-Bases-FR.pdf")

        self.assertTrue(os.path.exists(pdf_path_en))
        self.assertTrue(os.path.exists(pdf_path_fr))

        reader_en = PdfReader(pdf_path_en)
        self.assertGreaterEqual(len(reader_en.pages), 3)

        reader_fr = PdfReader(pdf_path_fr)
        self.assertGreaterEqual(len(reader_fr.pages), 3)

if __name__ == '__main__':
    unittest.main()
