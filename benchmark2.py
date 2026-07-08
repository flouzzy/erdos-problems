import timeit

setup = """
tex_start = "A" * 10000
"""

stmt_old = """
tex = tex_start
for n in range(1, 10):
    tex += "some string with number " + str(n) + " and some more text\\n" * 10
"""

stmt_new = """
tex = tex_start
parts = []
for n in range(1, 10):
    parts.append("some string with number " + str(n) + " and some more text\\n" * 10)
tex += "".join(parts)
"""

print("Old:", timeit.timeit(stmt_old, setup=setup, number=100000))
print("New:", timeit.timeit(stmt_new, setup=setup, number=100000))
