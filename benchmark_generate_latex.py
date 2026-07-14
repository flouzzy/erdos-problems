import timeit
from utils import load_module

module = load_module("generate_proof", "inprogress/16-Erdos-Turan-Additive/generate_proof.py")

if __name__ == "__main__":
    n_runs = 500
    time = timeit.timeit("module.generate_latex()", globals=globals(), number=n_runs)
    print(f"Total time for {n_runs} runs: {time:.4f}s")
