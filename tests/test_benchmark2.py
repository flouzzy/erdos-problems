import unittest
import sys
from unittest.mock import patch
from io import StringIO

class TestBenchmark2(unittest.TestCase):
    def test_benchmark2_runs(self):
        with patch("timeit.timeit", return_value=1.23) as mock_timeit:
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                if "benchmark2" in sys.modules:
                    del sys.modules["benchmark2"]
                import benchmark2

                output = mock_stdout.getvalue()
                self.assertIn("Old: 1.23", output)
                self.assertIn("New: 1.23", output)
                self.assertEqual(mock_timeit.call_count, 2)

    def test_benchmark2_logic(self):
        with patch("timeit.timeit", return_value=1.23):
            with patch("sys.stdout", new_callable=StringIO):
                if "benchmark2" not in sys.modules:
                    import benchmark2

                # Execute setup
                setup_globals = {}
                exec(sys.modules["benchmark2"].setup, setup_globals)

                # Execute stmt_old
                old_globals = setup_globals.copy()
                exec(sys.modules["benchmark2"].stmt_old, old_globals)

                # Execute stmt_new
                new_globals = setup_globals.copy()
                exec(sys.modules["benchmark2"].stmt_new, new_globals)

                # Assert they produce the same result
                self.assertEqual(old_globals["tex"], new_globals["tex"])

if __name__ == '__main__':
    unittest.main()
