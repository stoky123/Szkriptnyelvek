#!/usr/bin/env python3


MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def hangrend(word):
    for i in range(len(word)):
        if word[i] in MELY_MGHK:
            for j in range(i+1, len(word)):
                if word[j] in MAGAS_MGHK:
                    return f"{word}: vegyes"
            return f"{word}: mély"
        
        if word[i] in MAGAS_MGHK:
            for j in range(i+1, len(word)):
                if word[j] in MELY_MGHK:
                    return f"{word}: vegyes"
            return f"{word}: magas"
    return f"{word}: semmilyen"


def main():
    print(hangrend(input("Add meg a szót: ")))


##########################


if __name__ == "__main__":
    main()