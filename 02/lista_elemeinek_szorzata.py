#!/usr/bin/env python3


def product(numbers):
    prod = 1
    for number in numbers:
        prod *= number
    return prod


def main():
    numbers1 = [5, 1, 3, 7, 3, 2, 2, 74, 21]
    numbers2 = [2, 5, 3]
    numbers3 = [10, 5, 3, 2, 8]
    empty_list = []
    print(product(numbers1))
    print(product(numbers2))
    print(product(numbers3))
    print(product(empty_list))

##########################


if __name__ == "__main__":
    main()