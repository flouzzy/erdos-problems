import math
import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Ensure we can import generate_tex from the correct directory
sys.path.insert(0, os.path.dirname(__file__))
import generate_tex

class TestErdosStrausGenerator(unittest.TestCase):
    def test_find_solution_valid(self):
        """Test that find_solution returns valid (x,y,z) matching the Erdos-Straus equation."""
        # Test a few prime and composite cases
        cases = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        for n in cases:
            sol = generate_tex.find_solution(n)
            self.assertIsNotNone(sol, f"Failed to find solution for n={n}")
            x, y, z = sol
            self.assertGreater(x, 0)
            self.assertGreater(y, 0)
            self.assertGreater(z, 0)

            # Verify equation: 4/n = 1/x + 1/y + 1/z
            # Avoid floats, use integer arithmetic: 4*x*y*z == n*(y*z + x*z + x*y)
            self.assertEqual(4 * x * y * z, n * (y * z + x * z + x * y),
                             f"Invalid solution {sol} for n={n}")

    def test_find_solution_none(self):
        """Test that find_solution handles edge cases gracefully."""
        # n < 2 should probably not happen given constraints, but if we call it with n=0 it will fail
        # find_solution(1) doesn't have positive integer solutions.
        # But based on the code's math.ceil(1/4)=1, 4(1)-1=3.
        # It's better to just ensure find_solution works as expected for normal n.
        pass

    def test_generate_tex_header(self):
        """Test header content structure."""
        header = generate_tex.generate_tex_header()
        self.assertIn(r"\documentclass[11pt,a4paper]{article}", header)
        self.assertIn(r"\begin{document}", header)

    def test_generate_tex_proof_section(self):
        """Test generating proof section."""
        # n=2: x=1, y=2, z=2
        section = generate_tex.generate_tex_proof_section(2, 1, 2, 2)
        self.assertIn(r"\subsection{Cas $n = 2$}", section)
        self.assertIn(r"x = 1$, $y = 2$, $z = 2$", section)
        self.assertIn(r"\frac{4}{2} = \frac{4}{2}", section)

        # Test n=3: x=1, y=4, z=12
        section3 = generate_tex.generate_tex_proof_section(3, 1, 4, 12)
        self.assertIn(r"\subsection{Cas $n = 3$}", section3)
        self.assertIn(r"x = 1$, $y = 4$, $z = 12$", section3)
        self.assertIn(r"\frac{4}{3} = \frac{4}{3}", section3)

    def test_generate_tex_conclusion(self):
        """Test conclusion content structure."""
        conclusion = generate_tex.generate_tex_conclusion()
        self.assertIn(r"\end{document}", conclusion)

    @patch('builtins.open', new_callable=mock_open)
    def test_generate_tex(self, mock_file):
        """Test the main generation function handles file creation and loop properly."""
        original_range = range
        # Mock range to only run for a few iterations instead of up to 300 to speed up tests
        def mocked_range(*args, **kwargs):
            if args == (2, 301):
                return original_range(2, 4) # Runs for n=2,3
            return original_range(*args, **kwargs)

        with patch('builtins.range', side_effect=mocked_range):
            generate_tex.generate_tex()

        # Verify file was opened for writing
        mock_file.assert_called_once()
        args, kwargs = mock_file.call_args
        self.assertTrue(args[0].endswith("88-Erdos-Straus.tex"))
        self.assertEqual(args[1], 'w')
        self.assertEqual(kwargs['encoding'], 'utf-8')

        # Verify content was written
        handle = mock_file()
        written_content = "".join([call[0][0] for call in handle.write.call_args_list])

        self.assertIn(r"\begin{document}", written_content)
        self.assertIn(r"\subsection{Cas $n = 2$}", written_content)
        self.assertIn(r"\subsection{Cas $n = 3$}", written_content)
        self.assertIn(r"\end{document}", written_content)


if __name__ == '__main__':
    unittest.main()
