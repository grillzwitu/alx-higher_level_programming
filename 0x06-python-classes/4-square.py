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

    def area(self):
        """Calculates the area of the square based on its size
        Returns:
        The area (int).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the current area/size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """resets the size of the square based on the value passed"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
