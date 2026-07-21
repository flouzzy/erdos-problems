import os
import sys
import tempfile
import unittest
from utils import load_module

class TestLoadModuleSecurity(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.abspath(os.path.dirname(__file__))
        self.valid_module_path = os.path.join(self.base_dir, "temp_valid_module.py")
        with open(self.valid_module_path, "w") as f:
            f.write("x = 42\n")

        self.tf = tempfile.NamedTemporaryFile(suffix=".py", delete=False)
        self.tf.write(b"y = 99\n")
        self.tf.close()
        self.invalid_module_path = self.tf.name

    def tearDown(self):
        if os.path.exists(self.valid_module_path):
            os.remove(self.valid_module_path)
        if os.path.exists(self.invalid_module_path):
            os.remove(self.invalid_module_path)

    def test_load_module_valid_path(self):
        mod = load_module("temp_valid_module", self.valid_module_path)
        self.assertEqual(mod.x, 42)

    def test_load_module_invalid_path(self):
        with self.assertRaises(ValueError) as context:
            load_module("temp_invalid_module", self.invalid_module_path)
        self.assertIn("Untrusted module path", str(context.exception))

if __name__ == '__main__':
    unittest.main()
