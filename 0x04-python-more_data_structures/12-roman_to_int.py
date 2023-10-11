#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    tmp1 = roman[roman_string[0]] 
    for i in range(len(roman_string)):
        tmp2 = roman[roman_string[i]]
        if (tmp2 <= tmp1):
            suma += roman[roman_string[i]]
        else:
            suma = roman[roman_string[i]] - suma
    return (suma)
