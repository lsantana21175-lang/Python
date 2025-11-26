def superposicio(a, b):
    return any(x in b for x in a)

def main():
    print(superposicio([1, 2, 3], [4, 5, 3]))
    print(superposicio(["a", "b"], ["c", "d"]))

if __name__ == "__main__":
    main()