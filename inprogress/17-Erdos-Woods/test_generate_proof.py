import os
import sys
import unittest
from unittest.mock import patch, mock_open

# Append the directory containing the generator to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_proof import generate_latex

class TestGenerateProof(unittest.TestCase):
    @patch('subprocess.run')
    def test_generate_latex(self, mock_run):
        # Mock file operations to test generation without writing to disk
        with patch('builtins.open', new_callable=mock_open) as mocked_file:
            generate_latex()

            # Check if correct file path was used
            filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '17-proof.tex')
            mocked_file.assert_called_with(filepath, 'w', encoding='utf-8')

            # Ensure something was written
            handle = mocked_file()
            self.assertTrue(handle.write.called)

            # Retrieve all written content
            content = "".join(call.args[0] for call in handle.write.call_args_list)

            # Verify key sections
            self.assertIn(r"\title{Une Approche Analytique et Combinatoire de la Conjecture d'Erdős-Woods}", content)
            self.assertIn(r"erdos_woods_conjecture", content)
            self.assertIn(r"\end{document}", content)

if __name__ == '__main__':
    unittest.main()
