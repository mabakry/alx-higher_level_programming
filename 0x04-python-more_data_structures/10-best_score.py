#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == biggest:
            return key
    return None
