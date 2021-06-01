#!/usr/bin/python3
"""
    Defines a student class
"""


class Student:
    """
        A class Student
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrives the dict representation of the class
        """
        my_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                        my_dict = self.__dict__
                        break
                try:
                    my_dict[i] = getattr(self, i)
                except:
                    pass
        else:
            my_dict = self.__dict__
        return (my_dict)
