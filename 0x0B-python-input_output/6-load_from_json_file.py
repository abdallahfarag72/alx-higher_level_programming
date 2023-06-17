#!/usr/bin/python3

"""
Defines a function
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
