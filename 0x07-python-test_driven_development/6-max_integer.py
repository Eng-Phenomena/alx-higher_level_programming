#!/usr/bin/python3

def max_integer(list=[]):
    if len(list) == 0:
        return None
    tmp = list[0]
    i = 1
    while i < len(list):
        if list[i] > tmp:
            tmp = list[i]
        i += 1
    return (tmp)
