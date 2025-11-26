def from_base(s, base):
    return int(s, base)

def to_base(n, base):
    if base == 2:
        return bin(n)[2:]
    if base == 8:
        return oct(n)[2:]
    if base == 10:
        return str(n)
    if base == 16:
        return hex(n)[2:].upper()
    raise ValueError("Base desconeguda")

def main():
    s, base_from = input("Valor i base d'origen (ex: 1010 2): ").split()
    n = from_base(s, int(base_from))
    base_to = int(input("Base destí (2/8/10/16): "))
    print(to_base(n, base_to))

if __name__ == "__main__":
    main()