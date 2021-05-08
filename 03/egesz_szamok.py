#!/usr/bin/env python3


def main():
    #Python shellben:
    #feladat
    #print(sum(range(1,101)))
    #variáció
    digit_sum = 0
    for i in range(1,101):
        for j in str(i):
            digit_sum += int(j)

    print("1-től 100-ig az egész számok számjegyeinek összege:", digit_sum)


##########################


if __name__ == "__main__":
    main()
