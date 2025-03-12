import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from . import connected_regions

license_plate = np.invert(connected_regions.plate_like_objects[2])
labelled_plate = measure.label(license_plate)

fig, ax1 = plt.subplots(1, figsize=(10, 5))
ax1.imshow(license_plate, cmap="gray")

character_dimensions = (0.35 * license_plate.shape[0], 0.70 * license_plate.shape[0], 0.05 * license_plate.shape[1], 0.15 * license_plate.shape[1])
min_height, max_height, min_width, max_width = character_dimensions

characters = []
counter = 0
column_list = []

for regions in regionprops(labelled_plate):
    y0, x0, y1, x1 = regions.bbox
    region_height = y1 - y0
    region_width = x1 - x0
    
    if region_height > min_height and region_height < max_height and region_width > min_width and region_width < max_width:
        roi = license_plate[y0:y1, x0:x1]
        
        # Calculate the width and height of the character
        # Use resize to standardize the dimensions
        resized_char = resize(roi, (128, 128))
        characters.append(resized_char)
        
        # Manteniamo un elenco delle colonne
        column_list.append(x0)
plt.show()
