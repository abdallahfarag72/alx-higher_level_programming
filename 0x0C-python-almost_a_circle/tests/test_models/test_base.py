#!/usr/bin/python3
"""Unit tests for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_id_assignment(self):
        """Test id assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)
        self.assertCountEqual(
            json_string, '[{"x": 2, \
            "width": 10, "id": 1, "height": 7, "y": 8}]')

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(type(obj_list), list)
        self.assertEqual(len(obj_list), 1)
        self.assertEqual(obj_list[0]['x'], 2)
        self.assertEqual(obj_list[0]['width'], 10)
        self.assertEqual(obj_list[0]['id'], 1)
        self.assertEqual(obj_list[0]['height'], 7)
        self.assertEqual(obj_list[0]['y'], 8)

    def test_create_rectangle(self):
        """Test create method for Rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(type(r2), Rectangle)
        self.assertEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Test create method for Square"""
        s1 = Square(5)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(type(s2), Square)
        self.assertEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_save_to_file_rectangle(self):
        """Test save_to_file method for Rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertCountEqual(content, '[{"x": 2, "width": 10, \
            "id": 1, "height": 7, "y": 8}, \
{"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]')

    def test_save_to_file_square(self):
        """Test save_to_file method for Square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as file:
            content = file.read()
            self.assertCountEqual(content, '[{"id": 5, \
            "size": 5, "x": 0, "y": 0}, \
{"id": 7, "size": 7, "x": 9, "y": 1}]')

    def test_load_from_file_rectangle(self):
        """Test load_from_file method for Rectangle"""
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        rectangles = Rectangle.load_from_file()
        self.assertEqual(type(rectangles), list)
        self.assertEqual(len(rectangles), 0)
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(type(rectangles), list)
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0], r1)
        self.assertEqual(rectangles[1], r2)

    def test_load_from_file_square(self):
        """Test load_from_file method for Square"""
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        squares = Square.load_from_file()
        self.assertEqual(type(squares), list)
        self.assertEqual(len(squares), 0)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        squares = Square.load_from_file()
        self.assertEqual(type(squares), list)
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0], s1)
        self.assertEqual(squares[1], s2)


if __name__ == "__main__":
    unittest.main()
