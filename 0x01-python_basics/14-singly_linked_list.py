#!/usr/bin/python3
""" 14-singly_linked_list.py - define singly linked list objects
"""


class Node:
    """ class Node definition """

    def __init__(self, data, next_node=None):
        """
        __init__():
        Arguments:
        self: python self
        data: data object
        next_node: next_node or None object
        Returns: Node object
        """
        self.__data = data
        self.__next_node = next_node

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
        value: next node to set instance to
        Returns: N/A
        """

        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SinglyLinkedList() - singly-linked list with value and next pointer
    """

    __head = None

    def __init__(self):
        """
        __init__() - create empty singly-linked list
        Arguments:
        self: python self
        Returns: empty singly-linked list
        """
        self.__head = None
        return self.__head

    def __str__(self):
        """
        __str__() - print singly-linked list
        Arguments: N/A
        Returns: string of all data in singly-linked list
        """
        print("Printing ssl...")
        sll = ""
        if self.__head is None:
            return ""
        else:
            current = self.__head
            ssl = str(current.data) + "\n"
            while current.next_node != None:
                current = current.next_node
                ssl = str(current.data) + "\n"
        return ssl

    def sorted_insert(self, value):
        """
        sorted_insert()
        Arguments:
        self: python self
        value: value to insert into SLL in increasing order
        Returns: N/A
        """
        new = Node(value, None)
        if self.__head is None:
            self.__head = new
        new.next_node = self.__head

        """
        else:
            prev = None
            current = self.__head
            while current and current.__data < value:
                prev = current
                current = current.next_node

            if current is None and prev is None: # new first element
                new.next_node = current
                self.__head = new
            elif current is None: # must be new last element
                prev.next_node = new
            else: # in the middle
                prev.next_node = new
                new.next_node = current
        """
