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
        SELECT * FROM uczniowie
    """)
    
    wyniki = cur.fetchall()
    for row in wyniki:
        print(row)

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
