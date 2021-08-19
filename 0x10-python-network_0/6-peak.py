#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """Find highest value in a list of unsorted integers"""

    int_list = list_of_integers

    if int_list:
        int_list.sort()
        return int_list[-1]
    else:
        return None
