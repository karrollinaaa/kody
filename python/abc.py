#
#Program pobiera trzy liczby od urzytkownika, a nasteonie wyswietla liczbe najwieksza
#

def maks(a,b,c):
    m = None
    if a > b:
        if a > c:
            m = a
    elif b > c:
            m = b
    print("najwieksza:", m)
    return m
            
def main(args):
    assert(maks(3,2,1)
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
