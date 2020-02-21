#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stos.py

stos = []
SP = 0

def push(rozmiar, dane):
    global stos, SP
    if SP < rozmiar:
        stos[SP] = dane
        SP += 1
    else:
        print("Stack overflow!")

def main(args):
    global stos, SP
    rozmiar = int(input("podaj rozmiar stosu: "))
    stos = [None] * rozmiar
    push (rozmiar, 5)
    push (rozmiar, 9)
    push (rozmiar, 11)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
