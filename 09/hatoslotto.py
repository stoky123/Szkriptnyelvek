#!/usr/bin/env python3
import time

def lotto(sum_numbers, product, numbers):
    for index, i in enumerate(numbers):
        for index2, j in enumerate(numbers[index+1:]):
            for index3, k in enumerate(numbers[index2+1:]):
                for index4, l in enumerate(numbers[index3+1:]):
                    for index5, m in enumerate(numbers[index4+1:]):
                        for n in numbers[index5+1:]:
                            if ((i + j + k + l + m + n) == sum_numbers and (i * j * k * l * m * n) == product):
                                return (i, j, k, l, m, n)


def main():
    start = time.time()
    osszeg = 90
    szorzat = 996300
    szamok = [i for i in range(1, 46) if not szorzat % i]
    print(lotto(osszeg, szorzat, szamok))
    print("Futási idő:", time.time() - start)


##########################


if __name__ == "__main__":
    main()