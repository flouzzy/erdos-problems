import sys
import pytest
from utils import load_module

def test_load_module_success(tmp_path):
    dummy_code = """
def hello():
    return 'world'

VAR = 42
"""
    dummy_file = tmp_path / "dummy.py"
    dummy_file.write_text(dummy_code)

    module_name = "dummy_module_test"
    module = load_module(module_name, str(dummy_file))

    assert module is not None
    assert module.hello() == 'world'
    assert module.VAR == 42
    assert module_name in sys.modules
    assert sys.modules[module_name] is module

def test_load_module_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_module("not_exist", "/path/that/does/not/exist.py")

def test_load_module_invalid_syntax(tmp_path):
    dummy_code = """
def hello(
    return 'world'
"""
    dummy_file = tmp_path / "invalid.py"
    dummy_file.write_text(dummy_code)

    with pytest.raises(SyntaxError):
        load_module("invalid_module", str(dummy_file))

if __name__ == '__main__':
    pytest.main(["-v", __file__])
