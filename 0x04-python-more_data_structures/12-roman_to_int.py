#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    num = 0
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(0, len(roman_string)):
        if i <= (len(roman_string) - 2) and r[roman_string[i]] == 1:
            if r[roman_string[i]] < r[roman_string[i + 1]]:
                num = num - r[roman_string[i]]
            else:
                num = num + r[roman_string[i]]
        else:
            num = num + r[roman_string[i]]
    return num
