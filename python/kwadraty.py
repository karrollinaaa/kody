#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import turtle

def rysujKwadrat(zolw, bok, ile):
    #for i in range(4):
    zolw.forward(bok)
    zolw.right(90)
    if ile > 0:
        rysujKwadrat(zolw, bok)
    
def rysujKwadrat2(zolw, bok):
    for i in range(4):
        zolw.forward(bok)
        zolw.right(90)
    if bok > 0:
        rysujKwadrat2(zolw, bok-10)
    
def main(args):
    turtle.title("Kwadraty")
    turtle.setup(1000, 800)
    
    zolw = turtle.Turtle()
    zolw.color('pink')
    zolw.speed(0)
    
    #rysujKwadrat(zolw, 100, 4)
    zolw.begin_fill()
    rysujKwadrat2(zolw, 200)
    zolw.end_fill()
    
    turtle.done()
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
