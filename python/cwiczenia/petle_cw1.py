#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(a, b):
    return a + b


def main(args):
    liczba = 0
    suma = 0
    while suma <= 75:
        liczba = int(input("Podaj liczbę: "))
        suma = suma + liczba
        
    print("Suma: ", suma)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
