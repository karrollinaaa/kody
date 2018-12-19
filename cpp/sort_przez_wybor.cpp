/*
 * sort_przez_wybór.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>
using namespace

void los(int tab[], int roz)
{   
    srand(time(NULL));  // inicjacja generatora pseudolosowych
    
    for (int i = 0; i < roz; i++){
        tab[i] = rand() % 101;  
    }
}

void drukuj(int tab[], int roz)
{    
    for (int i = 0; i < roz; i++){
        cout << tab[i] << ' ';
    }
}

int sort(int tab[], int n) {
     for (i; i < n; i++) {
        if (tab[i]
    }
}

int main(int argc, char **argv)
{
	int i = 1;
    int tablica[rozmiar]; //statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
	return 0;
}

