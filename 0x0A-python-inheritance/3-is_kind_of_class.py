#!/usr/bin/python3
"""
This module contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
        Checks that obj is an instance of a_class which inherits from a class
    """
    return (isinstance(obj, a_class))
