/*
 * algorytm3.cpp
 * 
 * Copyright 2019  <>
 * 
 */


#include <iostream>

int main(int argc, char **argv)
{
	float stopien, radian;
    do {
        radian = stopien * M_PI / 180;
        cout << "cos(" << stopien << ") = " cos(radian) << endl;
        stopien += 10.0;
        
    }
	return 0;
}

