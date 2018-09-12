#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py
#  


def pole(a, b):
    return a * b

def obwod(a, b):
    return a + b + a + b 
    

def main(args):
    a = int(input("Podaj bok a: "))
    print(a)
    b = int(input("Podaj bok b: "))
    print(b)
    
    print("Pole: ", pole(a, b))
    
    print("obwod: ", obwod(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
