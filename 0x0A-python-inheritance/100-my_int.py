#!/usr/bin/python3
"""
    Class that takes an integers
"""


class MyInt(int):
    """A class MyInt that is a rebel version of an int class"""
    def __init__(self, number):
        """Initializes MyInt"""
        self.number = number

    def __ne__(self, val):
        """Defines =="""
        return (self.number == val)

    def __eq__(self, val):
        """Defines !="""
        return (self.number != val)

    def __str__(self):
        """String Representation of MyInt"""
        return (str(self.number))
