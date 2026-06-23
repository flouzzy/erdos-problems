import time

def solve_es(n):
    for x in range(n // 4 + 1, n + 1):
        A = 4 * x - n
        if A <= 0: continue
        B = n * x
        B2 = B * B
        # We want A/B = 1/y + 1/z
        # (Ay - B)(Az - B) = B^2
        # D is a divisor of B^2. D = Ay - B => Ay = B + D => y = (B+D)/A
        # We only need to check D up to B.
        for D in range(1, B + 1):
            if B2 % D == 0:
                if (B + D) % A == 0:
                    y = (B + D) // A
                    D2 = B2 // D
                    if (B + D2) % A == 0:
                        z = (B + D2) // A
                        if x != y and y != z and x != z:
                            return x, y, z

    # If distinct not found, allow non-distinct
    for x in range(n // 4 + 1, n + 1):
        A = 4 * x - n
        if A <= 0: continue
        B = n * x
        B2 = B * B
        for D in range(1, B + 1):
            if B2 % D == 0:
                if (B + D) % A == 0:
                    y = (B + D) // A
                    D2 = B2 // D
                    if (B + D2) % A == 0:
                        z = (B + D2) // A
                        return x, y, z
    return None

t0 = time.time()
for n in range(2, 500):
    if solve_es(n) is None:
        print(f"Failed for {n}")
print(f"Time: {time.time() - t0}")
