/*
 * szkielet.cpp
 */


#include <iostream>  //biblioteka wejscia/wyjscia

int main(int argc, char **argv)
{
	int liczba;  //deklaracja zmiennej liczba typu calkowitegoo, int - integer
    liczba = 12.78;
    // std::cout << liczba;  //F8 F9 F5
    cout << liczba;
    
    int a, b, c;  //deklaracja zmiennych
    a = b = c = 0;  //inicjalizacja zmiennych
    a = 10;  //przypisanie
    b = 2 * a;
    c = b + a;
    d = a / b;  //dzielnie 
    
    
    cout << "/n" << a << b << " " << (b -a);
    cout << " " << d
    
	return 0;
}

