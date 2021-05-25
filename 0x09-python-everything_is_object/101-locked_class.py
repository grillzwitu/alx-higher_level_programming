#!/usr/bin/python3
"""Defines a class module"""


class LockedClass:
    """A class that only lets the user create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
