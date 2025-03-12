import os

# Percorso della directory in cui sono presenti i file
rename_directory = "/Users/giovacasula/Projects/LicencePlateRecognition/test_immages"

# Nome base per il nuovo file e l'estensione (in questo esempio ".jpg")
new_name = "car"
ext = ".jpg"

# Ottiene la lista dei file presenti nella directory (escludendo eventuali cartelle)
files = [f for f in os.listdir(rename_directory) if os.path.isfile(os.path.join(rename_directory, f))]
files = sorted(files)  # Ordina i file

# Itera su tutti i file, rinominandoli uno per uno
for idx, filename in enumerate(files):
    old_file = os.path.join(rename_directory, filename)
    new_filename = f"{new_name}_{idx}{ext}"
    new_file = os.path.join(rename_directory, new_filename)
    
    print(f"Rinomino {old_file} in {new_file}")
    os.rename(old_file, new_file)
