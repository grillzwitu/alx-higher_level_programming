#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDigit = (int(repr(-number)[-1])) * -1
else:
    lastDigit = int(repr(number)[-1])

if lastDigit > 5:
    print("Last digit of {0:d} is {1:d} and is greater than 5"
          .format(number, lastDigit))
elif lastDigit == 0:
    print("Last digit of {0:d} is {1:d} and is 0"
          .format(number, lastDigit))
elif lastDigit < 6 and not 0:
    print("Last digit of {0:d} is {1:d} and is less than 6 and not 0"
          .format(number, lastDigit))
