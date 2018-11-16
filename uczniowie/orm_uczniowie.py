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
    
        
class Klasa(BazaModel):
    klasa = CharField()
    roknaboru = IntegerField()
    rokmatury = IntegerField()


class Uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='numer')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    

class Przedmiot(BazaModel):
    przedmiot = CharField()
    nazwisko_naucz = CharField()
    imie_naucz = CharField()
    plec_naucz = BooleanField()
    
    
class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    przedmiot = ForeignKeyField(Przedmiot, related_name='cos')
    ocena = IntegerField()
    

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() #połaczenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
