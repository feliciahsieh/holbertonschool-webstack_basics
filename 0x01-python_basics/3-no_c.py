#!/usr/bin/python3


def no_c(str):
    s = ''
    for c in str:
        if c != 'c' and c != 'C':
            s += c
    return s
