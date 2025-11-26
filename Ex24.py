def crear_punts(lst):
    for n in lst:
        print("." * n)

def dibuixar_imatge():
    crear_punts([2, 3, 4])

if __name__ == "__main__":
    dibuixar_imatge()