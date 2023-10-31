#!/usr/bin/python3
"""implementation of constructor and setters and getters"""


class Rectangle:
    """class of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

     @classmethod
    def square(cls, size=0):
        """new rectangel instance that is a square"""
        return cls(size, size)

     @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle"""
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (type(rect_2) != Rectangle_:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    def __init__(self, width=0, height=0):
        """constructor of the recatngle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """prints a string at deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
            rect_str += "\n".join(str(self.print_symbol) * self.__width for j in range(self.__height))
        return rect_str

    def __repr__(self):
        """string representation of rectangle (reproduction)"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
