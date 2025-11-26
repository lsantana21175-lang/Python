import random

def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

def main():
    llista = llista_20_elements()
    print(llista)
    print("Té duplicats:", len(llista) != len(set(llista)))

if __name__ == "__main__":
    main()