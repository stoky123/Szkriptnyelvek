#!/usr/bin/env python3


def is_anagramm(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())


def main():
    str1 = input("Add meg az első vizsgálandó sztringet: ")
    str2 = input("Add meg a második vizsgálandó sztringet: ")
    if is_anagramm(str1, str2):
        print(f"A(z) '{str1}' és a(z) '{str2}' sztringek anagrammák.")
    else:
        print(f"A(z) '{str1}' és a(z) '{str2}' sztringek nem anagrammák.")


##########################


if __name__ == "__main__":
    main()