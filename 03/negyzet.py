#!/usr/bin/env python3


def main():
    negyzet_összege = 0
    for i in range(1,101):
        negyzet_összege += i**2
    
    print("Összeg négyzete és négyzetek összege közötti különbség:", sum(range(1,101))**2-negyzet_összege)


##########################


if __name__ == "__main__":
    main()