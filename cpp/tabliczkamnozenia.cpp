/*
 * tabluczkamnozenia.cpp
 * 
 * Copyright 2018  <>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <iomanip>

using namespace std;

void tabliczka(int a,int b) {
    for(int i = 1; i <= a; i++) {
        for (int j = 1; j <= b; j++) {
            cout << setw(4) << i * j;
            }
            cout << endl;
        }
    }

int main(int argc, char **argv)
{
	int a, b;  //deklaracja
    a = b = 0;  //inicjacja
    cout << "Podaj zakres 1: ";
    cin >> a;
    cout << "POdaj zakres 2: ";
    cin >> b;
    tabliczka(a, b);
	return 0;
}

