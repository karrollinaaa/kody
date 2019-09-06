#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy1.py
#  


def wersja1():
    n = int(input("Podaj liczbę: "))
    i = 1
    for i in range(1, n):
        print(i)
    
def wersja2():
    n = int(input("Podaj liczbę: "))
    i = 1
    while i < n:
        print(i)
        i += 2
        
##algorytm częsciowo poprawny, skonczony, o zdolności liniowej O(n)

def main(args):
    wersja2()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
