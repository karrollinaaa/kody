/*
 * szablon.cpp
 */


#include <iostream>

using namespace std;

int suma(int a, int b){
    
    return a + b;
    
    }
    
int roznica(int a, int b){
    
    return a - b;
    
    }
    
int iloczyn(int a, int b){
    
    return a * b;
    
    }
    
int iloraz(int a, int b){
    
    return a / b;
    
    }
int main(int argc, char **argv)
{ /* DRY - Don't repat yourself */
	
    int a, b;
    
    a = b = 0;
    
    cout << "Podaj liczbę: ";
    cin >> a;
    
    cout << endl << "Podaj drugą liczbę: ";
    cin >> b;
    
    cout << a << "," << b;
    
    cout << endl << "suma: "; 
    cout << suma(a, b);
    
    cout << endl << "różnica: ";
    cout << roznica(a, b);
    
    cout << endl << "iloczyn: ";
    cout << iloczyn(a, b);
    
    cout << endl << "iloraz: ";
    cout << iloraz(a, b);
    
    
    
	return 0;
}
