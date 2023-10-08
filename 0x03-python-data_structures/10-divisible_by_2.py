#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cases = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            cases.append(True)
        else:
            cases.append(False)
    return (cases)
