/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[])
{
    int i = 0;
    int biale = 0;
    while(tab[i] != '\0') {
        
        if (tab[i] == ' ' || tab[i] == '\t') 
             biale++;
        else
            cout << tab[i];
        
        i++; // zwiekszanie indeksu
    }
    cout << "/nznaków białych: " << biale << endl;
}

int main(int argc, char **argv)
{
    const int rozmiar = 20; //deklaracja stałej 
	char znaki[rozmiar];  //deklaracja
    cout << "Jak się nazywasz?  ";
    cin.getline(znaki, rozmiar);
    cout << "cześć " << znaki << endl;
    licz_znaki(znaki);
    
	return 0;
}

