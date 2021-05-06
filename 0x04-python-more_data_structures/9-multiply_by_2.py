#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = dict()
    for key, value in a_dictionary.items():
        newDict.update({key: value * 2})
    return newDict
