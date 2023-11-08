#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    num = 0
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(0, len(roman_string)):
        if i <= (len(roman_string) - 2) and roman_dic[roman_string[i]] == 1 and roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]:
            num = num - roman_dic[roman_string[i]]
        else:
            num = num + roman_dic[roman_string[i]]
    return num
