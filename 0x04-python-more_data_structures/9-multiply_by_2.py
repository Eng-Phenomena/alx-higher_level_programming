#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    li = a_dictionary.keys()
    for i in li:
        a_dictionary[i] *= 2
    return (a_dictionary)
