def comptar_digits(n):
    return len(str(abs(n)))

def main():
    n = int(input("Introdueix un número (1–900000): "))
    print(f"Té {comptar_digits(n)} dígits")

if __name__ == "__main__":
    main()
