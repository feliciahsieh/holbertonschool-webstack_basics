#!/usr/bin/python3
""" 3-no_c.py - print string without letters c or C
"""


def no_c(str):
    """
    no_c() - print string without letters c or C
    Arguments:
    str: string to evaluate
    Returns: modified string (w/o c or C)
    """
    s = ''
    for c in str:
        if c != 'c' and c != 'C':
            s += c
    return s
