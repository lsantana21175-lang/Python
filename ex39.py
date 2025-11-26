def calcul_interes(capital, interes, anys):
    return capital * (1 + interes / 100) ** anys

def main():
    c = float(input("Capital (50000–800000): "))
    i = float(input("Interès (0.5–13): "))
    a = int(input("Anys (3–40): "))
    final = calcul_interes(c, i, a)
    print(f"Al final de {a} anys tindràs {final:.2f}€")

if __name__ == "__main__":
    main()