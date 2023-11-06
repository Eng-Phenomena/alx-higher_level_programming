#!/usr/bin/python3
"""defining my own int class that inherts from the in class"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override ==  with !="""
        return self.real != value

    def __ne__(self, value):
        """override != withh =="""
        return self.real == value
