#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
#

def trojkat(a, b, c):
    """
    Funkcja przyjmuje te liczby - dlugosci boków trojkata
    Funkcja sprawdza, czy da się z nich zbudować trójkat
    Funkcja zwraca True jeśli się da, False w przeciwnym razie
    """
    wynik = False
    
    # warunek1 and warunek2
    # warunek1 or waruunek2
    # not warunek2
    
    if a + b > c and a + c > b and b + c > a:
        wynik = True
    
    return wynik
    

def main(args):
    assert(trojkat(3, 6, 8) == True)
    assert(trojkat(9, 3, 5) == False)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
