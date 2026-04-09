from pathlib import Path


def percorso_assoluto(nome:str) -> Path:
    cartella_script = Path(__file__).parent
    file_input = cartella_script / nome
    return file_input

def crea_nome_file(riga: str) -> str:
    nome_cognome = riga.lower().split(" ")
    
    if len(nome_cognome) < 2 or (len(nome_cognome[0]) <= 0 and len(nome_cognome[1]) <= 0):
        return 
    
    nome = nome_cognome[0].strip()
    cognome = nome_cognome[1].strip()
    return f"{cognome}_{nome}.txt"


def crea_file_da_elenco(percorso_input: Path, cartella_output: Path) -> None:
    if not percorso_input.exists():
        print(f"Errore: il file {percorso_input} non esiste.")
        return

    cartella_output.mkdir(exist_ok=True)
    print("Creo file al percorso: " , cartella_output)

    with percorso_input.open("r", encoding="utf-8") as file:
        righe = file.readlines()

    for riga in righe:
        nome_file = crea_nome_file(riga)
        
        percorso_file = cartella_output / nome_file

        percorso_file.write_text("", encoding="utf-8")
        print(f"Creato file: {nome_file}")


if __name__ == "__main__":
    file_input = percorso_assoluto("elenco_nomi.txt")
    cartella_output = percorso_assoluto("output")

    crea_file_da_elenco(file_input, cartella_output)