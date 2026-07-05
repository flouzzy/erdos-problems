import os
import sys
import unittest
import PyPDF2
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_generate_tex(self, mock_run):
        # Mock file operations to test generation without writing to disk
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            with patch('os.makedirs') as mocked_makedirs:
                generate_tex()

                # Check if correct file path was used
                filepath = "inprogress/04-Erdos-Gyarfas/04-Erdos-Gyarfas-Proof.tex"
                mocked_file.assert_called_with(filepath, "w", encoding="utf-8")

                # Ensure something was written
                handle = mocked_file()
                self.assertTrue(handle.write.called)

                # Retrieve all written content
                content = "".join(call.args[0] for call in handle.write.call_args_list)

                # Verify key sections
                self.assertIn(r"\title{Analyse Structurale et Preuves Constructives Explicites de la Conjecture d'Erdös-Gyárfás}", content)
                self.assertIn("ErdosGyarfasPredicate", content)
                self.assertIn("Analyse du pire cas : Arbre 3-régulier de profondeur $2$", content)
                self.assertIn("Analyse du pire cas : Arbre 3-régulier de profondeur $59$", content)
                self.assertNotIn("Analyse du pire cas : Arbre 3-régulier de profondeur $60$", content)

                # Verify pdflatex was called
                mock_run.assert_called_once()

    def test_pdf_output_exists_and_valid(self):
        # Assert the PDF was created
        pdf_path = "inprogress/04-Erdos-Gyarfas/04-Erdos-Gyarfas-Proof.pdf"
        self.assertTrue(os.path.exists(pdf_path), "PDF file was not generated.")

        # Verify page count
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            num_pages = len(reader.pages)
            self.assertTrue(10 <= num_pages <= 150, f"Page count is {num_pages}, expected between 10 and 150.")

if __name__ == '__main__':
    unittest.main()
