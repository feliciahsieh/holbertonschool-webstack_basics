#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    if my_dict is not None and len(my_dict) > 0:
        for i in sorted(my_dict.keys()):
            print("{}: {}".format(i, my_dict[i]))
