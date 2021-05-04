#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dupList = my_list[:]
    if idx < 0:
        return dupList
    elif idx >= len(my_list):
        return dupList
    else:
        dupList[idx] = element
        return dupList
