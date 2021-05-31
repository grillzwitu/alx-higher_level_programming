#!/usr/bin/python3
"""Inherits from a list"""


class MyList(list):
    """a subclass of list"""
    def print_sorted(self):
        """Prints a sorted list without changing the original"""
        print(sorted(self))
