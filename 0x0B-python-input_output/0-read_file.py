#!/usr/bin/python3
"""reading file function"""


def read_file(filename=""):
    """reading function"""
    with open(filename, encoding="utf-8") as rf:
        print(f.read(), end="")
