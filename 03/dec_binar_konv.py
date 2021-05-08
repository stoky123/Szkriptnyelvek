#!/usr/bin/env python3


def dec_to_bin(dec):
    binar = ""
    while(dec // 2 != 0):
        binar += str(dec % 2)
        dec = dec // 2
    
    return int("1"+binar[::-1])


def main():
    dec = int(input("Melyik számot alakítsuk binárisba?\n"))
    print(f"{dec} bináris számrendszerben ábrázolva:", dec_to_bin(dec))

##########################


if __name__ == "__main__":
    main()