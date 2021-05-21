#!/usr/bin/env python3


def feloszt(li):
    li = li.split(',')
    li = [elem.split('-') for elem in li]

    result = ""
    for elem in li:
        if len(elem) == 1:
            result += elem[0] + ','
        else:
            for page in range(int(elem[0]), int(elem[1])+1):
                result += str(page) + ','

    return result[:-1]


def main():
    li = "1-4,7,9,11-15"
    print(feloszt(li))


##########################


if __name__ == "__main__":
    main()