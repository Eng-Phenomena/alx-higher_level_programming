#!/usr/bin/python3
"""write function"""


def write_file(filename="", text=""):
    """writing function"""
    with open(filename, "w", encoding="utf-8") as wf:
        return wf.write(text)
