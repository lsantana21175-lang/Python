def crear_diccionari():
    d = {}
    for _ in range(3):
        nom = input("Nom: ")
        nota = float(input("Nota: "))
        d[nom] = nota
    return d

def main():
    alumnes = crear_diccionari()
    print("Diccionari de notes:", alumnes)

if __name__ == "__main__":
    main()
