#!/usr/bin/env python3


def main():
    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = range(ord('a'), ord('z')+1)

    for t in list(zip(list(chars), codes)):
        print(t)


##########################


if __name__ == "__main__":
    main()