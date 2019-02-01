#!/usr/bin/python3
"""106-weight_average.py - calc weighted average of all integer tuples
"""


def weight_average(my_list=[]):
    """ weight_average() - calc weighted average of all integer tuples
    Arguments:
    my_list: list of tuples
    Returns: weighted average
    """

    if my_list == []:
        return 0
    else:
        sum = 0
        denom = 0

        for i in my_list:
            sum += i[0] * i[1]
            denom += i[1]

        return sum / denom
