#!/usr/bin/env python
# -*- coding: utf-8 -*-

class KontoBasic():
    def __init__(self, ile=0, dane={}):
        self.bilans = ile
        self.osoba = dane
        
    def wplata(self, ile):
        self.bilans += int(ile)
        return self.bilans
        
    def wyplata(self, ile):
        self.bilans -= int(ile)
        return self.bilans

konta = [
    KontoBasic(100, {'imie': 'Ala', 'nazwisko': 'Kot'}),
    KontoBasic(100, {'imie': 'Ela', 'nazwisko': 'Pies'}),
]
kto = input('Imię: ')
klient = None
for k in konta:
    if k.osoba['imie'] == kto:
        klient = k
        
class KontoPremium(KontoBasic):
    def __init__(self, ile=0, osoba={}, debet=0):
        super().__init__(ile, dane)
        self.debet = debet
        
    def wyplata9self, ile):
        if self.bilans - ile < self.debet:
            print("Brak środków")
            return self.bilans
        else:
            return super(). wyplata(ile)

while True:
    op = input('Operacja: ').strip()
    if op == '+':
        ile = input('Wpłata: ')
        klient.wplata(ile)
    elif op == '-':
        ile = input('Wypłata: ')
        klient.wyplata(ile)
    else:
        break
    print('Konto:', klient.bilans)
