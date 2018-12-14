#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import os

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #instancja bazy

### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza
    
        
class Kategoria(BazaModel):
    kategoria = CharField()

class Pytanie(BazaModel):
    pytanie = CharField()
    kat = ForeignKeyField(Kategoria, related_name='kategoria')

class Odpowiedz(BazaModel):
    p = ForeignKeyField(Pytanie, related_name='pytanie')
    odpowiedz = CharField()
    odpok = FloatField(default=0)

