import unittest

from calculator import calculator


class TestCalculator(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculator(2, 3, "+"), 5)

	def test_subtraction(self):
		self.assertEqual(calculator(10, 4, "-"), 6)

	def test_multiplication(self):
		self.assertEqual(calculator(6, 7, "*"), 42)

	def test_division(self):
		self.assertEqual(calculator(8, 2, "/"), 4)

	def test_division_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			calculator(8, 0, "/")

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator(5, 5, "%")


if __name__ == "__main__":
	unittest.main()
