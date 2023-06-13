#!/usr/bin/python3

"""
Defines a class
"""


class MyList(list):
    """Subclass of list with additional method print_sorted"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
