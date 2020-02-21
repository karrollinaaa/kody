#include <iostream>
#include <cstdlib>
#include "osoba.h"

Osoba::Osoba() {
    imie = nazwisko = plec = "";
    wiek =  0;
}

Osoba::Osoba(string i, string n, int, string p); {
    imie = i;
    nazwiska = n;
    if (w > 0) wiek = w;
    else w = 0;
    plec = p;
}

