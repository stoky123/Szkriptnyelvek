#!/usr/bin/env python3

def feladat1(words):
    """Makes every word uppercase."""
    return [w.upper() for w in words]

def feladat2(names):
    """Capitalizes every word."""
    return [name.capitalize() for name in names]

def feladat3():
    """Creates a list with 10 0 digits."""
    return [0 for i in range(10)]

def feladat4(numbers):
    """Returns a list with the square of the original list."""
    return [i*2 for i in numbers]

def feladat5(numbers):
    """Converts every element of the list to int."""
    return [int(n) for n in numbers]

def feladat6(string):
    """Seperates all digits in the string and returns it as a list of ints."""
    return [int(n) for n in string]

def feladat7(words):
    """Returns a list of the length of the words."""
    return [len(word) for word in words]

def feladat8(words):
    """Returns the first letter of every element."""
    return [word[0] for word in words.split()]

def feladat9(words):
    """Returns the word with it's length in a list of tuples."""
    return [(word, len(word)) for word in words.split()]

def feladat10():
    """Returns every even number from 0-9"""
    return [i for i in range(10) if i % 2 == 0]

def feladat11():
    """Returns every square number from 1 to 400 if it's even"""
    return [n*n for n in range(20) if n*n % 2 == 0]

def feladat12():
    """Returns every square number if it's last digit is 4"""
    return [n*n for n in range(20) if n*n % 10 == 4]

def feladat13():
    """Returns the uppercase letters of the english alphabet in a list"""
    return "".join([chr(n).upper() for n in range(97, 97+26)])

def feladat14(words):
    """Returns every element of the list without whitespaces in the beginning and the end."""
    return [word.strip() for word in words]

def feladat15(numbers):
    """Creates a string from a list of ints."""
    return "".join([str(n) for n in numbers])


def main():
    print(feladat1(['auto', 'villamos', 'metro']))
    print(feladat2(['aladar', 'bela', 'cecil']))
    print(feladat3())
    print(feladat4(list(range(1,11))))
    print(feladat5(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']))
    print(feladat6("1234567"))
    print(feladat7('The quick brown fox jumps over the lazy dog'.split()))
    print(feladat8("python is an awesome language"))
    print(feladat9('The quick brown fox jumps over the lazy dog'))
    print(feladat10())
    print(feladat11())
    print(feladat12())
    print(feladat13())
    print(feladat14([' apple ', ' banana ', ' kiwi']))
    print(feladat15([1, 0, 1, 1, 0, 1, 0, 0]))


##########################


if __name__ == "__main__":
    main()