#!/usr/bin/python3
for i in range(100):
    if (i == 89):
        print("{}".format(i))
    elif (i // 10 < i % 10):
        print("{:02}".format(i), end=", ")
