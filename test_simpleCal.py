__author__ = 'Dreyke Boone'

import unittest
from simpleCal import Calculator

num1 = 10
num2 = 50
failure = "incorrect value"

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_answer_init(self):
        value = self.calc.answer
        self.assertEqual(value, 0.0, failure)

    def test_addition(self):
        value = self.calc.addition(num1, num2)
        self.assertEqual(value, 60, failure)
        self.assertEqual(value, self.calc.answer, failure)

    def test_subtraction(self):
        value = self.calc.subtraction(num1, num2)
        self.assertEqual(value, -40, failure)
        self.assertEqual(value, self.calc.answer, failure)

    def test_multiplication(self):
        value = self.calc.multiplication(num1, num2)
        self.assertEqual(value, 500, failure)
        self.assertEqual(value, self.calc.answer, failure)

    def test_division(self):
        value = self.calc.division(num1, num2)
        self.assertEqual(value, 0.2, failure)
        self.assertEqual(value, self.calc.answer, failure)

if __name__ == '__main__':
    unittest.main()