def ordenar_freq(dic):
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)

def main():
    d = {"el": 3, "sol": 2, "dia": 1}
    print(ordenar_freq(d))

if __name__ == "__main__":
    main()