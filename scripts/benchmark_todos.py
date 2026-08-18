import timeit

setup = """
import os
dirs = [f'dir_{i}' for i in range(1000)] + ['.git', '.lake']
"""

test_tuple = """
[d for d in dirs if d not in ('.git', '.lake')]
"""

test_set = """
[d for d in dirs if d not in {'.git', '.lake'}]
"""

time_tuple = timeit.timeit(test_tuple, setup=setup, number=10000)
time_set = timeit.timeit(test_set, setup=setup, number=10000)

print(f"Tuple baseline: {time_tuple:.5f} seconds")
print(f"Set optimization: {time_set:.5f} seconds")
print(f"Improvement: {(time_tuple - time_set) / time_tuple * 100:.2f}%")
