def suma_digits(n):
    return sum(int(x) for x in str(abs(n)))

def main():
    n = int(input("Introdueix un número: "))
    s = suma_digits(n)
    print(f"Suma de dígits: {s}")
    print("És parell" if s % 2 == 0 else "És senar")

if __name__ == "__main__":
    main()