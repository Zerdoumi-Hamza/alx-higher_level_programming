#!/usr/bin/python3

if __name__ == " __main__":
    """ Print the number of and list of arguments."""
    import sys

    argument = sys.argv
    size_argument = len(argument)

    if size_argument == 1:
        print("{} arguments.".format(size_argument - 1))

    elif size_argument == 2:
        print("{} argument:".format(size_argument - 1))
        print("{}: {}".format(size_argument - 1, argument[1]))

    else:
        print("{} arguments:".format(size_argument - 1))
        for i in range(1, size_argument):
            print("{}: {}".format(i, argument[i]))
