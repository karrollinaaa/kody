def main(args):
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    c = int(input('Podaj trzecią liczbę: '))
 
    if a > b and a > c:
        print('Największa liczba: ', a)
    elif b > a and b > c:
        print('Największa liczba: ', b)
    else:
        print('Największa liczba: ', c)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
