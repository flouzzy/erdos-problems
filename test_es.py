import math
import pytest

def _find_solution(n, require_distinct):
    for x in range(n // 4 + 1, n + 1):
        A = 4 * x - n
        if A <= 0: continue
        B = n * x
        B2 = B * B
        # We want A/B = 1/y + 1/z
        # (Ay - B)(Az - B) = B^2
        # D is a divisor of B^2. D = Ay - B => Ay = B + D => y = (B+D)/A
        # We only need to check D up to math.isqrt(B2).
        # We also know (B + D) % A == 0, which means D % A == (-B) % A.
        start_D = (-B) % A
        if start_D == 0:
            start_D = A

        limit = math.isqrt(B2)

        for D in range(start_D, limit + 1, A):
            if B2 % D == 0:
                y = (B + D) // A
                D2 = B2 // D
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

@pytest.mark.parametrize("n", range(2, 500))
def test_solve_es(n):
    result = solve_es(n)
    assert result is not None, f"solve_es failed for n={n}"
    x, y, z = result

    # 4/n = 1/x + 1/y + 1/z  =>  4 * x * y * z = n * (y * z + x * z + x * y)
    lhs = 4 * x * y * z
    rhs = n * (y * z + x * z + x * y)
    assert lhs == rhs, f"Mathematical property not met for n={n}, x={x}, y={y}, z={z}"

if __name__ == '__main__':
    pytest.main(["-v", __file__])
