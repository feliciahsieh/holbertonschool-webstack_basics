#!/usr/bin/python3
"""103-new_in_list.py - replace list element without modifying original list
"""


def new_in_list(my_list, idx, element):
    """
    new_in_list() - replace element in list without modifying original list
    Arguments:
    my_list: source list
    idx: index as integer
    element: new element to replace in my_list
    Returns: new list with designated element replaced
    """
    myCopy = []
    myCopy = my_list.copy()

    if type(element) is not int:
        return my_list

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    myCopy[idx] = element
    return myCopy
