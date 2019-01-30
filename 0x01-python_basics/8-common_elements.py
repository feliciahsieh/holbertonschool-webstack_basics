#!/usr/bin/python3


def common_elements(set_1, set_2):
    if type(set_1) is set and type(set_2) is set:
        common = {}
        common = set_1.intersection(set_2)
        return common
    else:
        return {}
