import math
import pytest
import functools

@functools.lru_cache(maxsize=None)
def get_prime_factors(num):

    factors = {}

    count2 = 0
    while num % 2 == 0:
        count2 += 1
        num //= 2
    if count2 > 0:
        factors[2] = count2

    d = 3
    while d * d <= num:
        if num % d == 0:
            count = 0
            while num % d == 0:
                count += 1
                num //= d
            factors[d] = count
        d += 2
    if num > 1:
        factors[num] = 1

    return factors

def _find_solution(n, require_distinct):
    n_factors = get_prime_factors(n)
    n2_factors = {p: count * 2 for p, count in n_factors.items()}
    for x in range(n // 4 + 1, n + 1):
        A = 4 * x - n
        if A <= 0: continue
        B = n * x

        b2_factors = n2_factors.copy()
        for p, count in get_prime_factors(x).items():
            if p in b2_factors:
                b2_factors[p] += count * 2
            else:
                b2_factors[p] = count * 2

        limit = B

        divisors = [1]
        for p, exp in b2_factors.items():
            new_divs = []
            power = p
            for _ in range(exp):
                for d in divisors:
                    val = d * power
                    if val <= limit:
                        new_divs.append(val)
                power *= p
            divisors.extend(new_divs)

        divisors.sort()
        B2 = B * B

        for D in divisors:
            if (B + D) % A == 0:
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
