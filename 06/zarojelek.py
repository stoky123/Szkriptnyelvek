#!/usr/bin/env python3

import random


PAROK = {
    '{' : '}',
    '[' : ']',
    '(' : ')'
}

def is_valid(text):
    to_find = []
    for char in text:
        if char in PAROK.values():
            if len(to_find) and char == PAROK.get(to_find[-1], None):
                to_find.pop()
            else:
                return False
        elif char in PAROK.keys():
            to_find.append(char)
    
    return not bool(to_find)


def main():
    to_test = ["((5+3)*2+1)", "{[(3+1)+2]+}", "(3+{1-1)}", "[1+1]+(2*2)-{3/3}", "(({[(((1)-2)+3)-3]/3}-3)", "[[][(())]]", "[{[]{}}]{}()((([{}])))", "}{", "[{[]{}}]{}()((([{}])))}"]
    for text in to_test:
        print(f"{text}: szabályos" if is_valid(text) else f"{text}: nem szabályos")
        
        
##########################


if __name__ == "__main__":
    main()