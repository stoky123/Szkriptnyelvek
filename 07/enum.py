#!/usr/bin/env python3

from enum import Enum


class Hangrend(Enum):
    MELY = 'aáoóuú'
    MAGAS = 'eéiíöőüű'
    VEGYES = MELY + MAGAS


def hangrend(word):
    mely = False
    magas = False
    for c in word:
        if c in Hangrend.MELY.value:
            mely = True
        elif c in Hangrend.MAGAS.value:
            magas = True

    return [mely, magas]

def main():
    szavak = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for word in szavak:
        eredmeny = hangrend(word)
        if eredmeny[0] and eredmeny[1]:
            print(f"{word}: Vegyes")
        elif eredmeny[0]:
            print(f"{word}: Mély")
        elif eredmeny[1]:
            print(f"{word}: Magas")
        


##########################


if __name__ == "__main__":
    main()