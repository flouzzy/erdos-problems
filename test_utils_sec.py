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


    def test_load_module_symlink_bypass(self):
        # Create a malicious file outside base_dir
        tf = tempfile.NamedTemporaryFile(suffix=".py", delete=False)
        tf.write(b"z = 'malicious'\n")
        tf.close()
        malicious_path = tf.name

        # Create a symlink inside base_dir pointing to the malicious file
        symlink_path = os.path.join(self.base_dir, "symlink_module.py")
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
        os.symlink(malicious_path, symlink_path)

        try:
            with self.assertRaises(ValueError) as context:
                load_module("symlink_module", symlink_path)
            self.assertIn("Untrusted module path", str(context.exception))
        finally:
            if os.path.exists(symlink_path):
                os.remove(symlink_path)
            if os.path.exists(malicious_path):
                os.remove(malicious_path)


if __name__ == '__main__':
    unittest.main()
