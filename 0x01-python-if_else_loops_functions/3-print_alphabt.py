#!/usr/bin/python3
for c in range(ord('a'), ord('{')):
    if c == ord('e') or c == ord('q'):
        continue
    print("{}".format(chr(c)), end="")
