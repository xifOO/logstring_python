import unittest
import sys
import time

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):

    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_of_large_number(self):
        with self.assertRaises(ValueError):
            factorial(10**6)

    def test_factorial_of_large_number_no_error(self):
        self.assertIsNotNone(factorial(1000))


if __name__ == '__main__':
    start_time = time.time()
    unittest.main()
    end_time = time.time()
    print("Время выполнения тестов:", end_time - start_time, "секунд")
