#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py
# 

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #instancja bazy

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza
    
    
class Klasa(Baza_Model):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
        
class Uczen(Baza_Model):
    imie = CharField(default=0)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    

class Wynik(Baza_Model):
    egzhum = FloatField(default=0)
    egzmat = FloatField((default=0)
    egzjez = FloatField((default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    
    
def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() #połaczenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
