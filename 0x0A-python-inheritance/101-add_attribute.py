#!/usr/bin/python3
"""
   Implements a function that checks for and adds an attribute
"""


def add_attribute(obj, name, value):
    """Checks for and Adds Attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
