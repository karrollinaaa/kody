#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv
import os.path


def dane_z_pliku(nazwa_pliku, separator=','):
    dane = []  # pusta lista na dane
    
    if not os.path.isfile(nazwa_pliku):
        print("plik {} nie istnieje!".format(nazwa_pliku))
        return dane
    
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def kwerenda_1(cur):
    cur.execute("""

    """)
    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:  # odczytywanie kolejnych rekordów
        print(tuple(row))  # drukowanie pól


    

def main(args):
    baza_nazwa = 'pracownicy'
    table = ['pracownicy', 'kontakt', 'place', 'stanowiska']
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open(baza_nazwa + '.sql', 'r') as plik:
        cur.executescript(plik.read())
        

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
