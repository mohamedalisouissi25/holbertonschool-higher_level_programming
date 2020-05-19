#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    """
    def __init__(self, size=0):
        """initializes the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculates the square's area
        """
        return (self.__size) ** 2
