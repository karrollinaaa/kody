#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import turtle

def rysujKwadrat(zolw, bok, ile):
    #for i in range(4):
    zolw.forward(bok)
    zolw.right(90)
    if ile > 0:
        rysujKwadrat(zolw, bok, ile-1)
    
def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('pink')
    
    rysujKwadrat(zolw, 100, 4)
    
    turtle.done()
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
