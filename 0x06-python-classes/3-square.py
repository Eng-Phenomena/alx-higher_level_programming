#!/usr/bin/python3
# 3-square.py done by ahmed hossam
"""class area method check"""


class Square:
    """area method"""
    def __init__(self, size=0):
        """constructor of class"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method to claculate area"""
        return (self.__size ** 2)
