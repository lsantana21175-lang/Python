def elimina_duplicats(lst):
    return list(dict.fromkeys(lst))

def main():
    print(elimina_duplicats([1, 2, 2, 3, 4, 4, 5]))

if __name__ == "__main__":
    main()
