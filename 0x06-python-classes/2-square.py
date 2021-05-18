#!/usr/bin/python3
"""Defines a class named square"""


class Square:
    """A square class
    Attributes:
    size: The size of the square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
