#!/usr/bin/python3

def text_indentation(text):
    if (type(text) is not str):
        raise TypeError("text must be a string")

    for i in text:
        if text == " ":
            continue
        else:
            if (i == "?" or i == "." or i == ":"):
                print(i)
                print("")
            else:
                print(i, end="")
