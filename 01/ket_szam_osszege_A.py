#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 3:
        print("Nem megfelelő számű argumentum!")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print(a+b)


if __name__ == "__main__":
    main()