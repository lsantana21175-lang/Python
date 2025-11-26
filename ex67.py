def invertir(dic):
    return {v: k for k, v in dic.items()}

def main():
    print(invertir({"A": 1, "B": 2, "C": 3}))

if __name__ == "__main__":
    main()