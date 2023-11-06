#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """exception not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating the input as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
