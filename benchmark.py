import timeit
from utils import load_module

module = load_module("generate_proof", "inprogress/16-Erdos-Turan-Additive/generate_proof.py")

# We can benchmark the entire function or extract the logic
# To make it more measurable, let's time generate_latex
print(timeit.timeit("module.generate_latex()", globals=globals(), number=100))
