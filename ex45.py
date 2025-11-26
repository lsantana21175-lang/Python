def digits_parells(n):
    return [int(x) for x in str(n) if int(x) % 2 == 0]

def main():
    n = int(input("Introdueix un número: "))
    print("Dígits parells:", digits_parells(n))

if __name__ == "__main__":
    main()
