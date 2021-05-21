#!/usr/bin/env python3


def my_func(li):
    return li[1]


def main():
    to_sort = [[2,6],[1,3],[5,4]]
    print(to_sort)
    print(sorted(to_sort, key=lambda l: l[1]))
    print(sorted(to_sort, key=my_func))


##########################


if __name__ == "__main__":
    main()