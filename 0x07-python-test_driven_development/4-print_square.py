#!/usr/bin/python3
""" TDD made by AHMED HOSSAM"""


def print_square(size):
    """function that prints square pattern"""

    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print(("#" * size + "\n"), end="")
