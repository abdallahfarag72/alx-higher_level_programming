#!/usr/bin/python3

"""
Defines a function print_square
that prints a square with the character #.
"""


def print_square(size):
    """
    prints a square with the character #.

    Args:
        size (int): size of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
