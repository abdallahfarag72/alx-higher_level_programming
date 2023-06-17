#!/usr/bin/python3

"""
Defines a function
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string"""
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
