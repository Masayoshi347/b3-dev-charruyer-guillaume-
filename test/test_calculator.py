import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        result = calculator("2", "+", "3")
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = calculator("5", "-", "2")
        self.assertEqual(result, 3)

    def test_multiplication(self):
        result = calculator("4", "*", "5")
        self.assertEqual(result, 20)

    def test_division(self):
        result = calculator("9", "/", "3")
        self.assertEqual(result, 3)

    def test_invalid_operation(self):
        result = calculator("7", "invalid_operation", "4")
        self.assertEqual(result, "Opération non valide. Veuillez recommencer.")

if __name__ == '__main__':
    unittest.main()
