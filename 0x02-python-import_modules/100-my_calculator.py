#!/usr/bin/python3
if __name__ == "__main__":
    """my calculator"""
    from calculator_1 import add, sub, mul, div
    import sys

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if (op == "+"):
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif (op == "-"):
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif (op == "*"):
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif (op == "/"):
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")