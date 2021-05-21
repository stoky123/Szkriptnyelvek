#!/usr/bin/env python3


def normalize(str):
    return str.replace(" ", "").lower()


def is_anagramm(str1, str2):
    str1_letters = set(str1)
    str2_letters = set(str2)
    if len(str1_letters) != len(str2_letters) or len(str1) != len(str2):
        return False
    for i in str1_letters:
        str1counter = 0
        str2counter = 0
        for j in str1:
            if j == i:
                str1counter += 1
        for j in str2:
            if j == i:
                str2counter += 1
        if str1counter != str2counter:
            return False
    return True


def main():
    str1 = input("Add meg az első vizsgálandó sztringet: ")
    str2 = input("Add meg a második vizsgálandó sztringet: ")
    if is_anagramm(normalize(str1), normalize(str2)):
        print(f"A(z) '{str1}' és a(z) '{str2}' sztringek anagrammák.")
    else:
        print(f"A(z) '{str1}' és a(z) '{str2}' sztringek nem anagrammák.")



##########################


if __name__ == "__main__":
    main()