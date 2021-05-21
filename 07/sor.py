#!/usr/bin/env python3


class Verem:
    def __init__(self):
        self.data = []

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
            return self.data.pop()
        else:
            print("Üres veremből nem tudunk kivenni.")

            return None


# Veremnek a verem készítése feladathoz implementált saját vermemet használtam

class MyQueue:
    def __init__(self):
        self.verem1 = Verem()
        self.verem2 = Verem()

    def __str__(self):
        return " ".join(str(elem) for elem in self.verem1.data)

    def append(self, elem):
        self.verem1.betesz(elem)
        self.verem2.data = self.verem1.data[::-1]

    def popleft(self):
        if self.size():
            self.verem1.data = self.verem2.data[::-1][1:]
            
            return self.verem2.kivesz()
        else:
            print("Üres sorból nem tudunk törölni.")

            return None

    def is_empty(self):
        return self.verem1.ures()

    def size(self):
        return self.verem1.meret()


def main():
    teszt = MyQueue()
    teszt.append(5)
    teszt.append(10)
    print(teszt)
    x = teszt.popleft()
    print(x)
    print(teszt)
    print(teszt.is_empty())
    print(teszt.size())


##########################


if __name__ == "__main__":
    main()