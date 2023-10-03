#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = str(number)[-1]
string = "Last digit of " + str(number) + " is " + st
if (int(st) > 5):
    string += " and is greater than 5"
elif (int(st) < 6 and int(st) != 0):
    string += " and is less than 6 and not 0"
else:
    string += " and is 0"
print(string)
