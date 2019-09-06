#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #instancja bazy

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza
    
        
class Klasa(BazaModel):
    klasa = CharField()
    roknaboru = DateField()
    rokmatury = DateField()


class Uczen(BazaModel):
    imie = CharField()
    nazwisko = CharField()
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    

class Przedmiot(BazaModel):
    przedmiot = CharField()
    nazwisko_naucz = CharField()
    imie_naucz = CharField()
    plec_naucz = IntegerField()
    
    
class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = IntegerField()
