from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import numpy as np

# Carica l'immagine in scala di grigi.
car_imm = imread("test_immages/car6.jpg", as_gray=True)
print("Dimensioni immagine:", car_imm.shape)

# Se l'immagine è normalizzata in [0,1], moltiplichiamo per 255 e convertiamo in uint8 per ottenere valori standard in scala di grigi
gray_car_imm = (car_imm * 255).astype(np.uint8)

# Visualizzazione dell'immagine in scala di grigi e dell'immagine binarizzata tramite la soglia di Otsu
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(gray_car_imm, cmap="gray")
ax1.set_title("Immagine in Scala di Grigi")
ax1.axis("off")

# Calcola la soglia di Otsu e applica la binarizzazione
threshold_value = threshold_otsu(gray_car_imm)
binary_car_imm = gray_car_imm > threshold_value

ax2.imshow(binary_car_imm, cmap="gray")
ax2.set_title("Immagine Binaria")
ax2.axis("off")

plt.tight_layout()
plt.show()

