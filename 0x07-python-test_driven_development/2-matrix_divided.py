#!/usr/bin/python3
""" matrix division by ahmed hossam """


def matrix_divided(matrix, div):
    """matrix divsion test cases"""

    if ((not isinstance(div, int)) and (not isinstance(div, float))):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new = []
    row = []
    fin = len(matrix[0])

    for i in range(0, len(matrix)):
        ts = len(matrix[i])
        if (fin != ts):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            fin = ts
        for j in range(0, len(matrix[i])):
            if ((not isinstance(matrix[i][j], int)) and (not isinstance(matrix[i][j], float))):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                row.append(round(matrix[i][j] / 3, 2))
        new.append(row)
        row = []
    return new
