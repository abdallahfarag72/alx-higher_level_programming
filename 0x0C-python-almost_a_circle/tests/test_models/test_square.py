#!/usr/bin/python3
"""Unit tests for Square class"""
import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_creation(self):
        """Test instance creation"""
        s = Square(5)
        self.assertEqual(type(s), Square)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_validations(self):
        """Test attribute validations"""
        with self.assertRaises(ValueError):
            s = Square(0)
        with self.assertRaises(ValueError):
            s = Square(-5)
        with self.assertRaises(ValueError):
            s = Square(5, -2, 8)
        with self.assertRaises(ValueError):
            s = Square(5, 2, -8)

    def test_area(self):
        """Test area calculation"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test display method"""
        s = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch("sys.stdout",
             new=unittest.mock.StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str_representation(self):
        """Test __str__ method"""
        s = Square(5, 2, 8, 99)
        expected_output = "[Square] (99) 2/8 - 5"
        self.assertEqual(str(s), expected_output)

    def test_update_args(self):
        """Test update method with *args"""
        s = Square(5, 2, 8, 99)
        s.update(1, 7)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 8)
        self.assertEqual(s.id, 1)

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        s = Square(5, 2, 8, 99)
        s.update(x=1, y=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 99)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(5, 2, 8, 99)
        expected_dict = {'x': 2, 'size': 5, 'id': 99, 'y': 8}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
