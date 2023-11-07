#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after specific string in a file"""
    text = ""
    with open(filename) as rf:
        for i in rf:
            text += i
            if search_string in i:
                text += new_string
    with open(filename, "w") as wf:
        wf.write(text)
