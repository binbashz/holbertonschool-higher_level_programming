#!/usr/bin/python3

import unittest
from max_integer import max_integer


class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 3, 2, 5, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -2, -5, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-1, 3, -2, 5, 0])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        result = max_integer([2, 4, 6, 4, 2])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
