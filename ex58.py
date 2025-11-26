def copiar_fitxer(origen, desti):
    with open(origen, "r", encoding="utf-8") as f1, open(desti, "w", encoding="utf-8") as f2:
        for linia in f1:
            f2.write(linia)

def main():
    copiar_fitxer("fitxer1.txt", "fitxer2.txt")
    print("Fitxer copiat!")

if __name__ == "__main__":
    main()