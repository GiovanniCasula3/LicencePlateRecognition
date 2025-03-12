import os
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import joblib
from skimage.io import imread
from skimage.filters import threshold_otsu

# Lista delle classi (numeri e lettere)
letters = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK", "LL", "MM",
    "NN", "OO", "PP", "QQ", "RR", "SS", "TT", "UU", "VV", "WW", "XX", "YY", "ZZ"
]

def read_training_data(training_directory):
    """
    Legge i dati di addestramento dalle cartelle specificate.
    Per ogni lettera, legge 10 immagini, le converte in immagini binarie 
    (usando la soglia di Otsu) e le appiattisce in un vettore.
    """
    image_data = []
    target_data = []
    
    for letter in letters:
        for i in range(10):
            image_path = os.path.join(training_directory, letter, f"{letter}_{i}.png")
            # Legge l'immagine in scala di grigi
            img = imread(image_path, as_gray=True)
            # Converte l'immagine in binaria usando la soglia di Otsu
            binary_img = img < threshold_otsu(img)
            # Appiattisce l'immagine in un vettore 1D
            flat_img = binary_img.reshape(-1)
            image_data.append(flat_img)
            target_data.append(letter)
            
    return np.array(image_data), np.array(target_data)

def cross_validation(model, num_of_fold, train_data, train_labels):
    scores = cross_val_score(model, train_data, train_labels, cv=num_of_fold)
    print(f"Risultati della cross validation a {num_of_fold} fold:")
    print(scores * 100)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    training_dataset_dir = os.path.join(current_dir, "license-plate-dataset")
    
    image_data, target_data = read_training_data(training_dataset_dir)
    
    # Creazione del modello SVM
    svc_model = SVC(kernel="linear", probability=True)
    
    # Valutazione del modello tramite cross validation
    cross_validation(svc_model, 4, image_data, target_data)
    
    # Addestramento del modello sui dati
    svc_model.fit(image_data, target_data)
    
    # Salvataggio del modello addestrato
    save_directory = os.path.join(current_dir, "models", "svc")
    os.makedirs(save_directory, exist_ok=True)
    model_path = os.path.join(save_directory, "svc.pkl")
    joblib.dump(svc_model, model_path)
    print("Modello salvato nella cartella", save_directory)
