#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    output = 0

    if len(argv) - 1 == 0:
        output = 0
        print("{}".format(output))
    else:
        for i in range(1, len(argv)):
            output += int(argv[i])

        print("{}".format(output))
