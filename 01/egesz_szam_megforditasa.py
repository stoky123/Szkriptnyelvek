#!/usr/bin/env python3


def reverse(number):
    return int(str(number)[::-1])


def main():
    number = int(input("Adj meg egy pozitív egész számot: "))
    print(reverse(number))
    print(type(number))


if __name__ == "__main__":
    main()
