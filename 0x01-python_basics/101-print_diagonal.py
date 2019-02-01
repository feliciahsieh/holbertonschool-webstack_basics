#!/usr/bin/python3
""" 101-print_diagonal.py - draw an ascii diagonal to output
"""


def print_diagonal(n):
    """
    print_diagonal - draw an ascii diagonal to output
    Arguments:
    n: number of diagonals
    Returns: N/A
    """
    if n <= 0:
        print("\n")
    elif n > 0:
        for i in range(0, n):
            print("{}\\".format(" " * i), end="\n")
