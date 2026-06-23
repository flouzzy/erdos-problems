import time

def _find_solution(n, require_distinct):
    for x in range(n // 4 + 1, n + 1):
        A = 4 * x - n
        if A <= 0: continue
        B = n * x
        # We want A/B = 1/y + 1/z
        # (Ay - B)(Az - B) = B^2
        # D is a divisor of B^2. D = Ay - B => Ay = B + D => y = (B+D)/A
        # We only need to check D up to B.
        for D in range(1, B + 1):
            if (B * B) % D == 0:
                if (B + D) % A == 0:
                    y = (B + D) // A
                    D2 = (B * B) // D
                    if (B + D2) % A == 0:
                        z = (B + D2) // A
                        if not require_distinct or (x != y and y != z and x != z):
                            return x, y, z
    return None

def solve_es(n):
    res = _find_solution(n, True)
    if res is not None:
        return res
    # If distinct not found, allow non-distinct
    return _find_solution(n, False)

t0 = time.time()
for n in range(2, 500):
    if solve_es(n) is None:
        print(f"Failed for {n}")
print(f"Time: {time.time() - t0}")
