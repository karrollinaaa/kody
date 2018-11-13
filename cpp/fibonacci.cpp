/*
 * fibonacci.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;


int fibonacci_it(int n) {
    int a = 0;
    int b = 1;
    int wynik = 0;
    if (n < 1) return a;
    else if (n < 2) return b;    
    for (int i = 2; i <= n; i++) {
        wynik = a + b;
        a = b;
        b = wynik;
    }
    return wynik;
}


int main(int argc, char **argv)
{
    int n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu n " << n << ":" << endl;
    cout << fibonacci_it(n);
	
    for (int i = 0; i <= n; i++) {
        cout << fibonacci_it(i) << endl;
    }
    
	return 0;
}

