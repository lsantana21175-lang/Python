def taula(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

def main():
    n = int(input("Número (1–20): "))
    taula(n)

if __name__ == "__main__":
    main()
