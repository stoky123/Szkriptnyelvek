#!/usr/bin/env python3


def is_palindrom_trivial(text):
    return text == text[::-1]


def is_palindrom_iterative(text):
    i = 0

    while text[(-1)-i] == text[i] and i < len(text)/2-1:
        i += 1

    return i >= len(text)/2-1

def is_palindrom_recursive(text, index):
    if index > len(text)/2-1:
        return True
    
    if text[(-1)-index] == text[index]:
        return is_palindrom_recursive(text, index+1)

    return False


def main():
    text = input("Add meg a tesztelendő szöveget: ")
    if is_palindrom_trivial(text):
        print("A megadott szöveg palindrom. (trivial)")
    else:
        print("A megadott szöveg nem palindrom. (trivial)")

    if is_palindrom_iterative(text):
        print("A megadott szöveg palindrom. (iterative)")
    else:
        print("A megadott szöveg nem palindrom. (iterative)")

    if is_palindrom_recursive(text, 0):
        print("A megadott szöveg palindrom. (recursive)")
    else:
        print("A megadott szöveg nem palindrom. (recursive)")


##########################


if __name__ == "__main__":
    main()