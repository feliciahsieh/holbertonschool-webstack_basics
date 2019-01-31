#!/usr/bin/python3
""" 104-search_replace.py - replace all occurrences of an element with another
"""


def search_replace(my_list, search, replace):
    """
    search_replace() - replace all occurrences of an element with another
    Arguments:
    my_list: target list
    search: element to replace in list
    replace: new element
    Returns: new list
    """
    if type(my_list) is list and len(my_list) > 0:
        return [replace if x == search else x for x in my_list]
    return my_list
