/*
 * szyfr_przestawieniowy.cpp
 */
 
#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz){
    int ilosc = strlen(tekst);
    cout << ilosc << endl;
    int reszta = ilosc % klucz;
    if(reszta > 0) {
        for(int i = ilosc; i < ilosc + klucz - reszta; i++) {
            int kod = (int)tekst[];
        }
    }
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;

    cout << "Podaj tekst:\n";
    cin.getline(tekst, MAKS);
    cout << strlen(tekst) << endl;
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    szyfruj(tekst, klucz);

    return 0;
}
