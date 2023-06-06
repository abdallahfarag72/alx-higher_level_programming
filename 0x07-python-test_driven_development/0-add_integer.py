#!/usr/bin/python3

"""
Defines a function add_integer
that adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): First int.
        b (int): Second int. Defaults to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
