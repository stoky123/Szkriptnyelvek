#!/usr/bin/env python3


def queens(pos):
    print("+-----------------+")
    for i in range(len(pos)-1, -1, -1):
        print('|', end=" ")
        for j in pos:
            if j == i:
                print('Q', end=" ")
            else:
                print('.', end=" ")
        print('|')
    print("+-----------------+")


def main():
    queens([7,3,0,2,5,1,6,4])
    queens([0,4,7,5,2,6,1,3])


##########################


if __name__ == "__main__":
    main()