import timeit
import sys
import importlib.util

def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

module = load_module("generate_proof", "inprogress/16-Erdos-Turan-Additive/generate_proof.py")

# We can benchmark the entire function or extract the logic
# To make it more measurable, let's time generate_latex
print(timeit.timeit("module.generate_latex()", globals=globals(), number=100))
