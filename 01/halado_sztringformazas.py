#!/usr/bin/env python3

# Ebben a szkriptben a formázásnál használjuk a minwidth és az igazítás funkciókat is.
# A minwidth-et a format függvénynél adhatjuk meg úgy, hogy az objektumokba írunk egy kettőspontot
# utána egy számmal. Ez a szám lesz az oszlop minimális szélessége. Az igazítást hasonló módon
# oldhatjuk meg, a kettőspont után rakhatunk <, ^, > jeleket (rendre balra, középre és jobbra igazítás).


def main():
    my_list = [('Takács', 'Balázs', 'PTI'), ('Süsü', 'Sárkány', 'PTI'), ('Spongyabob', 'Kockanadrág', 'PTI'), ('Herceg', 'András', 'GI'), ('Kovács', 'Balázs', 'MI')]

    print ('{0:<16} {1:^12} {2:>12}'.format('Vezetéknév', 'Keresztnév', 'Szak'))
    print ('-'*42)
    for i in my_list:
        print('{0:<16} {1:^12} {2:>12}'.format(i[0], i[1], i[2]))


if __name__ == "__main__":
    main()


# Forrás: http://knowledgestockpile.blogspot.com/2011/01/string-formatting-in-python_09.html