#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    li = a_dictionary.keys()
    for i in li:
        new[i] *= 2
    return (new)
