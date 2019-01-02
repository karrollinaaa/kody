#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy2.py
#


def main(args):
    n = int(input("Podaj liczbę: "))
    silnia = 1
    for i in range (1, n + 1):
        silnia = silnia*i
    print (silnia)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
