import timeit
import sys
import os

sys.path.insert(0, os.path.abspath("inprogress/16-Erdos-Turan-Additive"))
import generate_proof as module

# We can benchmark the entire function or extract the logic
# To make it more measurable, let's time generate_latex
print(timeit.timeit("module.generate_latex()", globals=globals(), number=100))
