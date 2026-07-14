import timeit
import sys
import os

sys.path.insert(0, os.path.abspath("inprogress/16-Erdos-Turan-Additive"))
import generate_proof as module

if __name__ == "__main__":
    n_runs = 500
    time = timeit.timeit("module.generate_latex()", globals=globals(), number=n_runs)
    print(f"Total time for {n_runs} runs: {time:.4f}s")
