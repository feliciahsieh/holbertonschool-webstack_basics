#!/usr/bin/python3
"""2-islower.py - checks if char is lowercase
"""


def islower(c):
    """
    islower() - checks if char is lowercase
    Arguments:
    c: character to check
    Returns: True if lowercase or False if not
    """
    try:
        if len(c) == 1:
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                return True
        return False
    except Exception as e:
        print("type error: " + str(e))
        return False
