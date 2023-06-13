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

    def integer_validator(self, name, value):
        """Validates that the given value is
        an integer greater than 0."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
