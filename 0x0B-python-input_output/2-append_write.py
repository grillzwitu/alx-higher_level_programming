#!/usr/bin/python3
"""
Implements the function "append_wrtie"
"""


def append_write(filename="", text=""):
    """returns the number of chars appended to filename from text"""
    with open(filename, "a", encoding="utf=8") as f:
        no_chars = f.write(text)
    return no_chars
