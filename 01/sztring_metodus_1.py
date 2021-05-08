#!/usr/bin/env python3

# A swapcase() szting metódus egy olyan sztringgel tér vissza, amiben az eredeti
# sztringgel ellentétben a kisbetűkből nagybetűket, a nagybetűkből pedig kisbetűket
# csinál.

def main():
    s = input("Adj meg egy sztringet: ")

    print()

    print("Eredeti sztring: " + s)

    print("Swapcase()-el: " + s.swapcase())

    print('Az eredeti szting ("' + s + '") ugyanaz maradt.')

if __name__ == "__main__":
    main()
    

