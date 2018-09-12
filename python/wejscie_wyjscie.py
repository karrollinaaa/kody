#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie_wyjscie.py
#  


def main(args):
    a = int(input("Podaj pierszą liczbę: "))
    print(a)
    
    b = int(input("Podaj drugą liczbę: "))
    print(b)
    
    print("Suma: ", a + b)
    
    print("Iloczyn: ", a * b)
    
    print("Iloraz: ", a / b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
