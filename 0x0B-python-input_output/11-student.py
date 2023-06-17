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
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)
        return json_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student
        instance with values from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
