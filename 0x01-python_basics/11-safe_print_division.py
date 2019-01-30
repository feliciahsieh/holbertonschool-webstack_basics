#!/usr/bin/python3
""" 11-safe_print_division.py - divide 2 numbers with checks
"""


def safe_print_division(a, b):
    """ safe_print_division() - divide 2 numbers with checks
    Arguments:
    a: operand 1
    b: operand 2
    Returns: the result of a divided by b or None if result is N/A
    """
    try:
        res = a / b
        return res
    except Exception as e:
        res = None
    finally:
        print("Inside result: {}".format(res))
