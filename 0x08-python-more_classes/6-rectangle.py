#!/usr/bin/python3
"""implementation of constructor and setters and getters"""


class Rectangle:
    """class of a rectangle"""

    count = 0

    def __init__(self, width=0, height=0):
        """constructor of the recatngle"""
        self.height = height
        self.width = width
        Rectangle.count += 1

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """perimeter of rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of rectangle"""
        rect_str = ""
        if self.__width != 0 and self.__height != 0:
            rect_str += "\n".join("#" * self.__width for j in range(self.__height))
        return rect_str

    def __repr__(self):
        """string representation of rectangle (reproduction)"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints a string at deletion"""
        print("Bye rectangle...")
        Rectangle.count -= 1
