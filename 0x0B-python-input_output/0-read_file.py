#!/usr/bin/python3
"""
Implements the read_file function
"""


def read_file(filename=""):
    """
        Reads the contents of a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
