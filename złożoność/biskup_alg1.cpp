/*
 * biskup_alg1.cpp
 */


#include <iostream>

int main(int argc, char **argv)
{
	int a;
    int i;
    cout << "podaj liczbę: ";
    cin >> a;
    if (0 < a && a < 100) {
        i = 2;
        if (a == i)
            cout << a << "to liczba parzysta";
        else {
            i = i + 2; 
            if (i == 100) {
                cout << a << "nie jest liczbą parzystą";
            }
        }
    }
    
    
    
	return 0;
}

