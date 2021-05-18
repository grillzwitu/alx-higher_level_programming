#!/usr/bin/python3
"""Defines a class named square"""


class Square:
    """A square class
    Attributes:
    size: The size of the square
    position (int, int): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) is not int or type(position[1]) is not int\
           or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """Gets the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of square based on a value paremeter"""
        if type(value) is not tuple or len(value) != 2\
           or type(value[0]) is not int or type(value[1]) is not int\
           or value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of two positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using # charcter"""
        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print()
        strchr = '#' * self.__size
        space = ' ' * self.__position[0]
        for i in range(self.__size):
            print(space, strchr, sep='')
