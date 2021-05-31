#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
        Check if the objects are of the same class
    """
    if type(obj) is a_class:
        return True
    return False
