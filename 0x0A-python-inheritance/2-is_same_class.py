#!/usr/bin/python3

"""
Defines a function
"""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class.

    Args:
        obj: An object to check.
        a_class: A class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise, False.
    """
    return type(obj) is a_class
