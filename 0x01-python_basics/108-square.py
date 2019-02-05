#!/usr/bin/python3
""" 108-square.py """


class Square:
    """ class definition of Square object """

    @property
    def size(self):
        """ size() - getter for size
        Arguments: N/A
        Returns: size of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size() - setter for size
        Arguments:
        value: integer value to set size
        Returns: N/A
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position() - getter for position (a tuple)
        Arguments: N/A
        Returns: N/A
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ position() - sets position (a tuple)
        Arguments:
        value: tuple holding upper left corner of square
        Returns: N/A
        """
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__()
        Arguments:
        size: size of square object as int
        position: position of upper left corner of square as tuple
        Returns: N/A
        """
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area() - returns area of square
        Arguments: N/A
        Returns: area of square as integer
        """
        return self.__size * self.__size

    def my_print(self):
        """ my_print() - print out square at right coordinates
        Arguments: N/A
        Returns: N/A
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for s in range(self.size):
                print(" " * self.__position[0] + ("#" * self.__size), end="\n")
