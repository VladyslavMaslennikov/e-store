"""
Sample tests
"""
from django.test import SimpleTestCase
import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)



    def test_subtract_numbers(self):
        res = calc.subtract(10, 2)
        self.assertEqual(res, 3)