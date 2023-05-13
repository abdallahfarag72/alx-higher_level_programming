#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argument = "argument" if len(argv) == 2 else "arguments"
    colon = ":" if len(argv) > 1 else "."
    print("{} {}{}".format(len(argv) - 1, argument, colon))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
