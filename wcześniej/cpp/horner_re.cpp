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
    int i = 0;
    for (i = 0; i < st; i++) {
        cout << tbwsp[i] << "x^" << st-i << " + ";
    }
    cout << tbwsp[i] << endl;
}


float horner_re(int st, float tbwsp[], float x) {
    if (st == 0) return tbwsp[0];
    
    return horner_re(st-1, tbwsp, x) * x + tbwsp[st];
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
        cout << "Podaj współczynnik przy potędze " << stopien-i << ": ";
        cin >> tbwsp[i];
    }
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\ndla x = " << x << " wynosi: " << horner_re(stopien, tbwsp, x);
    cout << endl;
    
	return 0;
}

