#!/usr/bin/python3

"""
Defines a function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
