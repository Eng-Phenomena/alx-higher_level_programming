#!/usr/bin/python3
# 4-square.py done by ahmed hossam
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

    def __init__(self, size=0, position=(0, 0)):
        """overloading of contstrcutors"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        case = type(position[0]) != int or type(position[1]) != int
        case2 = position[0] < 0 or position[1] < 0
        if (case or case2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """get size value"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size value"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method to claculate area"""
        return (self.__size ** 2)

    def my_print(self):
        """printing the square"""
        for bl in range(0, self.__position[1]):
            print("")
        i2 = self.__position[0]

        for i in range (0, self.__size):
            for j in range(0, self.__size + i2):
                if (j < i2):
                    print("_", end="")
                else:
                    print("#", end="")
            print("")

        if (self.__size == 0):
            print("")
