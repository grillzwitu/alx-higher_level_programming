#!/usr/bin/python3
"""
   Implements a function that checks for and adds an attribute
"""


def add_attribute(cls, name, first):
    """Checks for and Adds Attribute"""
    if not hasattr(cls, name):
        raise TypeError("can't add new attribute")
    cls.name = first
