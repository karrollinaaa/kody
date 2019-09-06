#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	char imie[20];
    char nazwisko[20];
    
    cout << "Ładnie proszę, podaj swoje imię: ";
    cin >> imie;
    cout << "Ładnie proszę, podaj swoje nazwisko: ";
    cin >> nazwisko;
    cout << "Witaj" << " " << imie << " " << nazwisko << "! :)" << endl;
    
	return 0;
}

