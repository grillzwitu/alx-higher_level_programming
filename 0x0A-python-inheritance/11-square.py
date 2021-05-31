#!/usr/bin/python3
"""
    Implements BaseGeometry class
"""


class BaseGeometry:
    """A class BaseGeometry with instance methods area and integer_validator"""
    def area(self):
        """
            Calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates value is an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        A class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializing width and height of Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of Rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
        A class Square that inherits from Rectangle
    """
    def __init__(self, size):
        """initialization of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Calculates area of Square"""
        return (self.__size ** 2)

    def __str__(self):
        ""String representation of Square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
