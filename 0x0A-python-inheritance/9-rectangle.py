#!/usr/bin/python3
"""Rectangle class using BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the representation of a Rectangle."""
        str_1 = "[" + str(self.__class__.__name__) + "] "
        str_2 = str(self.__width) + "/" + str(self.__height)
        return str_1 + str_2
