#!/usr/bin/env python3


def main():
    cells = [0] * 600
    for i in range(len(cells)):
        for j in range(i, len(cells), i+1):
            cells[j] = (cells[j] + 1) % 2


    print([i+1 for i in range(len(cells)) if cells[i] == 1])
            

##########################


if __name__ == "__main__":
    main()