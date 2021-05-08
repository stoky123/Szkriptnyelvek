#!/usr/bin/env python3

def greeting(name):
    print("Hello "+ name.strip() + "!")

def main():
    name = input("Name: ")
    greeting(name)

if __name__ == "__main__":
    main()