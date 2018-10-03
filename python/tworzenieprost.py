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
    i = 0
    
    while i < a:
        a = a - 1
        print("*", end='')
        
    while i < b:
        b = b - 1
        print("*")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
