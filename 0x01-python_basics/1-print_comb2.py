#!/usr/bin/python3
""" 1-print_comb2.py - print numbers from 0 - 99 separated by comma
"""
for i in range(0, 99):
    print("{:02d}".format(i), end=", ")
print("99", end="\n")
