#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie_wyjscie.py
#  
# zasięg zmiennych: lokalny(ograniczony funkcją)


def suma(a, b):
    return a + b

def roznica(a, b):
    return a - b
    
def iloczyn(a, b):
    return a * b
    
def iloraz(a, b):
    return a / b

def main(args):
    a = int(input("Podaj pierszą liczbę: "))
    print(a)
    b = int(input("Podaj drugą liczbę: "))
    print(b)
    
    print("Suma: ", suma(a, b))
    print("Różnica: ", roznica(a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
