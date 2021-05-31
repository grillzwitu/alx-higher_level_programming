#!/usr/bin/python3
"""The module contains a lookup function"""


def lookup(obj):
    """
        Returns a list of avaiblable attributes and methods in the object
    """
    return (dir(obj))
