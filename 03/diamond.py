#!/usr/bin/env python3


def diamond(height):
    for i in range(height-1):
        print((height-1-i)*' ' + '*'*(2*i+1))
    for i in range(height-1, -1, -1):
        print((height-1-i)*' ' + '*'*(2*i+1))


def main():
    height = int(input("Add meg a gyémánt magasságát (páratlan számot adj meg): "))
    if height % 2:
        diamond((height+1)//2)
    else:
        print("Páros magasságú gyémántot nem tudunk nyomtatni.")

##########################


if __name__ == "__main__":
    main()