#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ctrl+shift+p wywoływanie

import random


def main(args):
    liczba = random.randint(1, 10)
    print("wylosowano:", liczba)

    odp = input("podaj liczbę od 1 do 10:")
    print("podano:", odp)

    if liczba == int(odp):
        print("zgadłeś")
    else:
        print("spróbuj jescze raz")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
