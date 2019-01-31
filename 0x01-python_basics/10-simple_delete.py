#!/usr/bin/python3
""" 10-simple_delete.py - delete a dictionary entry with given key
"""


def simple_delete(my_dict, key=""):
    """
    simple_delete() - delete a dictionary entry with given key
    Arguments:
    my_dict: dictionary to check
    key: key in dictionary to delete
    Returns: original my_dict if key not found or modified my_dict
    """
    if type(my_dict) is dict and type(key) is str:
        if key in my_dict:
            del my_dict[key]

    return my_dict
