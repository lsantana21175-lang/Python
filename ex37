import random

def comparar(secret, intent):
    encertats = sum(s == i for s, i in zip(secret, intent))
    coincidencies = sum(min(secret.count(x), intent.count(x)) for x in set(intent)) - encertats
    return encertats, coincidencies

def main():
    secret = "".join(str(random.randint(0, 9)) for _ in range(4))
    print("He pensat un número de 4 xifres!")
    while True:
        intent = input("Introdueix un número de 4 xifres: ")
        if intent == secret:
            print("🎉 Encerta't completament!")
            break
        encertats, coincidencies = comparar(secret, intent)
        print(f"Encertats: {encertats}, Coincidències: {coincidencies}")

if __name__ == "__main__":
    main()