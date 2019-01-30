#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if type(element) is not int:
        return my_list

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    my_list[idx] = element
    return my_list
