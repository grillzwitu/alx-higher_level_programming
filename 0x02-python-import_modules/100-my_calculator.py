#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    #Throw an error if arguements are not 3
    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    #If argv[2](operator) is +
    if argv[2] == '+':
        print("{} + {} = {:d}"
              .format(argv[1], argv[3], add(int(argv[1]), int(argv[3]))))
    #If argv[2](operator) is -
    elif argv[2] == '-':
        print("{} - {} = {:d}"
              .format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))
    #If argv[2](operator) is *
    elif argv[2] == '*':
        print("{} * {} = {:d}"
              .format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))
    #If argv[2](operator) is /
    elif argv[2] == '/':
        print("{} / {} = {:d}"
              .format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))
    #If operator is not +, -, * or /
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
