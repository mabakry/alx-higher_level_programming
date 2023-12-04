#!/usr/bin/python3
""" MYlist Module """


class MyList(list):
    """  prints the list, but sorted (ascending sort)"""
    pass

    def print_sorted(self):
        """  prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
