  /*
 * prostokat.cpp
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

using namespace std;

int pole(int a, int b){
    
    return a * b;
    
    }
    
int obwod(int a, int b){
    
    return a + b + a + b;
    
    }    

int main(int argc, char **argv)
{
	int a, b;
    
    a = b = 0;
    
    cout << "Podaj bok a: ";
    cin >> a;
    
    cout << endl << "Podaj bok b: ";
    cin >> b;
    
    cout << a << "x" << b;
    
    cout << endl << "pole: "; 
    cout << pole(a, b);
    
    cout << endl << "obwod: ";
    cout << obwod(a, b);
    
	return 0;
}

