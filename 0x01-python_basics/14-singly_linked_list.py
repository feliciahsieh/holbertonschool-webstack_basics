#!/usr/bin/python3
""" 14-singly_linked_list.py -
"""

class Node():

    __data
    next_node

    @property
    def data(self):
    """
    data() - getter
    Arguments:
    self: python self
    Returns: private instance data
    """
        return self.__data

    @data.setter
    def data(self, value):
        """
        data() - setter
        Arguments:
        self: python self
        value: value to set instance to
        Returns: N/A
        """

        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")


    @property
    def next_node(self):
    """
    next_node() - getter
    Arguments:
    self: python self
    Returns: private instance next_node
    """
        return self.__next_node

    @data.setter
    def next_node(self, value):
        """
        next_node() - setter
        Arguments:
        self: python self
        value: value to set instance to
        Returns: N/A
        """

        if type(value) is Node or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


    def __init__(self, data, next_node=None):
        """
        __init__():
        Arguments:
        self: python self
        data: data object
        next_node: next_node or None object
        Returns: Node object
        """
        data = ??
        next_node??
