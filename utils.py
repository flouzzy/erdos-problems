import sys
import os
import importlib.util

def load_module(name, path):
    # Security: prevent loading arbitrary files (Directory Traversal / LFI)
    base_dir = os.path.realpath(os.path.dirname(__file__))
    abs_path = os.path.realpath(path)
    if os.path.commonpath([base_dir, abs_path]) != base_dir:
        raise ValueError(f"Untrusted module path: {path}")

    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
