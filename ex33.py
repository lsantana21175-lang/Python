def nums_que_comencen_per(llista, lletra):
    return sum(1 for nom in llista if nom.lower().startswith(lletra.lower()))

def main():
    noms = ["anna", "pere", "alicia", "joan", "ariel"]
    lletra = input("Introdueix una lletra: ")
    print(f"Noms que comencen per '{lletra}':", nums_que_comencen_per(noms, lletra))

if __name__ == "__main__":
    main()
