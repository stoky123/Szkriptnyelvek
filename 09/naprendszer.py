#!/usr/bin/env python3
import pandas as pd


def main():
    words = pd.read_csv("DT2.csv")["a"]
    for word in words:
        try:
            pos = word.lower().find('j')
            if pos >= 0:
                pos2 = word[pos:].lower().find('s')
                pos += pos2
                if pos2 >= 0:
                    pos2 = word[pos:].lower().find('u')
                    pos += pos2
                    if pos2 >= 0:
                        pos2 = word[pos:].lower().find('n')
                        pos += pos2
                        if pos2 >= 0:
                            print(word)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        except AttributeError:
            word2 = str(word)
            pos = word2.lower().find('j')
            if pos >= 0:
                pos2 = str(word[pos:]).lower().find('s')
                pos += pos2
                if pos2 >= 0:
                    pos2 = str(word[pos:]).lower().find('u')
                    pos += pos2
                    if pos2 >= 0:
                        pos2 = str(word[pos:]).lower().find('n')
                        pos += pos2
                        if pos2 >= 0:
                            print(word)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
            
            

##########################


if __name__ == "__main__":
    main()