import unittest

from week01.baseline_loops import sum_linear, sum_formula
from week01.recursion_iter import factorial_iter, factorial_rec, fib_iter


class TestWeek01(unittest.TestCase):
    def test_sum(self):
        for n in [0, 1, 10, 1000]:
            self.assertEqual(sum_linear(n), sum_formula(n))

    def test_factorial(self):
        for n in [0, 1, 5, 8]:
            self.assertEqual(factorial_iter(n), factorial_rec(n))

    def test_fib(self):
        self.assertEqual(fib_iter(0), 0)
        self.assertEqual(fib_iter(1), 1)
        self.assertEqual(fib_iter(10), 55)


if __name__ == "__main__":
    unittest.main()
