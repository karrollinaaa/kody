#include <iostream>
#include <cstdlib>
using namespace std;

void losowe(int tab[], int roz)
{
        srand(time(NULL));
        
        for (int i = 0; i < roz; i++) 
        {
            tab[i] =rand() %31;
        }
}

void druk (int tab[], int roz)
{
    for (int i = 0; i < roz; i++) 
    {
        cout << tab[i] << ' ';
    }
}


int main(int argc, char **argv)
{
	int rozmiar = 5;
    int tablica[rozmiar];
    
    losowe(tablica, rozmiar);
    druk(tablica, rozmiar);
    
	return 0;
}

