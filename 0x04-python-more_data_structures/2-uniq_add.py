#!/usr/bin/python3
def uniq_add(my_list=[]):
    newList = []
    for i in my_list:
        if i not in newList:
            newList.append(i)
    return sum(newList)
