import unittest
import os
import sys
import tempfile
from unittest.mock import patch
from io import StringIO
import get_todos

class TestGetTodos(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for tests
        self.test_dir = tempfile.TemporaryDirectory()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir.name)

    def tearDown(self):
        # Restore original working directory and cleanup
        os.chdir(self.original_cwd)
        self.test_dir.cleanup()

    def create_file(self, filepath, content):
        # Create intermediate directories if they don't exist
        dirname = os.path.dirname(filepath)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    @patch('sys.stdout', new_callable=StringIO)
    def test_md_and_tex_files(self, mock_stdout):
        # Test .md and .tex files containing "sorry"
        self.create_file("test.md", "This is a Lean proof sketch\nsorry -- I will do this later\n")
        self.create_file("test.tex", "\\begin{lstlisting}[language=Caml]\nsorry\n\\end{lstlisting}\n")
        self.create_file("no_sorry.md", "This is a document without any unproven statements.\n")

        get_todos.main()

        output = mock_stdout.getvalue()

        self.assertIn("test.md:2: I will do this later", output)
        self.assertIn("test.tex:2: Not inferrable", output)
        self.assertNotIn("no_sorry.md", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_py_files(self, mock_stdout):
        # Test .py files containing "sorry" and exclusion logic
        py_content = """def my_func():
    # This is a python comment with sorry in it
    a = "sorry"
    print("sorry")
    x = "sorry but with line"
    y = "sorry description"
    z = "actually just sorry" -- A comment
"""
        self.create_file("test.py", py_content)
        get_todos.main()

        output = mock_stdout.getvalue()

        self.assertNotIn("test.py:2:", output) # Ignored due to #
        self.assertNotIn("test.py:4:", output) # Ignored due to print
        self.assertNotIn("test.py:5:", output) # Ignored due to line
        self.assertNotIn("test.py:6:", output) # Ignored due to description
        self.assertIn("test.py:7: A comment", output) # This one should be included

    @patch('sys.stdout', new_callable=StringIO)
    def test_ignore_directories(self, mock_stdout):
        # Test that .git and .lake directories are ignored
        self.create_file(".git/test.md", "sorry")
        self.create_file(".lake/test.tex", "sorry")
        self.create_file("normal_dir/test.md", "sorry -- Found this")

        get_todos.main()

        output = mock_stdout.getvalue()

        self.assertNotIn(".git", output)
        self.assertNotIn(".lake", output)
        self.assertIn("normal_dir/test.md:1: Found this", output)

if __name__ == '__main__':
    unittest.main()
