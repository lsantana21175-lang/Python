def es_palindrom(s):
    t = ''.join(ch.lower() for ch in s if ch.isalpha())
    return t == t[::-1]

def main():
    for w in ["radar", "hola", "Anna"]:
        print(w, es_palindrom(w))

if __name__ == "__main__":
    main()