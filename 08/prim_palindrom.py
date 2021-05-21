#!/usr/bin/env python3


def fme(number: int, exponent: int, modulus: int) -> int:
    szorzat = 1
    b = number
    for i in "{0:b}".format(exponent)[::-1]:
        if int(i):
            szorzat *= b
        b = b**2 % modulus

    return szorzat % modulus


def miller_rabin(number: int) -> bool:
    (a, s, p) = (2, 0, number-1)
    while not p % 2:
        s += 1
        p = p // 2

    elso = fme(a, p, number)
    if elso == 1 or elso == number-1:
        return True

    for _ in range(1, s):
        elso = (elso ** 2) % number
        if elso == number-1:
            return True
    
    return False

def palindrom(number: int) -> bool:
    return str(number) == str(number)[::-1]


def test(number: int) -> int:
    if number == 2:
        return number
    number += (number+1) % 2
    while(not miller_rabin(number) or not palindrom(number)):
        number += 2

    return number

    
def main() -> None:
    print(f"31-hez képest a legkisebb paindrom prím: {test(31)}")
    print(f"130-hoz képest a legkisebb paindrom prím: {test(130)}")
    print(f"131-hez képest a legkisebb paindrom prím: {test(131)}")
    print(f"1977-hez képest a legkisebb paindrom prím: {test(1977)}")



##########################


if __name__ == "__main__":
    main()