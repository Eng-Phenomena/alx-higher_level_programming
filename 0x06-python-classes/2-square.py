#!/usr/bin/python3
# 2-square.py done by ahmed hossam
"""validiation check"""


class Square:
    """validate number"""
    def __init__(self, size=0):
        """constructor of class"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
