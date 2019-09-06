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
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
    
        
class Uczen(BazaModel):
    imie = CharField(default=0)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    

class Wynik(BazaModel):
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')
    
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() #połaczenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl2a = Klasa(nazwa="2A", roknaboru=2010, rokmatury=2013)
    kl2a.save()
    
    ul = Uczen(imie="Mateusz", nazwisko="Bernyś", plec=False, klasa=kl2a)
    ul.save()
    
    kl1a = Klasa(nazwa="1A", roknaboru=2011, rokmatury=2014)
    kl2a.save()
    
    ul1 = Uczen(imie="Paweł", nazwisko="Sroczyński", plec=False, klasa=kl1a)
    ul1.save()
    
    uczniowie = Uczen.select()
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
