#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  

"""
def main(args):
    
    a = int(input("podaj liczbe: "))
    b = int(input("podaj druga liczbe: "))
    for liczba in range(a,b):
        if not liczba % 2 == 0:
            print(liczba)
    return 0
"""

def main(args):
    
    start = int(input("liczba1: "))
    stop = int(input("liczba2: "))
    
    while start >= stop:
        stop = int(input("podaj wieksza liczbe niz pierwszą! Liczba2: "))
    
     for liczba in range(start, stop + 1):
        if not liczba % 2:
            print(liczba)
    #else:
        #print("będny zakres")
        
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
