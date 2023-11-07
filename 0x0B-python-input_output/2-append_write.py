#!/usr/bin/python3
"""appending text file"""


def append_write(filename="", text=""):
    """appending text"""
    with open(filename, "a", encoding="utf-8") as af:
        return af.write(text)
