def nums_que_comencen_per(llista):
    return sum(1 for nom in llista if nom.lower().startswith("a"))

def main():
    noms = ["anna", "pere", "alicia", "joan", "ariel"]
    print("Noms que comencen per 'a':", nums_que_comencen_per(noms))

if __name__ == "__main__":
    main()