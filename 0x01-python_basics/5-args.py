#!/usr/bin/python3
""" 5-args.py - print command line arguments
"""

import sys

n = len(sys.argv) - 1
if n == 0:
    print("0 arguments.")
elif n == 1:
    print("1 argument:\n{}: {}".format(n, sys.argv[1]))
else:
    print("{} arguments:".format(n))
    for i in range(1, n + 1):
        print("{}: {}".format(i, sys.argv[i]))
