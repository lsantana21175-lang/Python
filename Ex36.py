import random
import time

def intro():
    print("""En una època on els gegants governen Menorca.
Estem seguint el rastre de menjar, però ens trobem en una cruïlla.
Un talaiot és dels bons, l'altre de caníbals!
""")

def canviTalaiot():
    talaiot = ""
    while talaiot not in ["1", "2"]:
        talaiot = input("A quin Talaiot vols anar? (1 o 2): ")
    return talaiot

def trobada(talaiot):
    print("T'estàs apropant al talaiot...")
    time.sleep(1)
    gegantamic = random.randint(1, 2)
    if talaiot == str(gegantamic):
        print("Et convida a menjar! 😋")
        return True
    else:
        print("Se't menja d'un mos! 💀")
        return False

def main():
    punts = 0
    while True:
        intro()
        if trobada(canviTalaiot()):
            punts += 10
            print(f"Has guanyat! Tens {punts} punts.\n")
        else:
            print(f"Has perdut. Punts totals: {punts}")
            break
        if input("Vols tornar a jugar? (si/no): ").lower() not in ["si", "s"]:
            break

if __name__ == "__main__":
    main()