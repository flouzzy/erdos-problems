import os
import sys
import unittest
from unittest.mock import patch, mock_open

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_tex

class TestGenerateProof(unittest.TestCase):
    def test_generate_tex(self):
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            generate_tex()

            # Verify open was called twice (for English and French files)
            self.assertEqual(mocked_file.call_count, 2)

            # Check the paths called
            calls = mocked_file.call_args_list
            self.assertEqual(calls[0][0][0], 'inprogress/33-Erdos-Unit-Distance/proof.tex')
            self.assertEqual(calls[1][0][0], 'inprogress/33-Erdos-Unit-Distance/proof.fr.tex')

            # Retrieve written content for English file
            handle_en = calls[0][1] if 'encoding' in calls[0][1] else calls[0] # Handle mock differences if any
            # It's easier to check the written strings across all writes on the mock

            written_content = []
            for call in mocked_file().write.call_args_list:
                written_content.append(call[0][0])

            full_content = "".join(written_content)

            # Verify English specific elements
            self.assertIn(r"\title{The Erdős Unit Distance Problem: Incidences and Algebraic Deconstruction}", full_content)
            self.assertIn(r"\noindent Charles EDOU NZE, chercheur indépendant", full_content)
            self.assertIn("def ErdosUnitDistanceConjecture : Prop :=", full_content)

            # Verify French specific elements
            self.assertIn(r"\title{Le Problème des Distances Unités d'Erdős : Incidences et Déconstruction Algébrique}", full_content)
            self.assertIn(r"\usepackage[french]{babel}", full_content)

if __name__ == '__main__':
    unittest.main()
