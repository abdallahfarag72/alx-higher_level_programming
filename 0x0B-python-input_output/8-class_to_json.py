#!/usr/bin/python3

"""
Defines a function
"""


def class_to_json(obj):
    """Converts an object to a dictionary with simple
    data structures for JSON serialization"""
    if hasattr(obj, "__dict__"):
        attributes = obj.__dict__
        json_dict = {}
        for key, value in attributes.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
        return json_dict
    return obj
