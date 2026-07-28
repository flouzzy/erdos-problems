import sys
import pytest
from utils import load_module

def test_load_module_success():
    dummy_code = """
def hello():
    return 'world'

VAR = 42
"""
    dummy_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dummy_success_temp.py")
    with open(dummy_file, "w") as f:
        f.write(dummy_code)

    try:
        module_name = "dummy_module_test"
        module = load_module(module_name, dummy_file)

        assert module is not None
        assert module.hello() == 'world'
        assert module.VAR == 42
        assert module_name in sys.modules
        assert sys.modules[module_name] is module
    finally:
        if os.path.exists(dummy_file):
            os.remove(dummy_file)

def test_load_module_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_module("not_exist", os.path.join(os.path.abspath(os.path.dirname(__file__)), "path_that_does_not_exist.py"))

def test_load_module_invalid_syntax():
    dummy_code = """
def hello(
    return 'world'
"""
    dummy_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "dummy_invalid_temp.py")
    with open(dummy_file, "w") as f:
        f.write(dummy_code)

    try:
        with pytest.raises(SyntaxError):
            load_module("invalid_module", dummy_file)
    finally:
        if os.path.exists(dummy_file):
            os.remove(dummy_file)

if __name__ == '__main__':
    pytest.main(["-v", __file__])
