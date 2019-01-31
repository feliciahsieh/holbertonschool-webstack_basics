#!/usr/bin/python3
""" 15-square.py - print a square of chars to output
"""


class Square:
    """ class: Square - object to help print a square to output """

    @property
    def size(self):
        """ size Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size Setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __init__(self, size=0):
        """ __init__ - initialize square class """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area - returns area of Square object """
        return self.size * self.size

    def my_print(self):
        """ my_print - print a square using Square object """
        if self.__size != 0:
            for r in range(self.__size):
                print("#" * self.__size, end="\n")
        else:
            print()
