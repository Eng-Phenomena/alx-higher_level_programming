#!/usr/bin/python3
"""class of ordered list"""


class MyList(list):
    """my ordered list"""

    def print_sorted(self):
        print(sorted(self))
