#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    li = a_dictionary.keys()
    best = None
    Max = 0
    for i in li:
        if (a_dictionary[i] > Max):
            Max = a_dictionary[i]
            best = i
    return (best)
