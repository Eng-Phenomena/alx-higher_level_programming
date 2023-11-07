#!/usr/bin/python3
"""class student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary represetatio of instance"""
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k:getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replacing all stributes of student"""
        for i, j in json.items():
            setattr(self, i, j)
