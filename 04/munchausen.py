#!/usr/bin/env python3


def munchausen(limit):
    """
    Prints every münchausen number in the range of limit.
    """
    for i in range(1, limit+1):
        number = sum([int(digit)**int(digit) for digit in str(i)])
        if number == i:
            print(i)



def main():
    print("A 10000-nél kisebb Münchausen számok: ")
    munchausen(10000)
    print()
    print("Az összes Münchausen szám: ")
    munchausen(440000000)


##########################


if __name__ == "__main__":
    main()