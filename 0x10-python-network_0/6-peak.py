#!/usr/bin/python3
"""Technical Interview problem [List of Numbers algorithim]."""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted ints."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return (list_of_integers[0])
