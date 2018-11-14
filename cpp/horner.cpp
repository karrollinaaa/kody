/*
 * horner.cpp
 * 
 * w(x) = 2x^3 + 3x^2 + 5x + 4  => 6mnożeń i 4dodawania
 * w(x) = x(2x^2 + 3x + 5) + 4
 * w(x) = x (x(2x +3) + 5) + 4  => 3mnożenia i 3 dodawania
 * 
 */


#include <iostream>

using namespace std;

void drukujw(int st, float tbwsp[]) {
    for (int i = 0; i < st; i++) {
        cout << tbwsp[i] << "x^" << st-i << " + ";;
    }
}

int main(int argc, char **argv)
{
    int stopien = 0;
    float x = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp;  //wskaźnik - przechowuje adres komórki w pamięci
    tbwsp = new float [stopien+1];
    for (int i=0; i <= stopien; i++) {
        cout << "Podaj współczynnik przy potędze " << stopien-i << ":";
        cin >> tbwsp[i];
    }
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: ";
    cout << endl;
    
	return 0;
}

