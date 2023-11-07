#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """pascal's triangle representation"""
    if n <= 0:
        return []

    number_tri = [[1]]
    while len(number_tri) != n:
        tri = number_tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        number_tri.append(tmp)
    return number_tri
