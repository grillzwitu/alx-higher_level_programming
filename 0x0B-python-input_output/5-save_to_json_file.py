#!/usr/bin/python3
"""
Implements the save_to_json_file function
"""

import json


def save_to_json_file(my_obj, filename=""):
    """writes an my_obj to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
