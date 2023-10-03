#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = number % 10
if (number < 0):
    st = -st
string = "Last digit of " + str(number) + " is " + str(st)
if (st > 5):
    string += " and is greater than 5"
elif (st < 6 and st != 0):
    string += " and is less than 6 and not 0"
else:
    string += " and is 0"
print(string)
