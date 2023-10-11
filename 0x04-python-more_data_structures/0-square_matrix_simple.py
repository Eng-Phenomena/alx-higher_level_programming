#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for k in range(len(matrix)):
        new.append(list(matrix[k].copy()))
    for i in range(len(new)):
        for j in range(len(new[i])):
            new[i][j] **= 2
    return (new)
