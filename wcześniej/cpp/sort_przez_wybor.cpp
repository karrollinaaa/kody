
/*
 * sortowanie.cpp
 */


#include <iostream>

using namespace std;

void wypelnij_losowe(int tab[], int roz)
{   
    srand(time(NULL));  // inicjacja generatora pseudolosowych
    
    for (int i = 0; i < roz; i++)
    {
        tab[i] = rand() % 101;  
    }
}

void drukuj(int tab[], int roz)
{    
    for (int i = 0; i < roz; i++)
    {
        cout << tab[i] << ' ';
    }
}


void select_sort(int tab[], int n)
{
    cout << "\nSortowanie przez wybór:\n";
    
    int k;
    for(int i = 0; i < n; i++)
    {
        k = i;
        for(int j = i + 1; j <n; j++)
        {
            if(tab[j]<tab[k])
            {
                k = j;
                zamien2(tab, j);
            }
        }
    }
}

int main(int argc, char **argv)
{
    int rozmiar = 20;
    int tablica[rozmiar]; //statyczna deklaracja tablicy
    
    wypelnij_losowe(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl;
    select_sort(tablica, rozmiar);
    drukuj(tablica, rozmiar);
        
	return 0;
}
