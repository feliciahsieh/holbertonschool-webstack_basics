#!/usr/bin/python3
""" 0-print_alphabt.py - print alphabet except letters q and e
"""
start = ord('a')
end = ord('z') + 1
for i in range(start, end):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
