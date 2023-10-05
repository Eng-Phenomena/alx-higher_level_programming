#!/usr/bin/python3
if __name__ == "__main__":
    """sum of args"""
    import sys
    count = len(sys.argv)
    suma = 0
    for i in range(1, count):
        suma += int(sys.argv[i])
    print("{}".format(suma))
