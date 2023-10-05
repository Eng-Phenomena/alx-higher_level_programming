#!/usr/bin/python3
if __name__ == "__main__":
    """printing the system args"""
    import sys

    count = len(sys.argv) - 1
    if (count == 0):
        print("{} arguments.".format(count))
    else:
        print("{} arguments:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))
