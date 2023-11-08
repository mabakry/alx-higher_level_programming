#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    y = 0
    for i in range(0, len(my_list)):
        x = x + my_list[i][0] * my_list[i][1]
        y = y + my_list[i][1]
    return (x / y)
