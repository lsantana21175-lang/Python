from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"{self.especie} fa quisoc!")

class Cavall(Animal):
    def xerrar(self):
        print("Neigh!")

    def mourem(self):
        print("El cavall galopa.")

class Dofi(Animal):
    def xerrar(self):
        print("Eeeee!")

    def mourem(self):
        print("El dofí neda.")

class Abella(Animal):
    def xerrar(self):
        print("Bzzzz!")

    def mourem(self):
        print("L’abella vola.")

    def picar(self):
        print("L’abella pica!")

class Human(Animal):
    def __init__(self, nom, edat):
        super().__init__("Humà", edat)
        self.nom = nom

    def xerrar(self):
        print(f"{self.nom} diu hola!")

    def mourem(self):
        print(f"{self.nom} camina.")

class Fiet(Human):
    def __init__(self, nom, edat, pares):
        super().__init__(nom, edat)
        self.pares = pares

    def nompares(self):
        print(f"Els pares de {self.nom} són {', '.join(self.pares)}")

class Centaure(Cavall, Human):
    def xerrar(self):
        print("Centaure combina veu i galop!")

    def mourem(self):
        print("El centaure es mou com cavall i humà.")

class Xou:
    def xerrar(self):
        print("Xou fa xerrar!")

    def mourem(self):
        print("Xou es mou!")

    def quisoc(self):
        print("Xou fa quisoc!")

# Crear llista d’elements i cridar mètodes
elements = [Cavall("Cavall", 5), Dofi("Dofi", 3), Abella("Abella", 1), 
            Human("Joan", 30), Fiet("Anna", 10, ["Maria","Pere"]), 
            Centaure("Centaure", 15), Xou()]

for e in elements:
    e.xerrar()
    e.mourem()
    e.quisoc()