import time


def munchausen(hatvanyok,limit):
    for n in range(limit):
        summary = 0
        for digit in  str(n):
            summary += hatvanyok[int(digit)]
            if summary > n:
                break
        if summary == n:
            print(n)


def main ():
    hatvanyok = [0, 1 ** 1, 2 ** 2, 3 ** 3, 4 ** 4, 5 ** 5, 6 ** 6, 7 ** 7, 8 ** 8, 9 ** 9]
    print("A Münchausen számok 10000 alatt: ")
    munchausen(hatvanyok, 10000)
    print()
    start = time.time()
    print("Az összes Münchausen szám: ")
    munchausen(hatvanyok,440000000)
    end = time.time()
    print()
    print("Futási idő:", end-start)

main()