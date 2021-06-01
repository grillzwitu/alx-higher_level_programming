#!/usr/bin/python3
"""
Implements the from_json_string function
"""

import json


def from_json_string(my_str):
    """
        Converting string into object
    """
    return (json.loads(my_str))
