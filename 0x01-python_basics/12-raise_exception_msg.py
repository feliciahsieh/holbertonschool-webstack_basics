#!/usr/bin/python3
""" 12-raise_exception_msg.py - raise a NameError exception and print message
"""


def raise_exception_msg(message=""):
    """ raise_exception_msg() - raise a NameError exception and print message
    Arguments:
    message: string of message to user
    Returns: NameError exception with message
    """
    raise NameError(message)
