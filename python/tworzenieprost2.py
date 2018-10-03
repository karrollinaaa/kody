#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tworzenieprost.py
#  DANE WEJŚCIOWE: boki a i b prostokata
#  DANE WYJŚCIOWE: prostokat narysowny w terminalu z gwizadek o rozmiarach podfanych przez użytkownika 
#  
#  EXTRA: znak, ktorym rysowany jest prostokąt, pobierz od uzytkownika


def main(args):
    
    a = int(input("Podaj bok a: "))
    b = int(input("Podaj bok b: "))

    for i in range(a):
        for j in range(b):
            if j > 0 and j < b - 1:
                print(" ", end='')
            else:
                print("*", end='')

            print()
 
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
