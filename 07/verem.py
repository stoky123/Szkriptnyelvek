#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.data = []
        print("Üres verem létrehozása.")

    def __str__(self):
        return "[" + " ".join(str(elem) for elem in self.data)

    def meret(self):
        return len(self.data)

    def ures(self):
        return not bool(self.meret)
    
    def betesz(self, elem):
        self.data.append(elem)
    
    def kivesz(self):
        if self.meret():
            self.data.pop()

            return sum(self.data)
        else:
            print("Üres veremből nem tudunk kivenni.")

            return None


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


##########################


if __name__ == "__main__":
    main()