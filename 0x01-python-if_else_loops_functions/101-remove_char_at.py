#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for x in str:
        if (x == n):
            x += 1
        new[i] = str[x]
    return (new)
