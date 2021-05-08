#!/usr/bin/env python3


def string_clear(text):
    return text.replace(" ", "").replace(r"\n", "")


def main():
    text = input("Add meg a tisztítandó szöveget: ")
    print(string_clear(text))


##########################


if __name__ == "__main__":
    main()