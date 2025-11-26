import os

def llegir_fitxer(nom_fitxer):
    """Llegeix el contingut d’un fitxer i retorna una llista de línies.
    Controla si el fitxer existeix o hi ha problemes d’obertura."""
    if not os.path.exists(nom_fitxer):
        print(f"Error: el fitxer {nom_fitxer} no existeix.")
        return []

    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            contingut = [linia.strip() for linia in f]
        return contingut
    except Exception as e:
        print(f"No s'ha pogut obrir el fitxer: {e}")
        return []

# Exemple d’ús
if __name__ == "__main__":
    noms = llegir_fitxer("Ex12.txt")
    print(noms)