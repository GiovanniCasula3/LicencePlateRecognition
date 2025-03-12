import os

# Percorso principale della directory contenente le cartelle
rename_directory = "/Users/giovacasula/Projects/LicencePlateRecognition/test_immages"

letters = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK", "LL", "MM",
    "NN", "OO", "PP", "QQ", "RR", "SS", "TT", "UU", "VV", "WW", "XX", "YY", "ZZ"
]

new_name = "car"
ext = ".jpg"
elementi = os.listdir(rename_directory)
numero_elem = list(elementi)

for elemento in elementi:
    folder_path = os.path.join(rename_directory, elemento)

        # Lista e ordina i file all'interno della cartella
    files = sorted(os.listdir(folder_path))
    for idx, filename in enumerate(files):
        old_file = os.path.join(folder_path, filename)
    
        # Estrai l'estensione del file
        _, ext = os.path.splitext(filename)
        new_filename = f"{elemento}_{idx}{ext}"
        new_file = os.path.join(folder_path, new_filename)
        
        # Stampa l'operazione di rinomina (utile per debug)
        print(f"Rinomino {old_file} in {new_file}")
        os.rename(old_file, new_file)
