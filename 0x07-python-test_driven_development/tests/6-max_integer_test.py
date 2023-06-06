#!/usr/bin/python3

"""
Defines a class TestMaxInteger
Unittest for max_integer([...])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This is a class that represents a Unittest for max_integer([...]).
    """

    def test_regular_list(self):
        """Test with a regular list of integers"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_unsorted_list(self):
        """Test with an unsorted list of integers"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        result = max_integer([-3, -7, -2, -9])
        self.assertEqual(result, -2)

    def test_duplicate_numbers(self):
        """Test with a list containing duplicate numbers"""
        result = max_integer([5, 5, 5, 5])
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
