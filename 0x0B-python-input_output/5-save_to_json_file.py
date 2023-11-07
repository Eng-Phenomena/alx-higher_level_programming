#!/usr/bin/python3
"""json file writing function"""
import json


def save_to_json_file(my_obj, filename):
    """object to text file"""
    with open(filename, "w") as wf:
        json.dump(my_obj, wf)
