def invertir_fitxer(nom):
    with open(nom, "r", encoding="utf-8") as f:
        linies = f.readlines()
    with open("invertit.txt", "w", encoding="utf-8") as out:
        for linia in reversed(linies):
            out.write(linia)

def main():
    nom = input("Nom del fitxer: ")
    invertir_fitxer(nom)

if __name__ == "__main__":
    main()
