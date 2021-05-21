#!/usr/bin/env python3


def sum_of_digits(num):
    summary = 0
    while num != 0:
        summary += num % 10
        num = num // 10
    
    return summary


def main():
    print(sum_of_digits(2**1000))


##########################


if __name__ == "__main__":
    main()