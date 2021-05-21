#!/usr/bin/env python3


def loop(szam, debug=False):
    """
    If the debug parameter is True, it prints debug messages, otherwise it doesn't.
    """
    if debug:
        print("# loop kezdete")
        for i in range(szam):
            print(i+1, end=" ")
        print("\n# loop vége")
    else:
        for i in range(szam):
            print(i+1, end=" ")
        print()


def main():
    loop(5)
    print()
    loop(5, debug=True)


##########################


if __name__ == "__main__":
    main()