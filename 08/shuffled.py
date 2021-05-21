#!/usr/bin/env python3

import random
from typing import List


def shuffled(li: List) -> List:
    copy = li.copy()
    random.shuffle(copy)
    return copy


def main() -> None:
    li = [1, 2, 3, 4, 5]
    kevert = shuffled(li)
    print(kevert, kevert[-1])
    print(li)


##########################


if __name__ == "__main__":
    main()