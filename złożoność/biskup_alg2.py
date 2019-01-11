#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  biskup_alg2.py
#  


def main(args):
    a = int(input("podaj liczbę: "))
    i = 0
    if 0 < a and a < 100:
        i = 2 
        if a == i:
            print(a, "to liczba parzysta")
        else:
            i = i + 2
            if i > a:
                print(a, "nie jest liczbą parzystą")
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
