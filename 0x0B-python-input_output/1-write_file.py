#!/usr/bin/python3
"""
Implements the function "write_file"
"""


def write_file(filename="", text=""):
    """returns the number of chars written to filename from text"""
    with open(filename, mode="w", encoding="utf-8") as f:
        no_char = f.write(text)
    return no_char
