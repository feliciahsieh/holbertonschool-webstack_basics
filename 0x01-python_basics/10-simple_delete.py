#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    if type(my_dict) is dict and type(key) is str:
        if key in my_dict:
            del my_dict[key]

    return my_dict
