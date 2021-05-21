#!/usr/bin/env python3


def valid(text, chars=""):
    """
    Returns the common characters in the first and the second characters, if there is none, it returns an empty string, if there is no second parameter, it returns the first character of the first parameter.
    """
    result = ""
    if chars == "":
        return text[0]
    for c in text:
        if c in chars:
            result += c

    return result


def main():
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))
    print(valid("Hello", "Hello"))
    print(valid("sup", "nem"))


##########################


if __name__ == "__main__":
    main()