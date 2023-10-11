#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ex = sorted(a_dictionary)
    for i in range(len(ex)):
        print("{}: {}".format(ex[i], a_dictionary[ex[i]]))
