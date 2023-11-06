#!/usr/bin/python3
"""class that inherits from a class checker"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
