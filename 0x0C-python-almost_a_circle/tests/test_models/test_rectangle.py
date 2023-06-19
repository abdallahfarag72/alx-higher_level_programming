#!/usr/bin/python3
"""Unit tests for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_creation(self):
        """Test instance creation"""
        r = Rectangle(10, 5)
        self.assertEqual(type(r), Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_validations(self):
        """Test attribute validations"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(10, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, -5)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, -2, 8)
        with self.assertRaises(ValueError):
            r = Rectangle(10, 5, 2, -8)

    def test_area(self):
        """Test area calculation"""
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """Test display method"""
        r = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        with unittest.mock.patch("sys.stdout",
             new=unittest.mock.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str_representation(self):
        """Test __str__ method"""
        r = Rectangle(10, 5, 2, 8, 99)
        expected_output = "[Rectangle] (99) 2/8 - 10/5"
        self.assertEqual(str(r), expected_output)

    def test_update_args(self):
        """Test update method with *args"""
        r = Rectangle(10, 5, 2, 8, 99)
        r.update(1, 20)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 8)
        self.assertEqual(r.id, 1)

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        r = Rectangle(10, 5, 2, 8, 99)
        r.update(x=1, height=7, y=2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 99)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r = Rectangle(10, 5, 2, 8, 99)
        expected_dict = {'x': 2, 'width': 10, 'id': 99, 'height': 5, 'y': 8}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
