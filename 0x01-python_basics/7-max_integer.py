#!/usr/bin/python3
""" 7-max_integer.py - find max number in list
"""


def max_integer(my_list=[]):
    """
    max_integer() - find max number in list
    Arguments:
    my_list: source list to find max
    Returns: maximum value found in list
    """
    n = len(my_list)
    if n == 0:
        return None

    max = my_list[0]
    for i in range(1, n):
        if max < my_list[i]:
            max = my_list[i]
    return max
