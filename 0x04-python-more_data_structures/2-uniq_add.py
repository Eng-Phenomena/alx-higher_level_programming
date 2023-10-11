#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    suma = 0 
    for i in new:
        suma += i
    return (suma)
