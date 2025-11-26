def te_clau(dic, clau):
    return clau in dic

def main():
    notes = {"Anna": 8, "Joan": 5.5}
    print(te_clau(notes, "Anna"))
    print(te_clau(notes, "Marta"))

if __name__ == "__main__":
    main()