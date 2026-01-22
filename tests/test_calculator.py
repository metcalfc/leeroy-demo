"""
Unit tests for calculator module.
"""

import math
import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import add, subtract, multiply, divide, power, modulo, sqrt, log, sin, cos, tan

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(8, 4), 0)
        self.assertEqual(modulo(7, 2), 1)
        self.assertEqual(modulo(-10, 3), 2)
        with self.assertRaises(ValueError):
            modulo(5, 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=5)
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_log(self):
        self.assertAlmostEqual(log(math.e), 1, places=5)
        self.assertAlmostEqual(log(1), 0, places=5)
        self.assertAlmostEqual(log(100, 10), 2, places=5)
        self.assertAlmostEqual(log(8, 2), 3, places=5)
        with self.assertRaises(ValueError):
            log(0)
        with self.assertRaises(ValueError):
            log(-1)
        with self.assertRaises(ValueError):
            log(10, 1)
        with self.assertRaises(ValueError):
            log(10, -2)

    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0, places=5)
        self.assertAlmostEqual(sin(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(sin(math.pi), 0, places=5)
        self.assertAlmostEqual(sin(math.pi / 6), 0.5, places=5)

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1, places=5)
        self.assertAlmostEqual(cos(math.pi / 2), 0, places=5)
        self.assertAlmostEqual(cos(math.pi), -1, places=5)
        self.assertAlmostEqual(cos(math.pi / 3), 0.5, places=5)

    def test_tan(self):
        self.assertAlmostEqual(tan(0), 0, places=5)
        self.assertAlmostEqual(tan(math.pi / 4), 1, places=5)
        self.assertAlmostEqual(tan(math.pi), 0, places=5)
        self.assertAlmostEqual(tan(-math.pi / 4), -1, places=5)

if __name__ == '__main__':
    unittest.main()
