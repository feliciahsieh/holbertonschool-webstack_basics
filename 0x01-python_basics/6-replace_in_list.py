#!/usr/bin/python3
""" 6-replace_in_list.py - replace element in list
"""


def replace_in_list(my_list, idx, element):
    """
    replace_in_list() - replace element in list
    Arguments:
    my_list: source list
    idx: index as integer
    element: new element to replace in my_list
    Returns: list with designated element replaced
    """
    if type(element) is not int:
        return my_list

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    my_list[idx] = element
    return my_list
