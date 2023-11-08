#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    num = 0
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(0, len(roman_string)):
        if i > 0 and r[roman_string[i]] > r[roman_string[i - 1]]:
            num = num + r[roman_string[i]] - 2 * r[roman_string[i - 1]]
        else:
            num = num + r[roman_string[i]]
    return num
