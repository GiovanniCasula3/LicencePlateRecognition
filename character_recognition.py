import kagglehub

# Download latest version
path = kagglehub.dataset_download("/Users/giovacasula/Projects/LicencePlateRecognition/license-plate-dataset/")

print("Path to dataset files:", path)

import os 
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import joblib
from skimage.io import imread
from skimage.filters import threshold_otsu

letters = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "AA", "BB", "CC", "DD", "EE", "FF", "GG", "HH", "II", "JJ", "KK", "LL", "MM",
    "NN", "OO", "PP", "QQ", "RR", "SS", "TT", "UU", "VV", "WW", "XX", "YY", "ZZ"
]

def read_training_data(training_directory):
    image_data = []
    target_data = []
    for each_letter in letters:
        for each in range(10):
            image_path = os.path.join(training_directory, each_letter, each_letter + "_" + str(each) + ".jpg")
            # Read each character form a given immage
            img_details = imread(image_path, as_gray=True)
            # Converts each character into binary image
            binary_image = img_details < threshold_otsu(img_details)
            flat_bin_image = binary_image.reshape(-1)
            image_data.append(flat_bin_image)
            target_data.append(each_letter)
    return (np.array(image_data), np.array(target_data))

def cross_validation(model, num_of_fold, train_data, train_label):
    accuracy_result = cross_val_score(model, train_data, train_label, cv=num_of_fold)
    print("Cross Validation Result for", str(num_of_fold), "fold")
    print(accuracy_result * 100)

current_dir = os.path.dirname(os.path.realpath(__file__))
training_dataset_dir = os.path.join(current_dir, "training_data/train20X20/")
image_data, target_data = read_training_data(training_dataset_dir)

svc_model = SVC(kernel="linear", probability=True)
cross_validation(svc_model, 4, image_data, target_data)

svc_model.fit(image_data, target_data)
save_directory = os.path.join(current_dir, "models/svc/")
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
joblib.dump(svc_model, save_directory + "/svc.pkl")
print("Modello salvato nella cartella", save_directory)