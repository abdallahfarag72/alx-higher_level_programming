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

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student instance"""
        if attrs is None:
            return self.__dict__
        json_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                json_dict[attr] = self.__dict__[attr]
        return json_dict
