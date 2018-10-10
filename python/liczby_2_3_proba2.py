#!/usr/bin/env python
# -*- coding: utf-8 -*-


def liczby2():
    
    ile = 0 # ilość liczb
    
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print("{}{}".format(i,j), end="")
                ile += 1
                
    return ile
			          

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
