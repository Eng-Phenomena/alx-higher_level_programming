#!/usr/bin/python3
"""
script that sends a request to the URL and displays:
-> The body of the response if no errors are found
-> The error code when there is HTTP error.
"""
import requests
import sys


if __name__ == "__main__":
    if requests.get(sys.argv[1]).status_code >= 400:
        print("Error code: {}".format(requests.get(sys.argv[1]).status_code))
    else:
        print(requests.get(sys.argv[1]).text)
