def aplicacio1():
    print("Aplicació 1: llistes i nombres aleatoris")

def aplicacio2():
    print("Aplicació 2: fitxers i agenda")

def aplicacio3():
    print("Aplicació 3: joc Mastermind / talaiòtics")

def aplicacio4():
    print("Aplicació 4: objectes i herència")

def aplicacio5():
    print("Aplicació 5: treball amb big data o scraping")

def aplicacio6():
    print("Aplicació 6: servei web")

menu = {
    1: aplicacio1,
    2: aplicacio2,
    3: aplicacio3,
    4: aplicacio4,
    5: aplicacio5,
    6: aplicacio6
}

def main():
    while True:
        print("\nSelecciona una aplicació (1-6) o 0 per sortir:")
        opcio = int(input())
        if opcio == 0:
            break
        if opcio in menu:
            menu[opcio]()
        else:
            print("Opció no vàlida")

if __name__ == "__main__":
    main()