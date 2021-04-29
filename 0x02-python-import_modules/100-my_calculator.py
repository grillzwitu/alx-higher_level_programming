#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":

    #Throw an error if arguements are not 3
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
    #If argv[2](operator) is +
        if argv[2] == '+':
            print("{} + {} = {:d}".format(a, b, add(a, b)))
    #If argv[2](operator) is -
        elif argv[2] == '-':
            print("{} - {} = {:d}".format(a, b, sub(a, b)))
    #If argv[2](operator) is *
        elif argv[2] == '*':
            print("{} * {} = {:d}".format(a, b, mul(a, b)))
    #If argv[2](operator) is /
        elif argv[2] == '/':
            print("{} / {} = {:d}".format(a, b, div(a, b)))
    #If operator is not +, -, * or /
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
