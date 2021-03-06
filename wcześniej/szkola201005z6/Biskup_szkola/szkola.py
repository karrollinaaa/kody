#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='/t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    dane = dane_z_pliku('oceny.txt')
    print(dane)
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO oceny VALUES(?, ?, ?, ?)', dane)
    
    dane = dane_z_pliku('przedmioty.txt')
    print(dane)
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO przedmioty VALUES(?, ?, ?, ?)', dane)
    
    dane = dane_z_pliku('uczniowie.txt')
    print(dane)
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO uczniowie VALUES(?, ?, ?, ?, ?)', dane)


    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
