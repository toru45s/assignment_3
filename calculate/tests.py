from django.test import TestCase
from utility import Calculator

# Create your tests here.
class CalculatorTest(TestCase):
    def test_calculate_step1(self):
        result = Calculator.calculate(1, 2, 3)
        self.assertEqual(result['step1'], 3)

    def test_calculate_step2(self):
        result = Calculator.calculate(1, 2, 3)
        self.assertEqual(result['step2'], 0)

    def test_calculate_step3(self):
        result = Calculator.calculate(1, 2, 3)
        self.assertEqual(result['step3'], 0)

    def test_calculate_step4(self):
        result = Calculator.calculate(1, 2, 3)
        self.assertEqual(result['step4'], 0)

    def test_calculate_step5(self):
        result = Calculator.calculate(1, 2, 3)
        self.assertEqual(result['step5'], 0)