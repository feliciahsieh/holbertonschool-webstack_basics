#!/usr/bin/python3
""" 102-infinite_add.py - adds infinite-sized integers together """

import sys


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here

    if len(sys.argv) < 2:
        print("0")
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(sum)
