#!/usr/bin/python3
""" 13-add_integer.py - adds 2 integers with type checking
"""


def add_integer(a, b):
    """
    add_integer - adds 2 integers with type checking
    Arguments:
    a: operand 1
    b: operand 2
    Returns: raises an rror with a message
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
