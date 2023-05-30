#!/usr/bin/python3

""" Defines a Square class """


class Square:
    """
    This is a class that represents a square.

    Attributes:
        __size (num): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. defaults to 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
