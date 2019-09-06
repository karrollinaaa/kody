#include <iostream>
using namespace std;


void wypelnij_los(int tab[], int n) {
    srand(time(NULL));//inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < n; i++) {
        tab[i] = rand() % 101;
    }
}


void drukuj(int tab[], int n) {
    for(int i = 0; i < n; i++) {
        cout << tab[i] << " ";
    }
}


void sort_insert(int tab[], int n) {
    int i, j, tmp;
    for (i = 1; i < n; i++) {
        tmp = tab[i];
        j = i - 1;
        while (j >= 0 && tab[j] > tmp) {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}

int szukaj_bin_lin(int tab[], int n, int szuk) {
    int p, k, s;
    p = 0; k = n-1;
    while (p <= k) {
        s = (p + k) / 2;
        if (tab[s] == szuk) {
            return s;
        } else if (szuk < tab[s])  k =s -1;
        else p = s + 1;
    }

    return -1;
}

int main(int argc, char **argv)
{
    int n =20;
    int tab[n];
    wypelnij_los(tab, n);
    drukuj(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: "; cin >> szuk;
    sort_insert(tab, n);
    drukuj(tab, n);
    
    int indeks = szukaj_bin_lin(tab, n, szuk);
    if (indeks>=0) cout << "Znaleziono: " << indeks << endl;
    else cout << "Nie znaleziono";
    
    
	return 0;
} 
