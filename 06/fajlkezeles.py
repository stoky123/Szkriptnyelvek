#!/usr/bin/env python3


def main():
    with open("string1.py", 'r') as reading:
        with open("string1_clean.py", 'w') as writing:
            for line in reading:
                if not line.lstrip().startswith('#'):
                    writing.write(line)


##########################


if __name__ == "__main__":
    main()