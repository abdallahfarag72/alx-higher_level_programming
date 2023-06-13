#!/usr/bin/python3

"""
Defines a class
"""


class MyInt(int):
    """
    MyInt class that inherits from int
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==)
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=)
        """
        return super().__eq__(other)
