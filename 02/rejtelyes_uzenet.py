#!/usr/bin/env python3


DECRYPTED = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def main():
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_abc = abc.lower()

    encrypted = ""

    for letter in DECRYPTED.strip():
        if letter in abc:
            encrypted += abc[(abc.index(letter)+2) % len(abc)]
        elif letter in lower_abc:
            encrypted += lower_abc[(lower_abc.index(letter)+2) % len(lower_abc)]
        else:
            encrypted += letter

    print(encrypted)



##########################


if __name__ == "__main__":
    main()