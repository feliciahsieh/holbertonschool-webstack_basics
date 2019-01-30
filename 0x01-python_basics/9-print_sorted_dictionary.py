#!/usr/bin/python3
""" 9-print_sorted_dictionary.py - print a sorted dictionary
"""


def print_sorted_dictionary(my_dict):
    """
    print_sorted_dictionary():
    Arguments:
    my_dict: dictionary to sort and print
    Returns: None
    """
    if my_dict is not None and len(my_dict) > 0:
        for i in sorted(my_dict.keys()):
            print("{}: {}".format(i, my_dict[i]))
