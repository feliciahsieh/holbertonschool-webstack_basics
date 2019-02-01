#!/usr/bin/python3
""" 4-add.py - adds 2 numbers. File is imported in from main()
"""

from add_4 import add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    # run when run as main program (not called in an 'import')
