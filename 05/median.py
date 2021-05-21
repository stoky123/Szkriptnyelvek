#!/usr/bin/env python3


def median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        return numbers[(len(numbers)-1)//2]
    return (numbers[len(numbers)//2-1] + numbers[len(numbers)//2]) / 2


def main():
    print(median([1, 2, 3, 4, 5]))
    print(median([3, 1, 2, 5, 3]))
    print(median([1, 300, 2, 200, 1]))
    print(median([3, 6, 20, 99, 10, 15]))
    print(median([1, 1, 2, 3, 4, 5]))
    print(median([634, 231, 1235675, 324613, 1234534234]))
    

##########################


if __name__ == "__main__":
    main()