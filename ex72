import os

# Crear directori
path = "/home/cicles/AO/Prova"
os.makedirs(path, exist_ok=True)
os.chdir(path)

# Crear fitxer Ex12.txt amb noms d’estudiants
companys = ["Anna", "Joan", "Marta", "Pau"]
with open("Ex12.txt", "w", encoding="utf-8") as f:
    for nom in companys:
        f.write(nom + "\n")

# Afegir noms dels professors
professors = ["Professor1", "Professor2"]
with open("Ex12.txt", "a", encoding="utf-8") as f:
    for nom in professors:
        f.write(nom + "\n")

# Llegir tot i posar en llista
with open("Ex12.txt", "r", encoding="utf-8") as f:
    noms_totals = [linia.strip() for linia in f]

print(noms_totals)