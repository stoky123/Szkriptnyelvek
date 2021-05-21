#!/usr/bin/env python3


def main():
    """
    Returns the sum of the numbers from 1 to 1000 that is divisible by 3 or 5.
    """
    print(sum([n for n in range(1, 1000) if (n % 3 == 0) or (n % 5 == 0)]))

##########################


if __name__ == "__main__":
    main()