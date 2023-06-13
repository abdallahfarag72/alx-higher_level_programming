#!/usr/bin/python3

"""
Defines a class
"""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Raises an exception indicating that
        the area() method is not implemented."""
        raise Exception("area() is not implemented")
