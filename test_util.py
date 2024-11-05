import unittest
from util import convert_temperature

class TestUtil(unittest.TestCase):
    def test_convert_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert_temperature(0, 'C'), 32)
        self.assertAlmostEqual(convert_temperature(100, 'C'), 212)
    
    def test_convert_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert_temperature(32, 'F'), 0)
        self.assertAlmostEqual(convert_temperature(212, 'F'), 100)
    
    def test_invalid_unit(self):
        with self.assertRaises(ValueError):
            convert_temperature(100, 'K')

if __name__ == '__main__':
    unittest.main()
