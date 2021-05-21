#!/usr/bin/env python3

import string
import sys


def main():
    """
    If the a-z.py file was executed, it prints the english alphabet, if the z-a.py file was executed, it prints the english alphabet backwards.
    """
    if sys.argv[0].endswith("a-z.py"):
        print(string.ascii_lowercase)
    elif sys.argv[0].endswith("z-a.py"):
        print(string.ascii_lowercase[::-1])


##########################


if __name__ == "__main__":
    main()