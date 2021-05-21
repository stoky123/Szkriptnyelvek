#!/usr/bin/env python3


def main():
    f = open("day02.txt")
    osszeg = 0
    for line in f:
        sor = [int(x) for x in line.rstrip('\n').split()]
        osszeg += max(sor) - min(sor) 

    print(osszeg)
    f.close()


##########################


if __name__ == "__main__":
    main()