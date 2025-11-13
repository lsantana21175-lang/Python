def es_major(edat: int) -> str:
    if edat > 18:
        return "Major d'edat"
    elif edat == 18:
        return "Exactament 18 anys"
    else:
        return "No és major d'edat"

def main():
    edat = int(input("Introdueix la teva edat: "))
    print(es_major(edat))

if __name__ == "__main__":
    main()