def comptar_paraules(text):
    return len(text.split())

def main():
    t = input("Introdueix un text: ")
    print(f"Nombre de paraules: {comptar_paraules(t)}")

if __name__ == "__main__":
    main()