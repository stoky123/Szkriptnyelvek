#!/usr/bin/env python3

def palindrom_binary(number: int) -> bool:
    bi = "{0:b}".format(number)

    return bi == bi[::-1]


def palindrom(number: int) -> bool:
    return str(number) == str(number)[::-1]


def main() -> None:
    result = 0
    for i in range(1000000):
        if palindrom(i) and palindrom_binary(i):
            result += i
    
    print(result)


##########################


if __name__ == "__main__":
    main()