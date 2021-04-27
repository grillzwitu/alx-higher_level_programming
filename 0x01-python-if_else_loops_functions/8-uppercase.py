#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        char = ord(str[c])
        if char >= ord('a') and char <= ord('z'):
            char -= 32
        print("{}".format(chr(char)), end='')
    print()
