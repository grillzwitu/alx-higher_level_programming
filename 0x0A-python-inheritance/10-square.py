#!/usr/bin/python3
"""
    Implementing a Geometry class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        A class Square which inherits from Rectangle
    """
    def __init__(self, size):
        """initialization of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Calculates area of Square"""
        return (self.__size ** 2)
