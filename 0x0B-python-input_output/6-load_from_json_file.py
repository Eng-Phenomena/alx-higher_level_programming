#!/usr/bin/python3
"""json reading file function"""
import json


def load_form_json_file(fileame):
    """python object form json"""
    with open(filename) as rf:
        return json.load(rf)
