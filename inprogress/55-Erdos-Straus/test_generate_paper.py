import unittest
from unittest.mock import patch, mock_open
import generate_paper

class TestGeneratePaper(unittest.TestCase):
    def test_find_solution(self):
        # Known base case: n=4 -> x=2, y=3, z=6
        sol = generate_paper.find_solution(4)
        self.assertEqual(sol, (2, 3, 6))

        # Check correctness for a prime case n=5
        sol = generate_paper.find_solution(5)
        # We don't assert the exact tuple, just that it returns a valid solution
        self.assertIsNotNone(sol)
        x, y, z = sol
        from fractions import Fraction
        self.assertEqual(Fraction(4, 5), Fraction(1, x) + Fraction(1, y) + Fraction(1, z))

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_paper_io(self, mock_file):
        generate_paper.generate_paper()
        mock_file.assert_called_once()
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)

        # Check required French content and structural sections
        self.assertIn(r"\section{Analyse et Décomposition Axiomatique}", written_content)
        self.assertIn(r"\section{Littérature Contextuelle}", written_content)
        self.assertIn(r"\section{Architecture d'Autoformalisation (Lean 4)}", written_content)
        self.assertIn(r"\end{document}", written_content)

if __name__ == '__main__':
    unittest.main()
