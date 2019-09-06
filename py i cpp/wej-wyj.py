def main(args):
    a = input("Podaj imię: ")
    b = input("Podaj nazwisko: ")
    
    print("Witaj", a, b + "! :)")
    
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
