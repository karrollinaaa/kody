#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwerendy.py
#  
#  Copyright 2018  <>
#  

import sqlite3

def kwerenda1(cur):
    cur.execute("""
        SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

#SELECT klasa, COUNT(uczniowie.id) AS ile FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa GROUP BY klasa ORDER BY ile DESC
#SELECT klasa, nazwisko, imie, egz_mat FROM klasy INNER JOIN uczniowie ON klasy.id=uczniowie.id_klasa WHERE klasa='1A'
#SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE egz_hum > 40 AND egz_mat > 40 ORDER BY nazwisko ASC
#SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE plec=1 ORDER BY egz_hum DESC LIMIT 5
#SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie WHERE imie LIKE '%a' ORDER BY egz_hum DESC LIMIT 5
#SELECT nazwisko, imie, egz_hum, egz_mat FROM uczniowie ORDER BY egz_hum DESC LIMIT 5
#SELECT * FROM uczniowie WHERE nazwisko='Piasecki' AND imie='Rafał'
#SELECT COUNT(*) FROM uczniowie WHERE nazwisko='Piasecki'
#SELECT COUNT(*) FROM uczniowie WHERE nazwisko LIKE 'G%'

def main(args):
    baza_nazwa = 'uczniowie'
    table = ['uczniowie', 'klasy', 'przedmioty', 'oceny']
    
    con = sqlite3.connect(baza_nazwa + '.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora
    
    kwerenda1(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
