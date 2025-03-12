import os 
import shutil

path = "/Users/giovacasula/Downloads/archive"
destination_dir = os.path.join("/Users/giovacasula/projects/LicencePlateRecognition/test_immages")
extension = ".jpg"

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)
    print("Creo la directory di destinazione", destination_dir)

for filename in os.listdir(path):
    if filename.endswith(extension):
        source_file = os.path.join(path, filename)
        dest_file = os.path.join(destination_dir, filename)
        shutil.copy(source_file, dest_file)
        print(f"Copiato {source_file} in {dest_file}")
