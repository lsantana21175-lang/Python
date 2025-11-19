def imprimir_taula(any_actual, dades):
    print(f"Any actual {any_actual}")
    print("Nom\tData naixement\tAnys que farà aquest any")
    for nom, any_naix in dades:
        print(f"{nom}\t{any_naix}\t{any_actual - any_naix}")

def main():
    anys = int(input("Any actual: "))
    dades = []
    for i in range(4):
        nom = input(f"Nom {i+1}: ")
        any_naix = int(input(f"Any naixement de {nom}: "))
        dades.append((nom, any_naix))
    imprimir_taula(anys, dades)

if __name__ == "__main__":
    main()