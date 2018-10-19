#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import csv
import os.path


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    
    if not os.path.isfile(nazwa_pliku):
        print("plik {} nie istnieje!".format(nazwa_pliku))
        return dane
    
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delmiter=separator)
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane


def kwerenda_1(cur):
    cur.execute("""
        SELECT * FROM magazyn
    """)

    """
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps) ORDER BY downloads DESC LIMIT 5;
    SELECT COUNT(name) FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT category, SUM(downloads) AS suma_pobran FROM fakeapps GROUP BY category ORDER BY suma_pobran DESC;


    """
    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:  # odczytywanie kolejnych rekordów
        print(tuple(row))  # drukowanie pól

def ile_kolumn(tab):
    i = 0
    for kol in cur.execute("PRAGMA table_info('" + tab +"')")
        i += 1
    return 1

def main(args):
    con = sqlite3.connect(baza_nazwa'.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('magazyn.sql', 'r') as plik:
        cur.executescript(plik.read())
        
    for tab in table:
        ile = ile_kolumn(tab) # ile mamy pol w tabeli
        dane = dane_z_pliku(tab + '.csv')
        ile_d = len(dane[0])
        if ile > ile_d: #primary key autoincrement
            dane2 = [] #tymczasowa lista na dane
            for r in dane:



    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
