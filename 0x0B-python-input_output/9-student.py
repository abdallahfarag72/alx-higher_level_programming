#!/usr/bin/python3

"""
Defines a class
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance"""
        attributes = self.__dict__
        json_dict = {}
        for key, value in attributes.items():
            if isinstance(value, (str, int)):
                json_dict[key] = value
        return json_dict
