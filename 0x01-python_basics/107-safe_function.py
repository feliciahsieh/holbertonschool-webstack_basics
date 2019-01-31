#!/usr/bin/python3
""" 107-safe_function.py - run a function safely """

import sys


def safe_function(fct, *args):
    """ safe_function() - run a function safely by catching Exceptions
    Arguments:
    fct: pointer to a function
    args: arguments for the function
    Returns: result of the function
    """

    try:
        result = 0
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write("Exception: " + str(e.args[0]) + "\n")
        return None
