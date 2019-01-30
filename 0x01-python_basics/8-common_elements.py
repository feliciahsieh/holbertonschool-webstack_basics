#!/usr/bin/python3
""" 8-common_elements.py - find common elements between 2 lists
"""


def common_elements(set_1, set_2):
    """
    common_elements() - find common elements between 2 lists
    Arguments:
    set_1: set 1 to check
    set_2: set 2 to check
    Returns: list of common elements
    """
    if type(set_1) is set and type(set_2) is set:
        common = {}
        common = set_1.intersection(set_2)
        return common
    else:
        return {}
