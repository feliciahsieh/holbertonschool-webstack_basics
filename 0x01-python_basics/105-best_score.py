#!/usr/bin/python3
""" 105-best_score.py - finds key with biggest integer value
"""


def best_score(my_dict):
    """
    best_score()
    Arguments:
    my_dict: dictionary of scores
    Returns: dictionary key with max value
    """

    if my_dict is None or len(my_dict) == 0 or type(my_dict) is not dict:
        return None

    maxValue = maxKey = 0
    for i in sorted(my_dict.keys()):
        if maxValue < my_dict[i]:
            maxValue = my_dict[i]
            maxKey = i

    return maxKey
