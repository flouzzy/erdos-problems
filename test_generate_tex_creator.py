import unittest
from generate_tex_creator import find_solution

class TestGenerateTexCreator(unittest.TestCase):
    def check_solution(self, n):
        sol = find_solution(n)
        self.assertIsNotNone(sol, f"No solution found for n={n}")
        x, y, z = sol
        self.assertGreater(x, 0, f"x={x} is not > 0 for n={n}")
        self.assertGreater(y, 0, f"y={y} is not > 0 for n={n}")
        self.assertGreater(z, 0, f"z={z} is not > 0 for n={n}")

        # Check equation 4/n = 1/x + 1/y + 1/z
        # Using cross multiplication to avoid float precision issues:
        # 4 * x * y * z = n * (y * z + x * z + x * y)
        left_side = 4 * x * y * z
        right_side = n * (y * z + x * z + x * y)
        self.assertEqual(left_side, right_side, f"Equation not satisfied for n={n}: 4/{n} != 1/{x} + 1/{y} + 1/{z}")

    def test_find_solution(self):
        # Happy paths
        for n in range(2, 10):
            self.check_solution(n)

    def test_edge_cases(self):
        # n = 1 might return None based on the math logic, let's see.
        # But conjecture is for n >= 2. Let's just test n=1 behavior if we want.
        # Actually n=1 with 4/1 = 1/x+1/y+1/z. 4 = 1/x+1/y+1/z. Max RHS is 3. Impossible for positive integers.
        # find_solution(1) should return None.
        self.assertIsNone(find_solution(1))

        # Test n <= 0
        self.assertIsNone(find_solution(0))
        self.assertIsNone(find_solution(-5))

if __name__ == '__main__':
    unittest.main()
